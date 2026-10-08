class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for i in range(len(nums) + 1)]

        for key, value in count.items():
            freq[value].append(key)

        res = []

        for n in range(len(freq) - 1, 0, -1):
            for item in freq[n]:
                res.append(item)
                if len(res) == k:
                    return res