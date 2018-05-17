# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#
# Example 1:
#
#
# Input: [1,2,3,1]
# Output: true
#
# Example 2:
#
#
# Input: [1,2,3,4]
# Output: false
#
# Example 3:
#
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
#


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #自己写的，用了set
        '''
        resultSet = set()
        for n in nums:
            if n in resultSet:
                return True
            else:
                resultSet.add(n)
        return False
        '''
        #排序也可以
        '''
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
        '''
        #还可以这样
        resultSet = set(nums)
        return len(resultSet) < len(nums)
