# Design a data structure that supports the following two operations:
#
#
# void addWord(word)
# bool search(word)
#
#
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# Example:
#
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
#
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.links = {}
        self.isEnd = False
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self
        for ch in word:
            if ch not in node.links:
                node.links[ch] = WordDictionary()
            node = node.links[ch]
        node.isEnd = True
            
        
    #参考别人的答案写出来的，自己写的时候尝试递归不带index的search函数，但是没有成功，参考别人的使用了传入index的search函数，index参数可以帮助控制当前字符的变化，省去了for循环
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        return self.searchResult(word, 0)
    
    def searchResult(self, word, index):
        node = self
        if index == len(word): return node.isEnd
        if word[index] in node.links and word[index] != '.':
            return node.links[word[index]].searchResult(word, index + 1)
        elif word[index] == '.':
            for node1 in node.links.values():
                if node1 != None and node1.searchResult(word, index + 1): return True
            return False
        else:
            return False
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
