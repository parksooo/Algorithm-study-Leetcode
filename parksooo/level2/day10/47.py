from typing import List
from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        per = list(permutations(nums))
        res = []
        for i in (per):
            if i not in res:
                res.append(i)
        return res
test = Solution()
print(test.permuteUnique([1,1,2]))