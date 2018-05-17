# -*- coding:utf-8 -*-


# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
#
# 	You must do this in-place without making a copy of the array.
# 	Minimize the total number of operations.
#
#


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #自己写的，先把0都挑出去，最后再补上，还有没有别的方法？
        '''
        cnt, i = 0, 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                cnt += 1
            else:
                i += 1
        nums += [0] * cnt
        '''
        #approach 2,用两个pointer把非0元素排到前面去，然后添加0
        lastNonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZero] = nums[i]
                lastNonZero += 1
        for i in range(lastNonZero, len(nums)):
            nums[i] = 0
