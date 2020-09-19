# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left and right:
                if  left.val != right.val:
                    return False
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            elif not left and not right:
                pass
            else:
                return False
        return True            