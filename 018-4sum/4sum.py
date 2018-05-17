# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#
#


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #方法同3Sum， 但是不知道为什么过不了，自己运行的结果是对的。而且感觉会超时，有没有更好的办法？
        '''
        resultList = []
        nums.sort()
        if len(nums) < 4: return resultList
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                    k, l = j + 1, len(nums) - 1
                    while k < l:
                        qSum = nums[i] + nums[j] + nums[k] + nums[l]
                        if qSum < target:
                            k += 1
                        elif qSum > target:
                            l -= 1
                        else:
                            resultList.append([nums[i], nums[j], nums[k], nums[l]])
                            k += 1
                            l -= 1
        return resultList
        '''
        #一个Solution，通过额外的空间进行辅助存储
        d = dict()
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                sum2 = nums[i] + nums[j]
                if sum2 in d:
                    d[sum2].append((i, j))
                else:
                    d[sum2] = [(i, j)]
        
        result = set()
        for key in d:
            value = target - key
            if value in d:
                list1 = d[key]
                list2 = d[value]
                for (i, j) in list1:
                    for (k, l) in list2:
                        if i != k and i != l and j != k and j != l:
                            flist = [nums[i], nums[j], nums[k], nums[l]]
                            flist.sort()
                            result.add(tuple(flist))
        return list(result)
