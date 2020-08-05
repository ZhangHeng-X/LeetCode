class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        
        i = N-1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1

        if i > 0:
            j = N - 1
            while j >= i:
                if nums[j] > nums[i-1]:
                    nums[i-1], nums[j] = nums[j], nums[i-1]
                    break
                j -= 1
        
        j = N - 1
        while j > i:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1; i += 1
        