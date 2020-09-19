class Solution:
    def largestRectangleArea(self, heights) -> int:
        ans = 0
        stack = []
        i = 0
        while i < len(heights):
            if not stack or heights[i]>=heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                ans = max(ans, heights[i]*(i - stack[-1] + 1))
                stack.pop(-1)



print(Solution().largestRectangleArea([3,2,1]))

