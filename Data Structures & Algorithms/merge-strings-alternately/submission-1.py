class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ans = ""

        while i<len(word2) and i<len(word1):
            ans = ans + word1[i] + word2[i]
            i+=1
        
        ans = ans + word1[i:]
        ans = ans + word2[i:]
        return ans