# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
#
#
# Given an integer n, generate the nth term of the count-and-say sequence.
#
#
#
# Note: Each term of the sequence of integers will be represented as a string.
#
#
# Example 1:
#
# Input: 1
# Output: "1"
#
#
#
# Example 2:
#
# Input: 4
# Output: "1211"
#
#


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        #'''
        #自己写的，递归里嵌套循环，貌似有点慢，看看解答
        return self.countAndSayRec(n, '1')
    
    def countAndSayRec(self, n, str1):
        if n == 1: return str1
        if len(str1) == 1: return self.countAndSayRec(n - 1, '11')
        i, count = 0, 0
        result = ''
        for j in range(1, len(str1) + 1):
            if j != len(str1) and str1[i] != str1[j]:
                count = str1[i:j].count(str1[i])
                result += str(count) + str1[i]
                #result += str(str1[i])
                i = j
            elif j == len(str1):
        	    count = str1[i:j].count(str1[i])
        	    result += str(count) + str1[i]
        	    #result += str(str1[i])
        return self.countAndSayRec(n - 1, result)
        #'''
        '''
        f="1"
        def say(s):
            i=0
            t=""
            count=1
            flag=0
            while i<len(s)-1:
                if s[i]==s[i+1]:
                    count+=1
                    flag=0
                else:
                    t=t+str(count)+s[i]
                    count=1
                    flag=1
                i+=1
            if flag==0:
                t=t+str(count)+s[i]
            else:
                t=t+"1"+s[i]
            return t
        while n>1:
            f=say(f)
            n-=1
        return f
        '''
        '''
        #这个groupby真的是太高了，看来第三方模块还是要好好学习
        return self.countAndSayRec(n, '1')
    
    def countAndSayRec(self, n, str1):
        if n == 1: return str1
        result = ''.join([str(len(list(g))) + k for k, g in itertools.groupby(str1)])
        return self.countAndSayRec(n - 1, result)
        '''
