class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = defaultdict(int)

        for letter in s:
            word1[letter] = 1 + word1.get(letter, 0)

        for letter in t:
            word2[letter] += 1

        return word1 == word2
