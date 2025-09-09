class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def getHeight(self, node: TreeNode) -> int:
        if node is None:
            return -1   
        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)
        return 1 + max(left_height, right_height)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

binaryTree = BinaryTree(root)
print("Tree Height -> ", binaryTree.getHeight(binaryTree.root))
