class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode with length?
        # 5|Hello10|World
        encoded = ""
        for word in strs:
            l =str(len(word)) + '|'
            encoded += l + word

        return encoded

    def decode(self, s: str) -> List[str]:
        i=0
        res = []
        print(s)
        # 5|Hello5|World

        while i < len(s):
            breaker = s[i:].index('|')
            # print(i, i+breaker)
            length = int(s[i:i+breaker])
            start = i+breaker+1
            end = start+length
            res.append(s[start:end])
            i = end

        return res


