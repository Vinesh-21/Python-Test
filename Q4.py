class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def preorder(self, node):
        
        if node is None:
            # print("""|\n|-> None
            #       \n""", end=" ")
            return
        
        print(node.data, end=" -> ")
        # print("(left)")
        self.preorder(node.left)
        # print("(right)")
        self.preorder(node.right)
        
        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

binaryTree = BinaryTree(root)
binaryTree.preorder(binaryTree.root)
