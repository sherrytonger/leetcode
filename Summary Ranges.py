__author__ = 'Sherry'

# Given a sorted integer array without duplicates, return the summary of its ranges.

# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        ans = []
        start = 0
        for n in range(1, len(nums)):
            if nums[n] != nums[n - 1] + 1:
                ans.append('{}->{}'.format(nums[start], nums[n - 1]))
                start = n
        nums and ans.append('{}->{}'.format(nums[start], nums[-1]))
        return [i.replace('->' + i[:len(i) // 2 - 1], '') for i in ans]





sol = Solution()
print sol.summaryRanges([-4,0,1,2,4,5,7,9,11,12,13,14,20])