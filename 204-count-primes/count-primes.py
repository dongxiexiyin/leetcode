# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#


from math import sqrt

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #就想到了一种brute force的方法，写一个函数判断某一个数是否为素数，然后依次循环(0, n)的所有数，统计其中素数的个数，估计会很慢
        #埃氏筛法，廖雪峰教程在讲解filter函数的那一章有具体的讲解
        #这种写法居然超时了。。换一种
        '''
        if n == 0 or n == 1 or n == 2: return 0
        if n == 3: return 1
        count = 0
        it = self.odd_iter()
        while True:
            x = next(it)
            count += 1
            it = filter(self.not_divisible(x), it)
            if x >= n: break
        return count
    
        #定义一个从3开始的奇数序列
    def odd_iter(self):
        n = 1
        while True:
            n += 2
            yield n
            
        #再定义一个筛选函数
    def not_divisible(self, n):
        return lambda x : x % n > 0
        '''
        #一种写法
        count = 0
        resultList = [0] * n
        for i in range(2, n):
            if resultList[i] != -1:
                count += 1
                j = 2 * i
                while j < n:
                    resultList[j] = -1
                    j += i
        return count
