import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

from google.genai import types


import sys

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

    response = client.models.generate_content(
    model = 'gemini-2.0-flash-001', contents = messages
)
    if verbose:
        print(f"User prompt: {prompt}")
        x = response.usage_metadata.prompt_token_count
        y = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: "+ str(x))
        print(f"Response tokens: "+ str(y))

    print(response.text)


if __name__ == "__main__":
    main()
