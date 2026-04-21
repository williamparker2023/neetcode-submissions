class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        unique = set()
        for i in range(len(words)):
            for j in range(len(words[i])):
                unique.add(words[i][j])
        for i in range(len(words)-1):
            src = ""
            snk = ""
            for j in range( min( len(words[i]),len(words[i+1])) ) :
                if words[i][j]!=words[i+1][j]:
                    src = words[i][j]
                    snk = words[i+1][j]
                    break
            if len(words[i])>len(words[i+1]) and src=="":
                return ""
            if src not in adj and src!="":
                adj[src] = set()
            if src!="" and snk!="":
                adj[src].add(snk)
        print(adj)

        enter = {let:0 for let in unique}
        queue = deque()
        for src in adj:
            for snk in adj[src]:
                enter[snk]+=1
        
        for let in enter:
            if enter[let]==0:
                queue.append(let)
        
        ans = ""
        while len(queue)>0:
            curLet = queue.popleft()
            ans = ans + curLet

            if curLet not in adj:
                continue
            
            for snk in adj[curLet]:
                enter[snk] = enter[snk]-1
                if enter[snk]==0:
                    queue.append(snk)

        if len(ans)!=len(unique):
            return ""
        return ans