__author__ = 'Sherry'

# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) == 1: return True
        if len(s) != len(t): return False
        #use string s as a dict
        s_dict = dict()
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = t[i]
            elif s_dict[s[i]] != t[i]:
                return False
        for i in s_dict:
            for j in s_dict:
                if i!=j:
                    if s_dict[i] == s_dict[j]:
                        return False


        return True




sol = Solution()
print sol.isIsomorphic('ab', 'cc')
print sol.isIsomorphic('paper', 'title')
print sol.isIsomorphic('hello','sheis')