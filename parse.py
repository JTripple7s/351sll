
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
            #self.log(f"Matched {token}")
            self.iterate()
        else:
            self.log(f"Expected {expected_type} but got {token}")
            exit(1)

    def parse_one_line(self):
        """Parses a single line of TinyPie code based on the starting token."""
        token = self.get_current_token()
        if not token:
            return ParseNode("Empty")

        if token[0] == "key" and token[1] == "float" or token[1] == "int":
            return self.program()
        elif token[0] == "key" and token[1] == "if" or token[1] == "else":
            return self.if_exp()
        elif token[0] == "key" and token[1] == "print":
            return self.print_exp()
        else:
            self.log(f"Unknown start of line: {token}")
            exit(1)

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
        """Parse: exp -> expression."""
        self.log("Parsing expression")
        node = ParseNode("exp")
        node.add_child(self.expAdv())
        while self.get_current_token() and self.get_current_token()[1] in ["+", "-"]:
            op = self.get_current_token()[1]
            self.match("operator")
            node.add_child(ParseNode(op))
            node.add_child(self.expAdv())
        return node

    def expAdv(self):
        self.log("Parsing expression advanced")
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
        self.log(f"Parsing number, got token: {token}")
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

    def comparison_exp(self):
        """Parse: comparison_exp -> identifier > identifier"""
        self.log("Parsing comparison_exp")
        node = ParseNode("comparison_exp")
        left = self.get_current_token()
        self.match("identifier")
        op = self.get_current_token()
        self.match("operator")  # '>'
        right = self.get_current_token()
        self.match("identifier")

        node.add_child(ParseNode(left[1]))
        node.add_child(ParseNode(op[1]))
        node.add_child(ParseNode(right[1]))

        return node

    def if_exp(self):
        """Parse: if_exp -> if ( comparison_exp ) :"""
        self.log("Parsing if_exp")
        node = ParseNode("if_exp")
        self.match("key")  # Expect 'if'
        self.match("separator")  # Expect '('
        node.add_child(self.comparison_exp())
        self.match("separator")  # Expect ')'
        self.match("separator")  # Expect ':'
        return node

    def print_exp(self):
        """Parse: print_exp -> print ( identifier ) ;"""
        self.log("Parsing print_exp")
        node = ParseNode("print_exp")

        self.match("key")  # 'print'
        self.match("separator")  # '('

        ident = self.get_current_token()
        if ident[0] != "identifier":
            self.log(f"Expected identifier inside print but got {ident}")
            exit(1)
        self.match("identifier")
        node.add_child(ParseNode(ident[1]))

        self.match("separator")  # ')'
        self.match("separator")  # ';'

        return node


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

if __name__ == "__main__":
    print("=== Testing if_exp() ===")
    test_tokens = [
        ("key", "if"),
        ("separator", "("),
        ("identifier", "x"),
        ("operator", ">"),
        ("identifier", "y"),
        ("separator", ")"),
        ("separator", ":")
    ]

    parser = Parser(test_tokens)
    tree = parser.if_exp()
    print(tree)



