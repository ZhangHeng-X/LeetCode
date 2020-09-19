# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        ans = 0
        stk = [(root, 1)]
        while stk:
            node, dept = stk.pop()
            if node:
                ans = max(ans, dept)
                stk.append((node.left, dept + 1))
                stk.append((node.right, dept + 1))
        return ans
        