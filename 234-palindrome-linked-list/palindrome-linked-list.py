# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
#
# Input: 1->2
# Output: false
#
# Example 2:
#
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    left = ListNode(0)
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #没思路，看了solution，有如下几种解答
        #1.借助外部空间，将list里的每一个值保存下来，然后判断是否回文，但是需要O(n)的额外空间
        #2.借助递归，先找到链表的末尾元素，然后依次将末尾元素和开始元素进行比较
        #链表特别长的时候，这种方法会超过递归的最大深度，说明递归使用的栈空间也算是使用空间的一种
        '''
        self.left = head
        return self.isPalindromeUtil(head)
    
    def isPalindromeUtil(self, right):
        if right is None: return True
        isRestPallin = self.isPalindromeUtil(right.next)
        if not isRestPallin: return False
        
        isCurrentMatch = (self.left.val == right.val)
        self.left = self.left.next
        return isCurrentMatch
        '''
        #3.翻转链表的后半部分，然后和前半部分比较
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        slow = self.reverseList(slow)
        fast = head
        
        while slow is not None and fast.val == slow.val:
            fast = fast.next
            slow = slow.next
        return slow == None
    
    def reverseList(self, head):
        if head is None: return None
        p = head.next
        head.next = None
        while p:
            s = p.next
            p.next = head
            head = p
            p = s
        return head
