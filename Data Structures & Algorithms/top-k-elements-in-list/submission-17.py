class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for n in range(len(nums) + 1)]
        for key, value in count.items():
            freq[value].append(key)

        res = []

        for n in range(len(freq) - 1, 0, -1):
            for stuff in freq[n]:
                res.append(stuff)

                if len(res) == k:
                    return res
                    