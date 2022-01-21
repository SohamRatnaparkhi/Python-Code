class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
def parse_tuple(data):
    node = TreeNode(data)
    if type(data) is tuple and len(data) == 3:
        node.key = data[1]
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif type(data) is None:
        node = None
    else:
        node = TreeNode(data)
    return node

def pre_order(node):  # mid -> left -> right
    if node == None:
        return []
    else:
        mid = [node.key]
        go_left = pre_order(node.left)
        go_right = pre_order(node.right)
        return (mid + go_left + go_right) 

tree = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree2 = parse_tuple(tree)
print(pre_order(tree2))