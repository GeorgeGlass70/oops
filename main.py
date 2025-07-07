import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from prompts import system_prompt
from call_function import call_function, available_functions



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)




def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py \"<your prompt here>\" [--verbose]")
        sys.exit(1)

    args = sys.argv[1:]
    verbose = False
    if "--verbose" in args:
        verbose = True
        args.remove("--verbose")
    prompt = " ".join(args)

    messages = [
        types.Content(role = "user", parts = [types.Part(text = prompt)]),
]
    generate_content(client, messages, verbose)




def generate_content(client, messages, verbose):
    response = client.models.generate_content(
    model = 'gemini-2.0-flash-001',
    contents = messages,
    config = types.GenerateContentConfig(
        tools = [available_functions], system_instruction = system_prompt
        ),
    )




    if verbose:
        print(f"User prompt: {messages[-1].parts[0].text if messages and messages[-1].parts else 'N/A'}")
        x = response.usage_metadata.prompt_token_count
        y = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: "+ str(x))
        print(f"Response tokens: "+ str(y))

    if not response.function_calls:
        return response.txt

    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose=verbose)

        try:
            function_response = function_call_result.parts[0].function_response.response
        except (AttributeError, IndexError):
            raise RuntimeError("Function response missing or malformed in returned content.")

        if verbose:
            print(f"-> {function_response}")

    return function_call_result


if __name__ == "__main__":
    main()

