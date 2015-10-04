__author__ = 'Sherry'
# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
#     Each child must have at least one candy.
#     Children with a higher rating get more candies than their neighbors.
#
# What is the minimum candies you must give?
# tag: greedy

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        count = 0
        candys = [1 for i in range(len(ratings))]
        if len(ratings) == 0:
            return 0
        elif len(ratings) == 1:
            return 1
        else:
            for i in range(len(ratings)-1):
                if ratings[i] < ratings[i+1]:
                    candys[i+1] = candys[i] + 1

            for i in range(len(ratings)-1,0,-1):
                if ratings[i] < ratings[i-1]:
                    if candys[i] >= candys[i-1]:
                        candys[i-1] = candys[i] + 1
        return sum(candys)


