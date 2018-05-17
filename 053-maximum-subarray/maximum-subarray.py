# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        #Kadane算法
        if len(nums) == 0: return 0
        maxSum = currSum = nums[0]
        for n in nums[1:]:
            currSum = max(n, currSum + n)
            maxSum = max(currSum, maxSum)
        return maxSum
        '''
        if len(nums) == 0: return 0
        maxSum = nums[0]
        currSum = 0
        for n in nums:
            currSum += n
            if maxSum < currSum:
                maxSum = currSum
            if currSum < 0:
                currSum = 0
        return maxSum
