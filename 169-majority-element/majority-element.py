# -*- coding:utf-8 -*-


# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        #自己写的，太慢，有什么别的办法？
        resultDict = {}
        for n in nums:
            if n not in resultDict.keys():
                resultDict[n] = 1
            else:
                resultDict[n] += 1
        for key in resultDict:
            if resultDict[key] > len(nums) // 2:
                return key
        '''
        '''
        #更慢了...
        nums.sort()
        if len(nums) == 1: return nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                count += 1
                if count > len(nums) // 2:
                    return nums[i]
            else:
                count = 1
        return nums[-1]
        '''
        '''
        #这回快了一点...
        keySet = set()
        for n in nums:
            keySet.add(n)
        for key in keySet:
            if nums.count(key) > len(nums) // 2:
                return key
        '''
        '''
        #approach 2，用collections模块里的Counter类来实现对元素的计数
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        '''
        '''
        #approach 3，排序的方法其实不用那么复杂，排完序之后直接返回第n / 2个元素即可，因为这个元素一定是majority element，不用再统计每个元素出现的次数了
        nums.sort()
        return nums[len(nums)//2]
        '''
        '''
        #approach 4，随机选取元素，判断它是否是主要元素，如果是则返回，如果不是则继续找。时间复杂度理论上可能到达O(∞)，但是通过分析可知需要选择的次数是线性的
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
        '''
        '''
        #approach 5，归并法(Divide and conquer)。一个长度为1的数组的majority element一定是它唯一的元素，利用这一点，我们将数组二分为两部分，分别计算各自的majority element，然后合并两边的结果。如果结果相等，那么没有异议；如果不等，我们需要计算左右两个元素分别在数组中出现的次数，然后决定出谁是majority element
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right
        
        return majority_element_rec(0, len(nums) - 1)
        '''
        #approach 6，Boyer-Moore算法。该算法的原则是遇到主要元素时count + 1，遇到其他元素时count - 1，当count = 0时舍弃前面的结果，重新计算。先选定第一个元素为主要元素，然后依次计算数组中的各个元素，直到最后
        '''
        #自己写的
        if len(nums) == 0: return None
        count = 1
        result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == result:
                count += 1
            else:
                count -= 1
            if count == 0:
                result = nums[i + 1]
        return result
        '''
        #解答写的
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)
        return candidate
                
