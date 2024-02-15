#!/usr/bin/python3
""" Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name developedbyamin """

import sys
import os

def convert_markdown_to_html(input_file, output_file):
    # Check if the Markdown file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Your Markdown to HTML conversion logic goes here
    # For simplicity, let's assume a basic conversion
    with open(input_file, 'r') as f:
        markdown_text = f.read()

    # Your HTML generation logic here
    # ...

    # Save the HTML content to the output file
    with open(output_file, 'w') as f:
        # Write your HTML content to the file
        pass

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) == 1:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)
    if len(sys.arg) == 2:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    # Extract input and output file names
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML
    convert_markdown_to_html(input_file, output_file)

    sys.exit(0)

if __name__ == "__main__":
    main()
