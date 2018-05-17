# -*- coding:utf-8 -*-


# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
#
#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.
#
#


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #没思路，看了解答，用动态编程的思想
        #dp[i] means the max money when robbed house[0,i]
        #if rob house[i], then dp[i] = money of house[i] + dp[i-2]
        #if don't rob house[i], then dp[i] = dp[i-1]
        #so, dp[i] = max(money[i] + dp[i-2], dp[i-1])
        #This problem can be solved in O(1) space.
        if not nums: return 0
        odd, even = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                odd = max(odd + nums[i], even)
            else:
                even = max(even + nums[i], odd)
        return max(odd, even)
