import re


class Token:

    def __init__(self, match: re.Match, type: str):
        self.match = match
        self.type = type


testString = "int A1=5 if if "


def main():
    cutOneLineTokens(testString)



def cutOneLineTokens(oneLineString):
    #create list of all possible tokens
    typesAndTokens = []
    tokens = oneLineString.split()

    for token in tokens:
        # match keywords
        ifMatch = re.search(
            r"(?<!\S)if(?!\S)",
            oneLineString,
        )
        if ifMatch:
            typesAndTokens.append("<" + "key," + ifMatch.group(0) + ">" )

        elseMatch = re.search(
            r"(?<!\S)else(?!\S)",
            oneLineString,
        )
        if elseMatch:
            typesAndTokens.append("<" + "key," + elseMatch.group(0) + ">")

        intMatch = re.search(
            r"(?<!\S)int(?!\S)",
            oneLineString,
        )
        if intMatch:
            typesAndTokens.append("<" + "key," + intMatch.group(0) + ">")

        floatMatch = re.search(
            r"(?<!\S)float(?!\S)",
            oneLineString,
        )
        if intMatch:
            typesAndTokens.append("<" + "key," + intMatch.group(0) + ">")


        # match operators
        equalsMatch = re.search(
            r"=",
            oneLineString,
        )
        equalsToken = Token(equalsMatch, "operator")
        tokens.append(equalsToken)

        plusMatch = re.search(
            r"\+",
            oneLineString,
        )
        plusToken = Token(plusMatch, "operator")
        tokens.append(plusToken)

        greaterThanMatch = re.search(
            r">",
            oneLineString,
        )
        greaterThanToken = Token(greaterThanMatch, "operator")
        tokens.append(greaterThanToken)

        asteriskMatch = re.search(
            r"\*",
            oneLineString,
        )
        asteriskToken = Token(asteriskMatch, "operator")
        tokens.append(asteriskToken)

        # separators
        leftParenthesisMatch = re.search(
            r"\(",
            oneLineString,
        )
        leftParenthesisToken = Token(leftParenthesisMatch, "separator")
        tokens.append(leftParenthesisToken)

        rightParenthesisMatch = re.search(
            r"\)",
            oneLineString,
        )
        rightParenthesisToken = Token(rightParenthesisMatch, "separator")
        tokens.append(rightParenthesisToken)

        colonMatch = re.search(
            r":",
            oneLineString,
        )
        colonToken = Token(colonMatch, "separator")
        tokens.append(colonToken)

        quotationMatch = re.search(
            r"\"",
            oneLineString,
        )
        quotationToken = Token(quotationMatch, "separator")
        tokens.append(quotationToken)

        semicolonMatch = re.search(
            r"(?<!\S);(?!\S)",
            oneLineString,
        )
        semicolonToken = Token(semicolonMatch, "separator")
        tokens.append(semicolonToken)

        # identifiers (exclude keywords)
        identifierMatch = re.search(r"(?<!\S)(?!\b(?:int|float|if|else)\b)[a-zA-Z][a-zA-Z0-9]*", oneLineString)
        identifierToken = Token(identifierMatch, "identifier")
        tokens.append(identifierToken)

        # int literals
        intLitMatch = re.search(r"(?<!\S)[0-9]+(?!\S)", oneLineString)
        intLitToken = Token(intLitMatch, "integer literal")
        tokens.append(intLitToken)

        # float match
        floatLitMatch = re.search(r"(?<!\S)[0-9]*\.[0-9]+(?!\S)", oneLineString)
        floatLitToken = Token(floatLitMatch, "float")
        tokens.append(floatLitToken)

        # string match
        stringMatch = re.search(r"\"\s*[A-Za-z]*\s*\"", oneLineString)
        stringToken = Token(stringMatch, "float")
        tokens.append(stringToken)

    print("Output <type, token> list: [", end="")
    for token in tokens:
        if token.match:
            print("<" + token.type + "," + token.match.group(0) + ">,", end="")
    
    print("]")

def getStrFromMatch(stringToMatch: str, regexPattern: str, type: str):
    safePattern = re.escape(regexPattern)
    match = re.match(safePattern, stringToMatch)
    if match:
        return "<" + type + "," + match.group(0) + ">" 
    else:
        return ""

if __name__ == "__main__":
    main()
