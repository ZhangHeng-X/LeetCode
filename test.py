class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        dict = {}
        lf = 0
        for rt in range(len(s)):
            if s[rt] in dict and dict[s[rt]] >= lf:
                lf = dict[s[rt]] + 1
            else:
                ans = max(ans, rt - lf + 1)
            dict[s[rt]] = rt
        return ans

a = Solution()
print(a.lengthOfLongestSubstring('aaaabcbcbcadea'))