# -*- coding:utf-8 -*-


# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #自己写的，用循环，有点慢，有点奇怪
        dummyHead = curr = ListNode(0)
        curr.next = head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else: 
                curr = curr.next
        return dummyHead.next
