#!/usr/bin/python3
""" Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name developedbyamin """

import sys
import os
import re
import hashlib

# Recognize tags
def toHtml(name,text):
    return "<"+name+">"+text+"</"+name+">\n"

def paragraph(lines):
    text = ""
    for line in lines:
        if(line!=lines[0]):
            text += '<br/>'
        text += '\n\t' + line +'\n'
    return toHtml('p',text)

def heading(line):
    count = line.count('#')
    name = "H"+str(count)
    return toHtml(name,line[count+1:])

def uoList(lines,name):
    text = ""
    for line in lines:
        text += "\t" + toHtml("li",line[2:])
    return toHtml(name,"\n" + text)




# FUNCTIONS TO HELP CONVERT THE MARKDOWN TO HTML
def getLines(lines, char = '', isAlpha = False):
    l = [bold(emphasize(sqBrackets(brackets(lines[0]))))]
    lines.remove(lines[0])
    while(len(lines) != 0):
        line = lines[0]
        if(line == ''):
            break
        if((line[0].isalpha and isAlpha) or line[0] == char):
            lines.remove(line)
            line = bold(emphasize(sqBrackets(brackets(line))))
            l.append(line)
        else:
            break
    return l

def bold(line):
    line = re.sub(r"\*\*", "<b>", line, 1)
    line = re.sub(r"\*\*", "</b>", line, 1)
    return line

def emphasize(line):
    line = re.sub("__","<em>",line,1)
    line = re.sub("__","</em>",line,1)
    return line

def sqBrackets(line):
    first = line.find("[[")
    last = line.find("]]")
    if(first != -1 and last != -1):
        text = line[first+2:last]
        line = line[:first] + str(hashlib.md5(text.encode()).hexdigest()) + line[last+2:]
    return line

def brackets(line):
    first = line.find("((")
    last = line.find("))")
    if(first != -1 and last != -1):
        text = line[first+2:last]
        text = text.replace('c','')
        text = text.replace('c','')
        line = line[:first] + text + line[last+2:]
    return line

def convert_markdown_to_html(input_file, output_file):
    # Your Markdown to HTML conversion logic
    with open(input_file) as IN:
        with open(output_file, 'w') as OUT:
            lines = IN.read().splitlines()
            html = ""

            while(len(lines) != 0):
                line = lines[0]
                if(line == ""):
                    lines.remove(line)
                else:
                    line = bold(emphasize(sqBrackets(brackets(line))))

                    if(line[0] == "#"):
                        html += heading(line)
                        del lines[0]
                    elif(line[0] == "-"):
                        l = getLines(lines,'-')
                        html += uoList(l,"ul")
                    elif(line[0] == "*"):
                        l = getLines(lines,'*')
                        html += uoList(l,"ol")
                    elif(line[0].isalpha):
                        l = getLines(lines, isAlpha = True)
                        html += paragraph(l)
            OUT.write(html)
    exit(0)

def main():
    # Extract input and output file names
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)
    # Check if the number of arguments is correct
    if len(sys.argv) == 1 or len(sys.argv) == 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    # Convert Markdown to HTML
    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)

if __name__ == "__main__":
    main()
