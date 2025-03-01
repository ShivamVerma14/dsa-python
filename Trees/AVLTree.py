class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def update_height(self, node):
        if not node:
            return
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def right_rotate(self, y):
        if not y or not y.left:
            return y
        
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)
        return x
    
    def left_rotate(self, x):
        if not x or not x.right:
            return x
        
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)
        return y
    
    def insert(self, root, data):
        if not root:
            return Node(data)
        
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        else:
            return root
        
        self.update_height(root)
        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def insert_data(self, data):
        self.root = self.insert(self.root, data)

    def min_value_node(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr
    
    def delete(self, root, data):
        if not root:
            return root
        
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if not root.left:
                temp = root.right
                del root
                return temp
            elif not root.right:
                temp = root.left
                del root
                return temp
            
            temp = self.min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        if not root:
            return root
        
        self.update_height(root)
        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and self.get_balance(root.right) >= 0:
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and self.get_balance(root.right) >= 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
        
    def delete_data(self, data):
        self.root = self.delete(self.root, data)

    def inorder(self, node, res):
        if not node:
            return
        
        self.inorder(node.left, res)
        res.append(node.data)
        self.inorder(node.right, res)

    def inorder_traversal(self):
        res = []
        self.inorder(self.root, res)
        return res
    
    def print_tree(self):
        def display(root, level=0, prefix="Root: "):
            if not root:
                return []
            
            result = []
            result.append(" " * level + prefix + str(root.data) + " (h=" + str(root.height) + ")")
            
            if root.left or root.right:
                if root.left:
                    result.extend(display(root.left, level + 4, "L--- "))
                else:
                    result.append(" " * (level + 4) + "L--- None")
                    
                if root.right:
                    result.extend(display(root.right, level + 4, "R--- "))
                else:
                    result.append(" " * (level + 4) + "R--- None")
            
            return result
        
        return "\n".join(display(self.root))
    
def main():
    avl = AVLTree()

    values = [10, 20, 30, 40, 50, 60]
    for value in values:
        avl.insert_data(value)

    print("AVL Tree after insertion:")
    print(avl.print_tree())

    print("\nInorder Traversal:", avl.inorder_traversal())

    avl.delete_data(30)
    print("\nAVL Tree after deleting 30:")
    print(avl.print_tree())

if __name__ == "__main__":
    main()