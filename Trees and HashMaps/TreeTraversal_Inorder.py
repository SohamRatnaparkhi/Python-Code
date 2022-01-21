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

def in_order(node):
    if (node) is None:
        return []
    else:
        
        return (in_order(node.left) + [(node.key)] + in_order(node.right))

tree = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree2 = parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
tree1 = parse_tuple(tree)
print(in_order(tree2))