# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
#
# Input: [1,3,5,6], 5
# Output: 2
#
#
# Example 2:
#
#
# Input: [1,3,5,6], 2
# Output: 1
#
#
# Example 3:
#
#
# Input: [1,3,5,6], 7
# Output: 4
#
#
# Example 4:
#
#
# Input: [1,3,5,6], 0
# Output: 0
#
#


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        #自己写的，感觉还能优化？
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
        '''
        #试试二分查找？
        #时间差不多= =
        return self.binarySearchInsert(nums, target, 0, len(nums))
    
    def binarySearchInsert(self, nums, target, start, end):
        if start == end: return start
        middle = (start + end) // 2
        if target == nums[middle]:
            return middle
        elif target < nums[middle]:
            return self.binarySearchInsert(nums, target, 0, middle)
        else:
            return self.binarySearchInsert(nums, target, middle + 1, end)
