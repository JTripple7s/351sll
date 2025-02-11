import re

testString = ("int A1=5")

def main():
    cutOneLineTokens(testString)

def cutOneLineTokens(oneLineString):
    print(oneLineString)

if __name__ == '__main__':
    main()