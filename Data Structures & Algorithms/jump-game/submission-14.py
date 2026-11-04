class Solution:
    def canJump(self, nums: List[int]) -> bool:
        finish_line = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= finish_line:
                finish_line = i

        if finish_line == 0:
            return True

        return False