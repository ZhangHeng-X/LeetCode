class Solution:
    def lengthOfLIS(self, nums):
        dp = []

        for i in range(len(nums)):
            l, r = 0, len(dp)
            while l < r:
                m = l + (r-l)//2
                if nums[i] > dp[m]:
                    l = m + 1
                elif nums[i] < dp[m]:
                    r = m
                else:
                    l, r = m, m
                    break

            if l == len(dp):
                dp.append(nums[i])
            else:
                dp[l] = nums[i]

        return len(dp)