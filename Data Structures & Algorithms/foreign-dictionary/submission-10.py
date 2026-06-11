class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        n = len(words)
        seenLetters = set()
        for i in range(n-1):
            if len(words[i])>len(words[i+1]) and words[i][:len(words[i+1])]==words[i+1]:
                print("asdfa")
                return ""
            for c in words[i]:
                seenLetters.add(c)
        for c in words[-1]:
            seenLetters.add(c)

        for i in range(n-1):
            if words[i] == words[i+1]:
                continue
            l = 0
            r = 0
            word1 = words[i]
            word2 = words[i+1]
            if word1 == word2[:len(word1)]:
                continue
            while l<len(word1) and r<len(word2) and word1[l]==word2[r]:
                l+=1
                r+=1
            u = word1[l]
            v = word2[r]
            if u not in adj:
                adj[u] = []
            adj[u].append(v)

        inCount = {c:0 for c in seenLetters}
        for c in adj:
            for cNext in adj[c]:
                inCount[cNext] += 1
        
        q = deque()

        for c in inCount:
            if inCount[c] == 0:
                q.append(c)

        ans = ""
        while q:
            c = q.popleft()
            ans = ans + c
            if c not in adj:
                continue
            for cNext in adj[c]:
                inCount[cNext] -= 1
                if inCount[cNext] == 0:
                    q.append(cNext)
        if len(ans)<len(seenLetters):
            return ""
        return ans