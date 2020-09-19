# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        def helper(node1, node2) -> bool:
            if node1 and node2:
                return node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left)
            if not node1 and not node2:
                return True
            return False
        return not root or helper(root.left, root.right)