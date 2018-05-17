# -*- coding:utf-8 -*-


#
# Given a linked list, determine if it has a cycle in it.
#
#
#
# Follow up:
# Can you solve it without using extra space?
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        #用一个dict把每一个节点都记录进去，如果发现重复的节点，即有cycle，如果reach到None则没有
        nodesSeen = {}
        while head is not None:
            if head in nodesSeen.keys():
                return True
            else:
                nodesSeen[head] = 1
            head = head.next
        return False
        '''
        #用两个指针分别标记节点，一个每次走一步，一个每次走两步，如果能相遇，就是cycle
        if head is None or head.next is None:
            return False
        slow, fast = head, head.next
        while fast != slow:
            if fast is None or fast.next is None: 
                return False
            slow = slow.next
            fast = fast.next.next
        return True
