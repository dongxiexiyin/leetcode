# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #Brute Force
        #一种Solution，先排序，然后设置三个index i j k，i对nums做一次循环，每次循环中j和k一个在头一个在尾，往中间靠拢，有重复元素就跳过
        resultList = []
        nums.sort()
        if len(nums) < 3: return resultList
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tripleSum = nums[i] + nums[j] + nums[k]
                if tripleSum < 0:
                    j += 1
                elif tripleSum > 0:
                    k -= 1
                else:
                    resultList.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return resultList
