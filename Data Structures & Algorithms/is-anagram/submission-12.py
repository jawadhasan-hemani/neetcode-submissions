class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {}

        for letter in s:
            word1[letter] = 1 + word1.get(letter, 0)

        for letter in t:
            word2[letter] = 1 + word2.get(letter, 0)

        print(word1)
        print(word2)

        return sorted(s) == sorted(t)
