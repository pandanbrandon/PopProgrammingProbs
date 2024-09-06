'''
    Merge sorted array

    LeetCode 88: 
        You are given two integer arrays nums1 and nums2, 
        sorted in non-decreasing order, and two integers m and n, 
        representing the number of elements in nums1 and nums2 respectively.
        Merge nums1 and nums2 into a single array sorted in non-decreasing order.
'''

# idea: swap out zeros from nums2, then sort

class Solution(object):
    def merge(self, nums1, m, nums2, n):
    
        nums1[m:] = nums2

        nums1.sort()


        