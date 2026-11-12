class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = {}

        for letter in s:
            set_s[letter] = 1 + set_s.get(letter, 0)

        set_t = {}
        for letter in t:
            set_t[letter] = 1 + set_t.get(letter, 0)

        return set_s == set_t
            

