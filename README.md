# PyTestGen 

## What is this?
An AI-powered CLI tool that automatically generates 
unittest test cases for any Python file using a 
locally running LLaMA model via Ollama.

No API keys. No cloud. Runs 100% on your machine.

## Why?
Writing test cases manually is time-consuming.
PyTestGen reads your Python file and generates
positive, negative, and edge case tests instantly.

## Requirements
- Python 3.12+
- Ollama installed and running locally
- LLaMA3.2 model pulled

## Installation
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python main.py --file calculator.py
```

## Example Output
Given a `calculator.py` with `multiply` and `divide` 
functions, PyTestGen generates:

- test_multiply_positive_numbers
- test_multiply_negative_numbers  
- test_divide_by_zero (edge case)
- And more...

Generated tests are saved automatically to 
`test_calculator.py`

## Tech Stack
Python | LLaMA 3.2 | Ollama | argparse | Rich