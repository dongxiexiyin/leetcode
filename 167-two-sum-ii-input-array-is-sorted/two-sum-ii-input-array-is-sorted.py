# -*- coding:utf-8 -*-


# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
#
# Note:
#
#
# 	Your returned answers (both index1 and index2) are not zero-based.
# 	You may assume that each input would have exactly one solution and you may not use the same element twice.
#
#
# Example:
#
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
#


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        #自己写的，跟Two Sum I的解答一样，但是时间慢，说明有更快的方法
        result_map = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in result_map.keys():
                return [result_map[complement] + 1, i + 1]
            result_map[numbers[i]] = i
        '''
        '''
        #设置两个pointer，分别指向开头和结尾，如果相加结果大，那么结尾的--；如果相加结果小，那么开头的++
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        '''
        def bi(s, e, target):
            return bisect.bisect_left(numbers[s:e], target) + s

        l, r = 0, len(numbers)-1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r = min(bi(l+1, r, target - numbers[l]), r-1)
            else:
                l = bi(l+1, r, target - numbers[r])
        return [l+1, r+1]
