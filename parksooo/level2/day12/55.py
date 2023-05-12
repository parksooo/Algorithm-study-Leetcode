from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [False] * l
        dp[0] = True



a = [5, 3, 2, 1, 2, 0]
