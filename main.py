import sys
from pointer import brainfuck

def readFile(path):
    file = open(path, "r")
    content = file.read()
    file.close()
    return content

def main(args):
    path = args[1]
    file_content = readFile(path)
    brainfuck(file_content)

main(sys.argv)