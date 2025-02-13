import re


class Token:
    type = ""
    token = ""


testString = "int A1=5 if if "


def main():
    cutOneLineTokens(testString)



def cutOneLineTokens(oneLineString):
    # match keywords
    ifMatch = re.search(
        r"(?<!\S)if(?!\S)",
        oneLineString,
    )
    print(ifMatch.group(0))

    elseMatch = re.search(
        r"(?<!\S)else(?!\S)",
        oneLineString,
    )
    intMatch = re.search(
        r"(?<!\S)int(?!\S)",
        oneLineString,
    )
    floatMatch = re.search(
        r"(?<!\S)float(?!\S)",
        oneLineString,
    )

    # match operators
    equalsMatch = re.search(
        r"=",
        oneLineString,
    )
    plusMatch = re.search(
        r"\+",
        oneLineString,
    )
    greaterThanMatch = re.search(
        r">",
        oneLineString,
    )
    asteriskMatch = re.search(
        r"\*",
        oneLineString,
    )

    # separators
    leftParenthesisMatch = re.search(
        r"\(",
        oneLineString,
    )
    rightParenthesisMatch = re.search(
        r"\)",
        oneLineString,
    )
    colonMatch = re.search(
        r":",
        oneLineString,
    )
    quotationMatch = re.search(
        r"\"",
        oneLineString,
    )
    semicolonMatch = re.search(
        r"(?<!\S);(?!\S)",
        oneLineString,
    )

    # identifiers
    identifierMatch = re.search(r"(?<!\S)[a-zA-Z][a-zA-Z0-9]*", oneLineString)

    # int literals
    intLitMatch = re.search(r"(?<!\S)[0-9]+(?!\S)", oneLineString)

    # float match
    floatMatch = re.search(r"(?<!\S)[0-9]*\.[0-9]+(?!\S)", oneLineString)

    # string match
    stringMatch = re.search(r"\"\s*[A-Za-z]*\s*\"", oneLineString)


if __name__ == "__main__":
    main()
