from collections import deque
class Node:
    """Represents a single node in a binary tree"""
    def __init__(self, data):
        self.data = data    # Value stored in the node
        

class BinaryTree:
    """Represents a binary tree"""
    def __init__(self, root_data):
        self.root = Node(root_data)
        self.left=None
        self.right=None

    def print_tree(self, traversal_type="inorder"):
        """Print the tree using different traversal methods"""
        if traversal_type == "preorder":
            return self._preorder_traversal(self.root, "")
        elif traversal_type == "inorder":
            return self._inorder_traversal(self.root, "")
        elif traversal_type == "postorder":
            return self._postorder_traversal(self.root, "")
        else:
            return "Invalid traversal type"

    def _preorder_traversal(self, node, traversal):
        """Root -> Left -> Right"""
        if node:
            traversal += str(node.data) + " "
            traversal = self._preorder_traversal(node.left, traversal)
            traversal = self._preorder_traversal(node.right, traversal)
        return traversal

    def _inorder_traversal(self, node, traversal):
        
        """Left -> Root -> Right"""
        if node:
            traversal = self._inorder_traversal(node.left, traversal)
            traversal += str(node.data) + " "
            traversal = self._inorder_traversal(node.right, traversal)
        return traversal

    def _postorder_traversal(self, node, traversal):
        """Left -> Right -> Root"""
        if node:
            traversal = self._postorder_traversal(node.left, traversal)
            traversal = self._postorder_traversal(node.right, traversal)
            traversal += str(node.data) + " "
        return traversal
    
    def invertBinarytree(self,root):
        if root is None:
            return None
        left= self.invertBinarytree(root.left)
        right=self.invertBinarytree(root.right)
        root.left,root.right=root.right,root.left
        return root

    def maxWidth(self):
        queue=deque()
        max_wid=-2
        queue.append(self.root)
        while queue:
            size=len(queue)
            max_wid=max(max_wid,size)
            for i in range(size):
                node=queue.pop()
                if node.left is not None:queue.append(node.left)
                if node.right is not None:queue.append(node.right)
        return max_wid       

        