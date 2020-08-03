class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i = N-1
        for i in range(N-1, -1, -1):
            if i == 0:
                nums.sort()
                return
            if nums[i] > nums[i-1]:
                break
        nums[i:] = sorted(nums[i:])
        for j in range(i, N):
            if nums[j] > nums[i-1]:
                tmp = nums[j]
                nums[j] = nums[i-1]
                nums[i-1] = tmp
                return
        