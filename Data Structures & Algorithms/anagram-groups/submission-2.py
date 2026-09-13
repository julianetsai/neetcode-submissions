class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map of Counter(str), list of result words
        res = defaultdict(list)
        for word in strs:
            counts = [0]*26
            for w in word:
                counts[ord(w)-ord('a')]+=1
            res[tuple(counts)].append(word)

        return [value for value in res.values()]

        