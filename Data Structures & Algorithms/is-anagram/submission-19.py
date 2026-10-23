class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i, letter in enumerate(s):
            s_dict[letter] += 1

        for i, letter in enumerate(t):
            t_dict[letter] += 1

        return s_dict == t_dict