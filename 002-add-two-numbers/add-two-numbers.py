# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r1, r2 = 0, 0
        i, j = 0, 0
        while l1:
            r1 += l1.val * (10 ** i)
            l1 = l1.next
            i += 1
        while l2:
            r2 += l2.val * (10 ** j)
            l2 = l2.next
            j += 1
        result = r1 + r2
        l3 = dummyHead = ListNode(0)
        if result == 0:
            l3.next = ListNode(0)
            return dummyHead.next
        while result != 0:
            l3.next = ListNode(result % 10)
            result //= 10
            l3 = l3.next
        return dummyHead.next
