# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        '''
        #自己写的，两个列表都没有结束之前，依次拼，有一个结束之后，把另一个的剩下所有元素拼进去
        curr = resultHead = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        #当有一个列表结束以后，不需要再做while循环，直接把没结束列表的剩余部分加到最后边
        #while l1:
        #    curr.next = l1
        #    l1 = l1.next
        #    curr = curr.next
        #while l2:
        #    curr.next = l2
        #    l2 = l2.next
        #    curr = curr.next
        curr.next = l1 or l2 #l1 or l2的意思是如果l1有，那么就是l1；如果l1没有，那么就是l2
        return resultHead.next
        '''
        #'''
        #迭代写法
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        #'''

