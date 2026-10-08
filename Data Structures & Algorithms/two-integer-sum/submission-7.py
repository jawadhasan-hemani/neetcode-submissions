class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        q = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in q:
                return [q[diff], i]
            q[num] = i