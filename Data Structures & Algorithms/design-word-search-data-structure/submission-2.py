class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] is None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isLeaf = True
        

    def search(self, word: str) -> bool:
        def dfs(r,w):
            if not r:
                return False
            if not w and r.isLeaf:
                return True
            elif not w:
                return False
            if w[0] == ".":
                for i in range(26):
                    if r.children[i] is not None:
                        if dfs(r.children[i],w[1:]):
                            return True
                return False
            else:
                i = ord(w[0]) - ord("a")
                return dfs(r.children[i],w[1:])
        
        cur = self.root
        return dfs(cur,word)
