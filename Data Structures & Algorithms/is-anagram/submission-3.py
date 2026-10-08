class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = {}
        two = {}

        for char in s:
            one[char] = 1 + one.get(char, 0)

        for char in t:
            two[char] = 1 + two.get(char, 0)

        return one == two