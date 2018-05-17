# -*- coding:utf-8 -*-


#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#
# push(x) -- Push element x onto stack.
#
#
# pop() -- Removes the element on top of the stack.
#
#
# top() -- Get the top element.
#
#
# getMin() -- Retrieve the minimum element in the stack.
#
#
#
#
# Example:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
#
#


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        '''
        #approach 1，用另外一个list保存栈中的元素，在这个过程中取得当前的最小元素。时间复杂度是O(n)，超时了
        self.resultList = []
        '''
        '''
        #approach 2，使用另外一个list保存当前的最小元素，当插入一个新元素时，判断是否小于当前的最小元素，如果是那么入栈；出栈的时候判断出栈的元素是否与当前的最小元素相等，如果是那么保存最小元素的栈也要pop
        self.resultList = []
        self.minList = []
        '''
        #approach 3，可以不需要另外一个list来保存当前的最小元素，只需要一个额外的变量表示最小元素，当push的时候，如果被push的元素小于当前的最小元素，那么再将当前最小元素入一次栈；pop的时候，如果pop出的元素和当前最小元素相等，那么再进行一次pop，并将返回值赋给当前最小的元素
        self.resultList = []
        self.currMin = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        '''
        #approach 1
        self.resultList.append(x)
        '''
        '''
        #approach 2
        self.resultList.append(x)
        if len(self.minList) == 0:
            self.minList.append(x)
        elif x <= self.minList[-1]:
            self.minList.append(x)
        '''
        #approach 3
        if self.currMin is None or self.currMin >= x:
            self.resultList.append(self.currMin)
            self.currMin = x
        #elif self.currMin >= x:
        #    self.resultList.append(self.currMin)
        #    self.currMin = x
        self.resultList.append(x)

    def pop(self):
        """
        :rtype: void
        """
        '''
        #approach 1
        self.resultList.pop()
        '''
        '''
        #approach 2
        if self.resultList[-1] == self.minList[-1]:
            self.minList.pop()
        self.resultList.pop()
        '''
        #approach 3
        if self.currMin == self.resultList.pop():
            self.currMin = self.resultList.pop()

    def top(self):
        """
        :rtype: int
        """
        '''
        #approach 1
        return self.resultList[-1]
        '''
        '''
        #approach 2
        return self.resultList[-1]
        '''
        #approach 3
        return self.resultList[-1]

    def getMin(self):
        """
        :rtype: int
        """
        '''
        #approach 1
        if len(self.resultList) == 0: return None
        currMin = self.resultList[-1]
        tempList = []
        while len(self.resultList) != 0:
            if currMin > self.resultList[-1]:
                currMin = self.resultList[-1]
            tempList.append(self.resultList.pop())
        while len(tempList) != 0:
            self.resultList.append(tempList.pop())
        return currMin
        '''
        '''
        #approach 2
        return self.minList[-1]
        '''
        return self.currMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
