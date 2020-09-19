class Solution:
    def isSameTree(self, p, q) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if p and q:
                if p.val == q.val:
                    stack.append((p.left, q.left))
                    stack.append((p.right, q.right))
                else:
                    return False
            elif not p and not q:
                pass
            else:
                return False
        return True