class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                # count how many chars of each char we have
                count[ord(c) - ord("a")] += 1 # ord is to get ascii value

            res[tuple(count)].append(s)

        return list(res.values())