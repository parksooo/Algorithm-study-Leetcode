from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ct_p = Counter(p)
        res = []
        limit = len(s) - len(p) + 1
        l_p = len(p)
        for i in range(limit):
            if Counter(s[i : i + l_p]) == ct_p:
                res.append(i)
        return res

test = Solution()
print(test.findAnagrams("cbaebabacd", "abc"))
print(test.findAnagrams("abab", "ab"))