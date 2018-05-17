# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
#
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
#
#
#
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
#
#


class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        #自己写的，超时
        '''
        resultStr = ''
        g = (str(x) for x in range(1, n + 1))
        for s in g:
            resultStr += s
        return int(resultStr[n - 1])
        '''
        #solution，看不懂，某种数学关系
        #这道题还是蛮有创意的一道题，是说自然数序列看成一个长字符串，问我们第N位上的数字是什么。那么这道题的关键就是要找出第N位所在的数字，然后可以把数字转为字符串，这样直接可以访问任何一位。那么我们首先来分析自然数序列和其位数的关系，前九个数都是1位的，然后10到99总共90个数字都是两位的，100到999这900个数都是三位的，那么这就很有规律了，我们可以定义个变量cnt，初始化为9，然后每次循环扩大10倍，再用一个变量len记录当前循环区间数字的位数，另外再需要一个变量start用来记录当前循环区间的第一个数字，我们n每次循环都减去len*cnt (区间总位数)，当n落到某一个确定的区间里了，那么(n-1)/len就是目标数字在该区间里的坐标，加上start就是得到了目标数字，然后我们将目标数字start转为字符串，(n-1)%len就是所要求的目标位，最后别忘了考虑int溢出问题
        n = n - 1
        for digit in range(1, 11):
            pre = 10 ** (digit - 1)
            
            if n < 9 * pre * digit:
                return int(str(pre + n / digit)[n % digit])
            
            n -= 9 * pre * digit
