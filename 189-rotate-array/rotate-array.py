# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
#
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#
# Example 2:
#
#
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
# Note:
#
#
# 	Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# 	Could you do it in-place with O(1) extra space?
#
#


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #自己写的，感觉是对的，放在sublime里也是对的，但是这里报错，不知道为什么
        '''
        nums = nums[len(nums) - k:] + nums[:len(nums) - k]
        '''
        #还可以append到一个新的list里
        '''
        resultList = []
        resultList += (nums[len(nums) - k:])
        resultList += (nums[:len(nums) - k])
        '''
        #approach 4还有点意思，先翻转所有元素，再依次翻转前k个元素和后n - k个元素
        k = k % len(nums)
        nums.reverse()
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        
    def reverse(self, n, p, q):
        while p < q:
            temp = n[p]
            n[p] = n[q]
            n[q] = temp
            p += 1
            q -= 1
