'''
    Given an integer array [nums], return true if any value appears more
    than once in the array, otherwise return false. yuh
'''

# use 'count' method

from typing import List
from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDup = False

        for x in nums:
            if(nums.count(x) > 1):
                isDup = True

        return isDup
    

sol = Solution()

x = [1,2,3,4,3]

print(sol.hasDuplicate(x))
