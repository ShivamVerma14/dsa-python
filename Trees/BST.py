class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(node: Node) -> None:
    if not node:
        return
    
    inorder_traversal(node.left)
    print(node.data, end=" ")
    inorder_traversal(node.right)

def preorder_traversal(node: Node) -> None:
    if not node:
        return
    
    print(node.data, end=" ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def postorder_traversal(node: Node) -> None:
    if not node:
        return
    
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data, end=" ")

def insert(node: Node, data: int) -> Node:
    if not node:
        return Node(data)
    
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node

def search(node: Node, key: int) -> Node:
    if not node:
        return None
    
    if node.data == key:
        return node
    elif key < node.data:
        return search(node.left, key)
    else:
        return search(node.right, key)
    
def min_value_node(node: Node) -> Node:
    curr = node
    while curr.left:
        curr = curr.left
    return curr

def delete(node: Node, data: int) -> Node:
    if not node:
        return None
    
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        if not node.left:
            temp = node.right
            del node
            return temp
        elif not node.right:
            temp = node.left
            del node
            return temp
        else:
            node.data = min_value_node(node.right).data
            node.right = delete(node.right, node.data)
    
    return node

def main() -> None:
    head: Node = None
    
    values = [12, 4, 26, 13, 2, 7, 30]
    for value in values:
        head = insert(head, value)

    print("Preorder Traversal: ", end="")
    preorder_traversal(head)
    print("\nInorder Traversal: ", end="")
    inorder_traversal(head)
    print("\nPostorder Traversal: ", end="")
    postorder_traversal(head)
    print()

    if search(head, 30):
        print("Yes, 30 is present in the BST.")
    else:
        print("No, 30 is not present in the BST.")

    print("Deleting 4 from the tree...")
    head = delete(head, 4)

    print("Preorder Traversal: ", end="")
    preorder_traversal(head)
    print("\nInorder Traversal: ", end="")
    inorder_traversal(head)
    print("\nPostorder Traversal: ", end="")
    postorder_traversal(head)
    print()

if __name__ == "__main__":
    main()