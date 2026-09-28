# O(n^2) -> Time complexity
# O(1) -> Space complexity
def check_duplicates(nums: List[int]) -> bool:
    for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
    return False

#O(n) -> Time complexity
#O(n) -> Space complexity
def check_duplicates_hash(nums: List[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return check_duplicates(nums)
        return check_duplicates_hash(nums)
        