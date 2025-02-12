import re


class Token:
    type = ""
    token = ""


testString = "int A1=5 if "


def main():
    cutOneLineTokens(testString)


def cutOneLineTokens(oneLineString):
    ifMatch = re.search(
        r"(?<!\S)if(?!\S)",
        oneLineString,
    )
    print(ifMatch)


if __name__ == "__main__":
    main()
