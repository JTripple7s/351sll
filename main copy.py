import re

regexes = [
# keys
r"(?<!\S)if(?!\S)",
r"(?<!\S)else(?!\S)",
r"(?<!\S)int(?!\S)",
r"(?<!\S)float(?!\S)",
# operators
r"=",
r"\+",
r">",
r"\*",
# separators 
r"\)",
r"\(",
r":",
r"\""
r";",
r"(?<!\S)(?!\b(?:int|float|if|else)\b)[a-zA-Z][a-zA-Z0-9]*", # identifier 
r"(?<!\S)[0-9]+(?!\S)", # int lit
r"(?<!\S)[0-9]*\.[0-9]+(?!\S)", # double
r"\"\s*[A-Za-z]*\s*\"", # string lit
]


testString = "int A1=5;"


def main():
    cutOneLineTokens(testString)



def cutOneLineTokens(oneLineString):
    print(oneLineString)
    

if __name__ == "__main__":
    main()
