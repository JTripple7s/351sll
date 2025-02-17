import re

# list of tuples; regex and the type it is
regexes = [
    # keys
    (r"(?<!\S)if(?!\S)", "key"),
    (r"(?<!\S)else(?!\S)", "key"),
    (r"(?<!\S)int(?!\S)", "key"),
    (r"(?<!\S)float(?!\S)", "key"),
    # operators
    (r"\+", "operator"),
    (r">", "operator"),
    (r"\*", "operator"),
    # separators
    (r"\)", "separator"),
    (r"\(", "separator"),
    (r":", "separator"),
    (r"\"" r";", "separator"),
    (r"(?<!\S)(?!\b(?:int|float|if|else)\b)[a-zA-Z][a-zA-Z0-9]*", "identifier"),
    (r"(?<!\S)[0-9]+(?!\S)", "int lit"),
    (r"(?<!\S)[0-9]*\.[0-9]+(?!\S)", "float"),
    (r"\"\s*[A-Za-z]*\s*\"", "string lit"),
    (r"=", "operator"),
]


testString = "int A1 = 5;"
results = []  # list of <token, type> strings


def main():
    cutOneLineTokens(testString)


def cutOneLineTokens(oneLineString):
    for regex in regexes:
        match = re.match(regex[0], oneLineString)
        if match:  # if we matched something, add it to the results list
            # main issues: how do we determine type? also, what if there are multiple matches of the same type?
            results.append("<" + match.group(0) + ">") 

            # we have to cut out the token we just matched
            firstHalf = oneLineString[0 : match.start()] 
            secondHalf = oneLineString[match.end() :]
            oneLineString = firstHalf + secondHalf
            oneLineString = oneLineString.lstrip() # strip leading whitespaces 

    print(results)


if __name__ == "__main__":
    main()
