class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        c_count = defaultdict(int)
        good = True

        for c in ransomNote:
            c_count[c] += 1
            if c not in count or c_count[c] > count[c]:
                good = False

        return good