class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordBankS = {}
        wordBankT = {}

        if len(s) != len(t):
            return False

        for letter in s:
            wordBankS[letter] = wordBankS.get(letter, 0) + 1

        for letter in t:
            wordBankT[letter] = wordBankT.get(letter, 0) + 1

        return wordBankS == wordBankT
