# -*- coding:utf-8 -*-


# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
#
# Input: [3,0,1]
# Output: 2
#
#
# Example 2:
#
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
#


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #自己写的，先排序，再找出缺的那个
        '''
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                return nums[i] - 1
        return nums[-1] + 1 if nums[0] == 0 else nums[0] - 1
        '''
        #也是自己写的，还是不够快
        '''
        maxNum = max(nums)
        minNum = min(nums)
        listSum = sum(nums)
        nSum = sum((x for x in range(maxNum + 1)))
        if minNum != 0: return 0
        elif minNum == 0 and listSum == nSum: return maxNum + 1
        else: return nSum - listSum
        '''
        #approach 2，用set
        '''
        resultSet = set(nums)
        for i in range(len(nums) + 1):
            if i not in resultSet:
                return i
        '''
        #approach 3，用XOR，把nums的长度和所有的index和value XOR在一起，剩下的那个就是missing number
        '''
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        return missing
        '''
        #高斯公式，其实我写的第二个也是利用高斯公式，但是搞得有点复杂，其实只要算出n项和，减去数组和，就是结果，不用求什么最大最小
        nSum = len(nums) * (len(nums) + 1) // 2
        listSum = sum(nums)
        return nSum - listSum
        
