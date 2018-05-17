# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
#


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        '''
        #自己写的，需要利用generator
        #尝试写一个不用generator的
        result = []
        i = 0
        if numRows == 0: return result
        for t in self.triangles():
            result.append(t)
            i += 1
            if i == numRows: break
        return result
    
    
    def triangles(self):
        '''
        result = []
        L = [1]
        i = 0
        if numRows == 0: return result
        while i < numRows:
            result.append(L)
            L = [x + y for x, y in zip([0] + L, L + [0])]
            i += 1
        return result
        '''
        L = [1]
        while True:
            yield L
            L = [x+y for x,y in zip( [0]+L, L+[0] )]
        '''
        '''
        L = [1]
        while True:
            yield L
            M = L[:]
            M.append(0)
            L = [M[i - 1] + M[i] for i in range(len(M))]
        '''
        '''
        L1, L2 = [], []
        n = 1
        while True:
            if n == 1:
                L1 = [1]
                n += 1
                yield L1
            elif n == 2:
                L1 = [1, 1]
                n += 1
                yield L1
            else:
                L2.append(1)
                for x in range(1, n - 1):
                    L2.append(L1[x - 1] + L1[x])
                L2.append(1)
                L1 = L2
                L2 = []
                n += 1
                yield L1
        '''
        '''
        n = 1
        while True:
            if n == 1:
                L=[1]
                n += 1
                yield [1]
            elif n == 2:
                L = [1,1]
                n += 1
                yield L
            else:
                L=[1]+[L[x]+L[x-1] for x in range(1,len(L))]+[1]
                n += 1
                yield L
        '''
