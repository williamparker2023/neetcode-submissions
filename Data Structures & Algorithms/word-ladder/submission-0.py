class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def countDiff(s1,s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff+=1
            return diff

        if beginWord == endWord:
            return 0
        
        wordList.append(beginWord)
        adj = {}
        for word in wordList:
            adj[word] = []

        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if i == j:
                    continue
                else:
                    if countDiff(wordList[i],wordList[j]) == 1:
                        adj[wordList[i]].append(wordList[j])
        
        #bfs
        q = deque()
        q.append(beginWord)
        size = 1
        numWords = 1
        seen = set()
        seen.add(beginWord)

        while q:
            size-=1
            cur = q.popleft()
            if cur == endWord:
                return numWords

            if cur not in adj:
                continue
            
            for snk in adj[cur]:
                if snk not in seen:
                    seen.add(snk)
                    q.append(snk)

            if size<=0:
                size = len(q)
                numWords += 1
            

        return 0