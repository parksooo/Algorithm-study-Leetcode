from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s ,e= 0 ,len(nums) - 1
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:
                return mid
            if nums[s] <= nums[mid]:
                if target < nums[s] or target > nums[mid]:
                    s = mid + 1
                else:
                    e = mid - 1
            else:
                if target < nums[mid] or nums[e] < target:
                    e = mid - 1
                else:
                    s = mid + 1
        return -1

test = Solution()
# print(test.search([4,5,6,7,0,1,2], 0))
print(test.search([1, 3], 3))