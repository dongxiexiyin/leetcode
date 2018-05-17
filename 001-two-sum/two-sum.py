# -*- coding:utf-8 -*-


# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#  
#


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    j += 1
            i += 1
        """
        """
        return [(i, j) for i in range(len(nums)) for j in range(len(nums)) if i != j and nums[i] + nums[j] == target][0]
        """
        result_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in result_map.keys():
                return [result_map[complement], i]
            result_map[nums[i]] = i
