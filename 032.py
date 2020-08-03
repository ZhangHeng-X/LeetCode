class Solution:
    def longestValidParentheses(self, s):
        unpairs = []
        for i in range(len(s)):
            if s[i] == ')' and len(unpairs) > 0 and s[unpairs[-1]] == '(':
                unpairs.pop()
            else:
                unpairs.append(i)
        if not unpairs:
           return len(s)
        ans = unpairs[0]
        for i in range(1,len(unpairs)):
            ans = max(ans, unpairs[i] - unpairs[i-1] - 1)
        ans = max(ans, len(s) - unpairs[-1] - 1)
        return ans