class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def get_current_token(self):
        """Returns the current token or None if end of tokens."""
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None

    def iterate(self):
        """Move to the next token."""
        self.current_token_index += 1

    def match(self, expected_type):
        """Checks if current token matches the expected type and advances."""
        token = self.get_current_token()
        if token and token[0] == expected_type:
            print(f"Matched {token}")
            self.iterate()
        else:
            print(f"Expected {expected_type} but got {token}")
            exit(1)

    def parse(self):
        """Parse the entire program."""
        self.program()

    def program(self):
        """Parse: type id = exp ;"""
        print("\nParsing program")
        self.type()
        self.id()
        self.match("operator")  # Expecting '='
        self.exp()
        self.match("separator")  # Expecting ';'

    def type(self):
        """Parse: type -> 'float'."""
        print("Parsing type")
        self.match("key")  # Expecting "float"

    def id(self):
        """Parse: id -> identifier."""
        print("Parsing identifier")
        self.match("identifier")

    def exp(self):
        """Parse: add and sub parse after expAdv"""
        print("Parsing expression")
        self.expAdv() #order of operations

        # Handle + and - operators
        while self.get_current_token() and self.get_current_token()[0] == "operator" and self.get_current_token()[1] in ["+", "-"]:
            self.match("operator")
            self.expAdv()

    def expAdv(self):
        """Parse: multi and div parse"""
        print("Parsing expAdv")
        self.num()

        # Handle * and / operators
        while self.get_current_token() and self.get_current_token()[0] == "operator" and self.get_current_token()[1] in ["*", "/"]:
            self.match("operator")
            self.num()

    def num(self):
        """Parse: num -> int | float | id | ( expr )."""
        print("Parsing number")
        token = self.get_current_token()

        if token[0] in ["int lit", "float", "identifier"]:
            self.match(token[0])
        elif token[0] == "separator" and token[1] == "(":
            self.match("separator")
            self.exp()
            self.match("separator")
        else:
            print(f"Unexpected token {token}")
            exit(1)
