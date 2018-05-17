# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
#
# Input: 1
# Output: true
#
# Example 2:
#
#
# Input: 16
# Output: true
#
# Example 3:
#
#
# Input: 218
# Output: false
#


from math import sqrt

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #自己写的，循环除2，判断余数是否为1。不是最快，能不能更好？
        '''
        if n < 1: return False
        while n != 1:
            if n % 2 == 1:
                return False
            else:
                n //= 2
        return True
        '''
        #开方的怎么更慢。。看来开方操作的效率不怎么样，能少用就少用
        '''
        if n < 1: return False
        if n == 1: return True
        while n != 2:
            if sqrt(n) % 2 == 0:
                n = sqrt(n)
            elif sqrt(n / 2) % 2 == 0:
                n = sqrt(n / 2)
            else:
                return False
        return True
        '''
        #把n转换成二进制字符串，判断字符串中1的个数是否为1，如果为1则返回true，否则返回false
        '''
        return False if n < 1 else bin(n).count('1') == 1
        '''
        #位运算也可以
        return False if n < 1 else n & (n - 1) == 0
    
        #这道题其实就是间接的判断整数n的汉明重量是否为1
        #如果去掉整数这个限制条件呢？n可以为小数，怎么做？
        #先分段成(0, 2)和[2, +)两个区间，当n < 2时，radius = 2 // n，然后判断n * radius是否等于2，等于为True，不等为False；当 n >= 2时，radius = n // 2。然后判断n / radius是否等于2，等于为True，不等为False。注意第二种情况是n / radius而非n // radius
        #这个方法不对！！！！！！！
        #这个方法不对！！！！！！！
        #这个方法不对！！！！！！！
        #这个方法判断的是n是否是2的倍数，而不是n是否是n的幂次
        '''
        if n < 0: return False
        if n < 2:
            return True if n * (2 // n) == 2 else False
        else:
            return True if n / (n // 2) == 2 else False
        '''
