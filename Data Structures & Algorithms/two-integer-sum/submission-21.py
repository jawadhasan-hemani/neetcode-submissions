class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}

        for i, num in enumerate(nums):
            nums_set[num] = i # dict[key] = value

        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_set and i != nums_set[diff]:
                return [i, nums_set[diff]]

