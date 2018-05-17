#
# Implement the following operations of a queue using stacks.
#
#
# push(x) -- Push element x to the back of queue.
#
#
# pop() -- Removes the element from in front of queue.
#
#
# peek() -- Get the front element.
#
#
# empty() -- Return whether the queue is empty.
#
#
# Notes:
#
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
#
#


class MyStack:
    
    def __init__(self):
        self.l = []
        
    def push(self, x):
        self.l.append(x)
        
    def pop(self):
        if not self.l: return None
        return self.l.pop(0)
    
    def peek(self):
        if not self.l: return None
        return self.l[0]
    
    def empty(self):
        return len(self.l) == 0

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = MyStack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.s.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.s.peek()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.s.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
