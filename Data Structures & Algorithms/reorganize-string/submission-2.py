class Solution:
    def reorganizeString(self, s: str) -> str:
        hp = []
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        
        for c in freq:
            heapq.heappush(hp,[-freq[c],c])
        
        ans = ""

        while hp:
            count1, c1 = heapq.heappop(hp)
            if len(ans) > 0 and ans[-1] == c1:
                if hp:
                    count2, c2 = heapq.heappop(hp)
                    ans += c2
                    heapq.heappush(hp,[count1,c1])
                    if count2 < -1:
                        heapq.heappush(hp,[count2+1,c2])
                else:
                    return ""
            else:
                ans += c1
                if count1 < -1:
                    heapq.heappush(hp,[count1+1,c1])
        
        return ans