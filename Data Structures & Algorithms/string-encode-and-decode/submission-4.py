class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for s in strs:
            encoding = encoding + str(len(s)) + ":" + s
        return encoding

    def decode(self, s: str) -> List[str]:
        strs = []
        print(s)
        while len(s)>0:
            i = 0
            while s[i]!= ":":
                i+=1
            print(i)
            length = int(s[:i])
            strs.append(s[1+i:(1+i+length)])
            s = s[1+i+length:]
        return strs