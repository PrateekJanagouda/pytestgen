import argparse

import requests
import json


def generate_tests(function_code:str) -> str:
    prompt = f"""
    You are Python testing expert.
    Generate the testcases for the this function:
    {function_code}
    Return only the test code ,nothing else.
    """


    response = requests.post(
        "http://localhost:11434/api/generate",
        json = {
            "model":"llama3.2:latest",
            "prompt": prompt,
            "stream":False
        }
    )

    raw = response.text.strip()
    last_line = raw.split("\n")[-1]
    result = json.loads(last_line)
    return result["response"].replace("```python", "").replace("```", "").strip()

# sample_function = """
# def add(a, b):
#     return a + b
# """

def read_file(filepath: str) -> str:
    with open(filepath, "r") as f:
        return f.read()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate unit tests for the Python file using LLAMA"
    )
    parser.add_argument("--file",required=True,help="Path to your Python file")
    args = parser.parse_args()

    print(f"Reading file {args.file}")
    code  = read_file(args.file)

    print("Generating the file")
    tests = generate_tests(code)

    output_file = "test_" + args.file
    with open(output_file, "w") as f:
        f.write(tests)

    print(f"Tests saved to {output_file}")
