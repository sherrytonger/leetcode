__author__ = 'Sherry'
# Palindrome 1
# Given a string s, partition s such that every substring of the partition is a palindrome
# Return all possible palindrome partitioning of s.
# Solution 1 returns max length of palindrome string
# Solution 2 returns all palindrome string using dynamic programming

# Palindrome 2
#  Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.
class Solution:
    # @param s, a string
    # @return a list of lists of string

    def partition(self, s):
        partitions = [[[]]]
        for i in range(len(s)):
            starti = []
            for j in range(i+1):
                if self.isPalindrome(s[j:i+1]):
                    starti.append(j)
            temp = []
            for k in starti:
                for par in partitions[k]:
                    temp = temp + [par + [s[k:i+1]]]
            partitions.append(temp)

            #partitions.append([partition + [s[j:i+1]] for j in starti for partition in partitions[j]])

        return partitions[-1]

    def isPalindrome(self,s):
        i,j = 0,len(s)-1
        while i<j:
            if s[i]!=s[j]: return False
            i +=1
            j -=1
        return True
# Palindrome 2
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.
class Solution1:
    def minCut(self,s):
        count = 0
        bool = [[]]
        dp = []
        i = 0
        j = 0
        bool = [[0]*len(s) for i in range(len(s))]
        for i in range(len(s)+1):
            dp.append(len(s) - i - 1)
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i]==s[j] and (j-i<2 or bool[i+1][j-1]):
                    bool[i][j] = 1
                    dp[i] = min(dp[i],dp[j+1]+1)
        return dp[0]
    def isPalindrome(self,s):
        i,j = 0,len(s)-1
        while i<j:
            if s[i]!=s[j]: return False
            i +=1
            j -=1
        return True


#  partitions[i] stores the possible partitions for the substring s[:i]
#  make starts[i] hold a list of starting indices of all palindromes ending in i-1
class Solution2:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        partitions = [[[]]]
        starts = [[]]
        for i in range(len(s)):
            starts_i = [i]
            for j in starts[-1] + [i]:
                if j-1 >= 0 and s[j-1] == s[i]:
                    starts_i.append(j-1)
            starts.append(starts_i)
            #print starts
            partitions.append([partition + [s[j:i+1]] for j in starts_i for partition in partitions[j]])
            #print partitions
        #print partitions
        return partitions[-1]


sol = Solution1()
#print sol.minCut("aabaac")
print sol.minCut("cabababcbc")
