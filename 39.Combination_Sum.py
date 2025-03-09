from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i, target, tmpList):
            if target == 0:
                result.append(tmpList[:])  
                return

            for j in range(i, len(candidates)):  
                if candidates[j] > target:
                    continue
                backtrack(j, target - candidates[j], tmpList + [candidates[j]])  

        backtrack(0, target, []) 
        return result