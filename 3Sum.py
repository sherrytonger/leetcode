__author__ = 'Sherry'

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.

#solution 1: time exceeded
class Solution1:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        result = []
        temp = []
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                for k in range(j+1, len(num)):
                    if num[i]+num[j]+num[k] == 0:
                        result.append([num[i],num[j],num[k]])
        #deduplicate
        for x in result:
            x1 = sorted(x)
            if x1 not in temp:
                temp.append(x1)
        return temp
class Solution2:
    def threeSum(self, num):
        num = sorted(num)
        i, result = 0, set()
        while i < len(num)-2:
            j = i+1
            k = len(num)-1
            while j<k:
                if num[i]+num[j]+num[k] == 0:
                    result.add((num[i],num[j],num[k]))
                    j +=1
                elif num[i]+num[j]+num[k]>0:
                    k -=1
                else: j +=1
            i +=1
        return [list(t) for t in result]

print 'here'
sol = Solution2()
print sol.threeSum([-1,0,1,2,-1,-4])