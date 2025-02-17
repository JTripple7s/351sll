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
    (r"\"\s*[A-Za-z]*\s*\"", "string lit"),
]


testString = "int A1 = 5;"
results = []  # list of <token, type> strings


def main():
    cutOneLineTokens(testString)


def cutOneLineTokens(oneLineString):
    i = 0;  #index
    while i != len(oneLineString):  #loop through length of string, compare every char with match obj
        tokenMatched = False    #if string gets through and lexer doesn't match anything for some reason we iterate
                                #if this happens then the regex expressions are wrong, shouldn't happen
        for regex in regexes:   #loop through all possible regex expression matches
            match = re.match(regex[0], oneLineString)
            type = regex[1]
            if match:  # if we matched something, add it to the results list
                results.append("<" + type + ">, <" + match.group(0) + ">")

                # we have to cut out the token we just matched
                firstHalf = oneLineString[0: match.start()]
                secondHalf = oneLineString[match.end():]
                oneLineString = firstHalf + secondHalf
                oneLineString = oneLineString.lstrip()  # strip leading whitespaces

                #i = len(oneLineString) - 1  #lets it const loop until no more chars in string
                tokenMatched = True #lets our check know a token was Matched and the we already iterated
                break

        if not tokenMatched:
            i += 1

    print(results)


if __name__ == "__main__":
    main()
