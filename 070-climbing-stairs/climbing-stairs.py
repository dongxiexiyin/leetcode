# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        #暴力方法，每一步等于前一级台阶的步数加前两级台阶的步数，用递归来写，时间复杂度是O(2^n)，超时了
        return self.climbStairsRec(0, n)
    
    def climbStairsRec(self, i, n):
        if i > n: return 0
        if i == n: return 1
        return self.climbStairsRec(i + 1, n) + self.climbStairsRec(i + 2, n)
        '''
        '''
        #上面的方法在计算过程中做了大量重复的计算，时间复杂度很高，因此可以使用一个数组帮助记录每一步需要的步数，在需要的时候直接从数组中取出值就可以了。这种方法可以把时间复杂度降低到O(n)
        memoList = [0] * (n + 1)
        return self.climbStairsRec(0, n, memoList)
    
    def climbStairsRec(self, i, n, l):
        if i > n: return 0
        if i == n: return 1
        if l[i] > 0: return l[i]
        l[i] = self.climbStairsRec(i + 1, n, l) + self.climbStairsRec(i + 2, n, l)
        return l[i]
        '''
        '''
        #这个问题可以分解为多个相同的子任务。假设当前在第i级台阶，那么他可以通过以下两种方式到达：1、在第i-1级台阶上迈一步；2、在第i-2级台阶上迈两步。于是，第i级台阶的方法数=第i-1级台阶的方法数+第i-2级台阶的方法数。设dp[i]为第i级台阶的方法数，那么有dp[i] = dp[i - 1] + dp[i - 2]
        if n == 1: return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
        '''
        '''
        #通过上面的分析完全可以看出这是一个斐波那切数列，目的就是求数列的第n项，但是要注意，初始值分别是1和2，而不是原数列的1和1
        if n == 1: return 1
        first, second = 1, 2
        for i in range(3, n + 1):
            first, second = second, first + second
        return second
        '''
        '''
        #矩阵法，过程有点复杂，看approach 5
        q = [[1, 1], [1, 0]]
        res = self.pow(q, n)
        return res[0][0]
    
    def pow(self, a, n):
        ret = [[1, 0], [0, 1]]
        while n > 0:
            if (n & 1) == 1:
                ret = self.multiply(ret, a)
            n >>= 1
            a = self.multiply(a, a)
        return ret
    
    def multiply(self, a, b):
        c = [[0, 0]] * 2
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c
        '''
        #利用斐波那契数列的通项公式求出第n项的解，通项公式为Fn = 1 / √5(((1 + √5) // 2)^(n + 1) - ((1 - √5) // 2)^(n + 1))
        sqrt5 = math.sqrt(5)
        fibn = pow((1 + sqrt5) / 2, n + 1) - pow((1 - sqrt5) / 2, n + 1)
        return int(fibn / sqrt5)
