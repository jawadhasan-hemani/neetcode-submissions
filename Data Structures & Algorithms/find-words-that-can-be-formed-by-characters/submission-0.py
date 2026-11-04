class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        for w in words:
            word_count = defaultdict(int)
            good = True
            for c in w:
                word_count[c] += 1
                if c not in count or word_count[c] > count[c]:
                    good = False
            if good:
                res += len(w)

        return res