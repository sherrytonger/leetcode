__author__ = 'Sherry'

# Given an array of integers, find two numbers such that they add up to a specific
# target number.


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num1 = sorted(num)
        i = 0
        j = len(num1)-1
        while i <len(num1)-1:
            if num1[i] +num1[j] == target:
                if num1[i] !=num1[j]:
                    index1 = num.index(num1[i])+1
                    index2 = num.index(num1[j])+1
                    return (index1,index2) if index1 < index2 else (index2,index1)
                else:
                    index1 = num.index(num1[i])+1
                    index2 = num[i+1:].index(num1[j])+2+i
                    return (index1,index2) if index1 < index2 else (index2,index1)
            elif num1[i] + num1[j] <target:
                i +=1
            else: j -=1

sol = Solution()
print sol.twoSum([-1,-2,-3,-4,-5],-8)