class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def find(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        left = self.find(node.left, value)
        if left:
            return left
        return self.find(node.right, value)

    def insert(self, parent_value, new_value, direction):
        parent = self.find(self.root, parent_value)
        if not parent:
            print(f"Parent node '{parent_value}' not found.")
            return
        new_node = Node(new_value)
        if direction == 'l':
            if parent.left is None:
                parent.left = new_node
            else:
                print("Left child already exists.")
        elif direction == 'r':
            if parent.right is None:
                parent.right = new_node
            else:
                print("Right child already exists.")
        else:
            print("Invalid direction. Use 'l' or 'r'.")

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

# Main Program
if __name__ == "__main__":
    root_val = input("Enter root node value: ")
    tree = BinaryTree(root_val)

    while True:
        print("\nAdd a node (or type 'done' to finish):")
        parent = input("Enter parent node value: ")
        if parent.lower() == 'done':
            break
        child = input("Enter new node value: ")
        direction = input("Left or Right? (l/r): ").lower()
        tree.insert(parent, child, direction)

    print("\nInorder Traversal:")
    tree.inorder(tree.root)

    print("\nPreorder Traversal:")
    tree.preorder(tree.root)

    print("\nPostorder Traversal:")
    tree.postorder(tree.root)
