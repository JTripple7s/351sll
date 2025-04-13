tokens = []
position = 0

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.output =[]

    def log(self, message):
        print(message)
        self.output.append(message)

    def __str__(self):
        return '\n'.join(self.output)

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
            self.log(f"Matched {token}")
            self.iterate()
        else:
            self.log(f"Expected {expected_type} but got {token}")
            exit(1)

    def parse(self):
        return self.program()

    def program(self):
        node = ParseNode("program")
        node.add_child(self.type())
        node.add_child(self.id())
        self.match("operator")  # Expect '='
        node.add_child(ParseNode("="))
        node.add_child(self.exp())
        self.match("separator")  # Expect ';'
        node.add_child(ParseNode(";"))
        return node

    def type(self):
        """Parse: type -> 'float'."""
        self.log("Parsing type")
        self.match("key")  # Expecting "float"
        return ParseNode("type")

    def id(self):
        """Parse: id -> identifier."""
        self.log("Parsing identifier")
        self.match("identifier")
        return ParseNode("id")

    def exp(self):
        node = ParseNode("exp")
        node.add_child(self.expAdv())
        while self.get_current_token() and self.get_current_token()[1] in ["+", "-"]:
            op = self.get_current_token()[1]
            self.match("operator")
            node.add_child(ParseNode(op))
            node.add_child(self.expAdv())
        return node

    def expAdv(self):
        node = ParseNode("expAdv")
        node.add_child(self.num())
        while self.get_current_token() and self.get_current_token()[1] in ["*", "/"]:
            op = self.get_current_token()[1]
            self.match("operator")
            node.add_child(ParseNode(op))
            node.add_child(self.num())
        return node

    def num(self):
        token = self.get_current_token()
        if token[0] in ["int lit", "float", "identifier"]:
            self.match(token[0])
            return ParseNode(token[1])
        elif token[0] == "separator" and token[1] == "(":
            self.match("separator")
            node = self.exp()
            self.match("separator")  # Should be ')'
            return node
        else:
            print(f"Unexpected token {token}")
            exit(1)

class ParseNode:
    def __init__(self, label):
        self.label = label
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self, level=0):
        ret = "  " * level + self.label + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
