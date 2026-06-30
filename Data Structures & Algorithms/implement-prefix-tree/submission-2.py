class TrieNode():
    def __init__(self):
        self.isLeaf = False
        self.children = [None]*26

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] is None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isLeaf = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return cur.isLeaf
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return True
        