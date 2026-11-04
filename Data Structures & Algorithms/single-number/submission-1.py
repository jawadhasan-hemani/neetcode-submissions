class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # res = 0
        # for num in nums:
        #     res = num ^ res
        # return res

        num_set = set()

        for num in nums:
            if num in num_set:
                num_set.remove(num)
                continue
            num_set.add(num)

        return num_set.pop()