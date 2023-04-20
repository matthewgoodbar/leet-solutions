# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. 
# nums2 has a length of n.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Copy = nums1[:m]

        mIdx = nIdx = i = 0
        while mIdx < m and nIdx < n:
            if nums1Copy[mIdx] < nums2[nIdx]:
                nums1[i] = nums1Copy[mIdx]
                i += 1
                mIdx += 1
            else:
                nums1[i] = nums2[nIdx]
                i += 1
                nIdx += 1
        
        if nIdx < n:
            for el in nums2[nIdx:n]:
                nums1[i] = el
                i += 1
        else:
            for el in nums1Copy[mIdx:m]:
                nums1[i] = el
                i += 1
        
        return nums1