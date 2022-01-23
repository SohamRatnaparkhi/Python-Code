class BST:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def is_bst(node):
    if node is None:
        return True, None      # because a none node is always balanced and has height None

    left_bal, left_height = is_bst(node.left)
    right_bal, right_height = is_bst(node.right)

    balance = None
    if (left_bal and right_bal) and (abs(left_height - right_height) <= 1):
        balance = True
    
    height = max(left_height, right_height) + 1

    return balance, height

def make_balanced_bst(data, s = 0, e = None, parent = None):
    if e is None: e = len(data) - 1
    if s > e: return None

    mid = (s + e) // 2
    key = data[mid]
    value = None
    node = BST(key, value)
    parent = node.parent

    node.left = make_balanced_bst(data, s, mid - 1, parent)
    node.right = make_balanced_bst(data, mid + 1, e, parent)

    return node

def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        display_keys(self.left,space, level+1)

def find(node, key):
    if node is None:
        return None
    if node.key is key:
        return node
    if node.key > key:
        return find(node.left, key)
    else:
        return find(node.right, key)

def update(node, key, new_key):
    target = find(node, key)
    if target is not None:
        target.key = new_key


def input_details():
    data = input("Enter the data you want in Binary Search tree - ").strip().split()
    #data.sort()
    tree = make_balanced_bst(data)
    # if data is not sorted then do inorder traversal on unbalanced tree and then pass its result in make_balanced_tree() func
    display_keys(tree)

    f =  find(tree, input("Enter element you want to check - "))
    if f is None:
        print("Not found")
    else:
        print(f"{f.key} found")

    u = input("Element to update - ")
    nu = input("New value - ")
    update(tree, u, nu)
    display_keys(tree)
    
input_details()