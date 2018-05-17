# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
#
# Input: 4
# Output: 2
#
#
# Example 2:
#
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.
#
#


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        #自己写的，说我慢
        if x == 0: return 0
        natuals = itertools.count(1)
        for n in natuals:
            if n * n > x:
                return n - 1
            elif n * n == x:
                return n
        '''
        '''
        #二分查找
        if x == 0: return 0
        start, end = 1, x
        while start < end:
            mid = (start + end) // 2
            if mid <= x // mid and mid + 1 > x // (mid + 1):
                return mid
            elif mid > x // mid:
                end = mid
            else:
                start = mid + 1
        return start
        '''
        #牛顿法
        if x == 0: return 0
        n = x
        while n > x // n:
            n = (n + x // n) // 2
        return n
        
        
