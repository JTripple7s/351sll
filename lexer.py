import re
from parse import *

# list of tuples; regex and the type it is
regexes = [
    # keys
    (r"\"\s*[A-Za-z]*\s*\"", "string lit"),
    (r"(?<!\S)if(?!\S)", "key"),
    (r"(?<!\S)else(?!\S)", "key"),
    (r"(?<!\S)int(?!\S)", "key"),
    (r"(?<!\S)float(?!\S)", "key"),
    # operators
    (r"\+", "operator"),
    (r">", "operator"),
    (r"\*", "operator"),
    (r"=", "operator"),
    # separators
    (r"\)", "separator"),
    (r"\(", "separator"),
    (r":", "separator"),
    (r"\"", "separator"),
    (r";", "separator"),

    (r"(?<!\S)(?!\b(?:int|float|if|else)\b)[a-zA-Z][a-zA-Z0-9]*", "identifier"),
    (r"(?<!\S)[0-9]+(?!\w|\.\d)", "int lit"),
    (r"(?<!\S)[0-9]*\.[0-9]+(?!\w)", "float"),
]

originalString = "int A1=5" #original test string
testString = "\"TinyPie \", ,,\"Otherpie\" \"" #this test shows that we can have multiple string lit as well as a quote mark and it will all be cataloged
results = []  # list of <token, type> strings


def main():
    cutOneLineTokens(testString)


def cutOneLineTokens(oneLineString):
    tokens = []  # List of (type, value) tuples
    while oneLineString:
        tokenMatched = False
        for regex in regexes:
            match = re.match(regex[0], oneLineString)
            if match:
                token_type = regex[1]
                token_value = match.group(0)
                tokens.append((token_type, token_value))  # Store tuple format
                # Remove matched token from input
                oneLineString = oneLineString[match.end():].lstrip()
                tokenMatched = True
                break

        if not tokenMatched:
            raise SyntaxError(f"Unexpected character: {oneLineString[0]}")

    return tokens


if __name__ == "__main__":
    input_string = "float myVar = 5 * 4.3 + 2.1;"
    print("starting lex of: float myVar = 5 * 4.3 + 2.1;")
    tokens = cutOneLineTokens(input_string)

    print("\nTokens:", tokens)

    print("\nStarting parse")
    parser = Parser(tokens)
    parser.parse()
    print("\nParsing completed successfully!")

