class Solution(object):
    def combinationSum2(self, candidates, target):
        uniqueCombinations = set()
        candidates.sort()

        def backtracking(index, combination, sum):
            if sum > target:
                return
            if sum == target:
                uniqueCombinations.add(tuple(combination[:]))
                return
            if index >= len(candidates):
                return

            for i in range(index, len(candidates)):
                # Avoiding duplicates in same recursion level
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                backtracking(i + 1, combination, sum + candidates[i])
                combination.pop()
                i += 1

        backtracking(0, [], 0)
        return [list(comb) for comb in uniqueCombinations]
