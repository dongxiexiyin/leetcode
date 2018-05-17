# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
#
# Example 1:
#
#
# Input: [1,2,3,1], k = 3
# Output: true
#
# Example 2:
#
#
# Input: [1,0,1,1], k = 1
# Output: true
#
# Example 3:
#
#
# Input: [1,2,1], k = 0
# Output: false
#


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        resultDict = {}
        for i in range(len(nums)):
            if nums[i] in resultDict:
                if abs(i - resultDict[nums[i]] <= k):
                    return True
                else:
                    resultDict[nums[i]] = i
            else:
                resultDict[nums[i]] = i
        return False
