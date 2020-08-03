class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        lf = 0
        rt = m
        while lf <= rt:
            i = (lf + rt) // 2
            j = (m + n) //2 - i
            if i < m and j > 0 and nums2[j-1] > nums1[i]:
                lf = i + 1
                continue
            if j < n and i > 0 and nums1[i-1] > nums2[j]:
                rt = i - 1
                continue
            break
        ans = 0
        if i == m:
            ans += nums2[j]
        elif j == n:
            ans += nums1[i]
        elif nums1[i] < nums2[j]:
            ans += nums1[i]
        else:
            ans += nums2[j]
        if (m + n) % 2 == 1:
            return float(ans)

        if i == 0:
            ans += nums2[j-1]
        elif j == 0:
            ans += nums1[i-1]
        elif nums1[i-1] > nums2[j-1]:
            ans += nums1[i-1]
        else:
            ans += nums2[j-1]
        return float(ans)/2




nums1 = [1, 3, 5, 7, 9]
nums2 = [ 2, 4, 6, 8, 10, 12, 12]
print(Solution().findMedianSortedArrays(nums1, nums2))


