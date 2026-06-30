class TrieNode():
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
        def dfs(wLeft,cur):
            if not cur:
                return False
            if len(wLeft) == 0 and cur.isLeaf:
                return True
            if len(wLeft) == 0:
                return False
            
            if wLeft[0] == ".":
                for i in range(26):
                    if dfs(wLeft[1:],cur.children[i]):
                        return True
                return False
            
            i = ord(wLeft[0]) - ord("a")
            print(i)
            if cur.children[i] is None:
                return False
            return dfs(wLeft[1:],cur.children[i])
        return dfs(word,self.root)

