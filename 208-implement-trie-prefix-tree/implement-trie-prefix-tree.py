#
# Implement a trie with insert, search, and startsWith methods.
#
#
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEnd = False
        self.links = {}
        
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self
        for ch in word:
            if ch not in node.links:
                node.links[ch] = Trie()
            node = node.links[ch]
        node.isEnd = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self
        for ch in word:
            if ch in node.links:
                node = node.links[ch]
            else:
                node = None
                break
        return node != None and node.isEnd
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self
        for ch in prefix:
            if ch in node.links:
                node = node.links[ch]
            else:
                node = None
                break
        return node != None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
