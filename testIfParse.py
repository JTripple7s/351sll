from idlelib.tree import TreeNode

tokens = []  # this will hold the tokens for a line
position = 0  # current index in tokens list

def match(expected):
    global position
    if position < len(tokens) and tokens[position] == expected:
        position += 1
    else:
        raise SyntaxError(f"Expected '{expected}' but found '{tokens[position]}'")

def identifier():
    global position
    if position < len(tokens) and tokens[position].isidentifier():
        node = TreeNode(tokens[position])
        position += 1
        return node
    else:
        raise SyntaxError("Expected identifier")

def comparison_exp():
    left = identifier()
    match('>')
    right = identifier()
    parent = TreeNode('>')
    parent.add_child(left)
    parent.add_child(right)
    return parent

def if_exp():
    match('if')
    match('(')
    comp_node = comparison_exp()
    match(')')
    match(':')
    parent = TreeNode('if')
    parent.add_child(comp_node)
    return parent
