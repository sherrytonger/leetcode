__author__ = 'Sherry'
# Given an array of integers and an integer k, find out whether there there are two distinct
# indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        num_dict = dict()
        for i in range(len(nums)):

            if nums[i] in num_dict:
                if i - num_dict[nums[i]] <= k:  return True
                else:
                    num_dict[nums[i]] = i
            else:
                num_dict[nums[i]] = i
        return False


sol = Solution()
print sol.containsNearbyDuplicate([-1,-1],1)