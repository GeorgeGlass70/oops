import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from call_function import available_functions


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


    system_prompt = system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    response = client.models.generate_content(
    model = 'gemini-2.0-flash-001',
    contents = messages,
    config = types.GenerateContentConfig(
        tools = [available_functions], system_instruction = system_prompt
        ),
    )




    if verbose:
        print(f"User prompt: {prompt}")
        x = response.usage_metadata.prompt_token_count
        y = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: "+ str(x))
        print(f"Response tokens: "+ str(y))

    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(response.text)
    


if __name__ == "__main__":
    main()

