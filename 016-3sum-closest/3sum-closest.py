# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Brute Force
        #大的思路和之前的3Sum是一样的，也是先排序，然后设置三个游标，一个遍历，另外两个一头一尾向中间靠拢，没想明白的是什么时候该j++，什么时候该k--，看了一个Solution，需要对tripleSum和target进行比较
        if len(nums) < 3: return None
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tripleSum = nums[i] + nums[j] + nums[k]
                if abs(tripleSum - target) < abs(closestSum - target):
                    closestSum = tripleSum
                if tripleSum < target:
                    j += 1
                elif tripleSum > target:
                    k -= 1
                else:
                    return target
        return closestSum
