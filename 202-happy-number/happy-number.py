# -*- coding:utf-8 -*-


# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 
#
#
# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#
#


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #自己写的，慢，或许递归好一点？
        '''
        if n == 0: return False
        resultSet = set()
        while True:
            if self.squares(n) == 1:
                return True
            else:
                if n in resultSet:
                    return False
                else:
                    resultSet.add(n)
                    n = self.squares(n)
        '''
        #递归果然好一点
        '''
        if n == 0: return False
        resultSet = set()
        return self.isHappyRec(n, resultSet)
    
    def isHappyRec(self, n, s):
        if self.squares(n) == 1:
            return True
        else:
            if n in s:
                return False
            else:
                s.add(n)
                return self.isHappyRec(self.squares(n), s)
    '''
        #之前的循环写的不太好，可以把self.squares(n) == 1作为while退出的条件
        if n == 0: return False
        resultSet = set()
        while n != 1:
            if n in resultSet:
                return False
            else:
                resultSet.add(n)
                n = self.squares(n)
        return True
                    
    def squares(self, n):
        result = 0
        while n != 0:
            result += (n % 10) ** 2
            n //= 10
        return result
