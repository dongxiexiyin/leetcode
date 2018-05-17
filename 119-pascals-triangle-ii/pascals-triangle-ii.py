# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#
# Input: 3
# Output: [1,3,3,1]
#
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #自己写的，问题1的改进版，不需要result保存全部的结果，只需要计算够次数，返回计算的结果就可以了
        L = [1]
        i = 0
        while i != rowIndex:
            L = [x + y for x, y in zip([0] + L, L + [0])]
            i += 1
        return L
