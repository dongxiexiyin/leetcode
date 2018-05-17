# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,1]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,1,2,1,2]
# Output: 4
#
#


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        #自己写的，有点慢，怎么快？
        if len(nums) == 1: return nums[0]
        nums.sort()
        i = 0
        while i < len(nums):
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                return nums[i]
            else:
                i += 2
        '''
        '''
        #approach 2，hash table
        result = {}
        for n in nums:
            if n in result.keys():
                result.pop(n)
            else:
                result[n] = 1
        return result.popitem()[0]
        '''
        #approach 3，math 2∗(a+b+c)−(a+a+b+b+c)=c
        return 2 * sum(set(nums)) - sum(nums)
        
