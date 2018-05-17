# -*- coding:utf-8 -*-


# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
#
# Example 1:
#
#
# Input: 11
# Output: 3
# Explanation: Integer 11 has binary representation 00000000000000000000000000001011 
#
#
# Example 2:
#
#
# Input: 128
# Output: 1
# Explanation: Integer 128 has binary representation 00000000000000000000000010000000
#
#


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #自己写的，方法1，转换成字符串，数1的个数
        '''
        return bin(n).count('1')
        '''
        #方法二，不断向右位移，如果末位等于1，count + 1
        '''
        count = 0
        if n == 0: return count
        for _ in range(32):
            count += (n & 1)
            n >>= 1
        return count
        '''
        #看了汉明重量的维基百科，利用树状相加是最好的解决办法。
        '''
        m1 = 0x55555555
        m2 = 0x33333333
        m4 = 0x0f0f0f0f
        m8 = 0x00ff00ff
        m16 = 0x0000ffff
        h01 = 0x01010101
        '''
        #最原始的写法如下，这也是树状相加的基本思路，但是效率比较低，用到的计算次数比较多
        '''
        n = (n & m1) + ((n >> 1) & m1)
        n = (n & m2) + ((n >> 2) & m2)
        n = (n & m4) + ((n >> 4) & m4)
        n = (n & m8) + ((n >> 8) & m8)
        n = (n & m16) + ((n >> 16) & m16)
        return n
        '''
        #改进版的算法，计算次数有所减少
        '''
        n -= (n >> 1) & m1             #put count of each 2 bits into those 2 bits
        n = (n & m2) + ((n >> 2) & m2) #put count of each 4 bits into those 4 bits 
        n = (n + (n >> 4)) & m4        #put count of each 8 bits into those 8 bits 
        n += n >>  8  #put count of each 16 bits into their lowest 8 bits
        n += n >> 16  #put count of each 32 bits into their lowest 8 bits
        return n & 0xff
        '''
        #终极版的算法，计算次数最少，效果最好，但是好像有错。。。
        '''
        n -= (n >> 1) & m1             #put count of each 2 bits into those 2 bits
        n = (n & m2) + ((n >> 2) & m2) #put count of each 4 bits into those 4 bits 
        n = (n + (n >> 4)) & m4        #put count of each 8 bits into those 8 bits 
        return (n * h01) >> 24  #returns left 8 bits of n + (n<<8) + (n<<16) + (n<<24) + ... 
        '''
        #如果已知大多数位是0的话，还有更快的算法。这些更快的算法是基于这样一种事实即n与n - 1相与得到的最低位永远是0,例如n = 01000100010000,n - 1 = 01000100001111,n & (n - 1) = 01000100000000。减1操作将最右边的符号从0变到1，从1变到0，与操作将会移除最右端的1。如果最初n有N个1，那么经过N次这样的迭代运算，n将减到0。下面的算法就是根据这个原理实现的。
        '''
        count = 0
        while n > 0:
            n &= n - 1
            count += 1
        return count
        '''
        #如果已知大多数位是1的话，也许可以把n &= n - 1的条件改成n |= n + 1?
        count = 0
        while n < 0xffffffff:
            n |= n + 1
            count += 1
        return 32 - count
