class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make a map of s char, freq, then for t subtract. if its zero remove.  map   should be empty at the end
        freq = defaultdict(int)
        for s_ch in s:
            freq[s_ch]+=1
        for t_ch in t:
            freq[t_ch]-=1
            if freq[t_ch]==0:
                del freq[t_ch]
        return len(freq)==0
        # O(n), O(n)

