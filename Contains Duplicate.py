__author__ = 'Sherry'
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if len(nums) <= 1: return False
        num_dict = dict()
        for i in nums:
            if i in num_dict: return True
            else:
                num_dict[i] = 1
        return False

sol = Solution()
print sol.containsDuplicate([])
print sol.containsDuplicate([1,2,3,4,5])
print sol.containsDuplicate([1,1,3,4,5])