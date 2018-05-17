# Write a function that takes a string as input and reverse only the vowels of a string.
#
#
# Example 1:
# Given s = "hello", return "holle".
#
#
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
#
#
# Note:
# The vowels does not include the letter "y".
#


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #自己写的，先把所有元音保存到一个set里，然后从头判断字符串的每个字符是不是元音，如果是，那么就用数组里的元音替换已有的
        '''
        vowelSet = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
        vowelList = []
        resultStr = ''
        for ch in s:
            if ch in vowelSet:
                vowelList.append(ch)
        for i in range(len(s)):
            resultStr += vowelList.pop() if s[i] in vowelSet else s[i]
        return resultStr
        '''
        #这样的写法也可以，保存在str里看能不能快点
        vowels = 'aAeEiIoOuU'
        s = list(s)
        vs = [i for i in s if i in vowels]
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vs.pop()
        return ''.join(s)
