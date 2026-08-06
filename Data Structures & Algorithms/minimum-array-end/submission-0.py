class Solution:
    def minEnd(self, n: int, x: int) -> int:
        gapFiller = bin(n-1)[2:]
        xBin = "0"*len(gapFiller) +  bin(x)[2:]
        
        nP = len(gapFiller)-1
        xP = len(xBin)-1

        while xP > -1 and nP > -1:
            if xBin[xP] == "0":
                xBin = xBin[:xP] + gapFiller[nP] + xBin[xP+1:]
                nP -= 1
            xP -= 1
        return int(xBin,2)