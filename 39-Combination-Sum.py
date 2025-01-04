class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        #i: Index of the current candidate being considered
        #current_combination: The current list of numbers being considered
        #total: The sum of numbers in current_combination
        def dfs(i, current_combination, total):
            #Base Case 1: If we find a combination that adds up to the target:
            if total == target:
                res.append(current_combination.copy()) #Append a copy to avoid modifying the result later
                return
            #Base Case 2: If out of bounds (i >= len(candidates)) or total exceeds target. Stop exploring this branch as it cannot yield valid combinations:
            if i >= len(candidates) or total > target:
                return
            #Decision-1: Include the current candidate (candidates[i]) in the combination. Do dfs to see if it has a solution
            current_combination.append(candidates[i])
            dfs(i, current_combination, total + candidates[i])
            #Decision-2: Skip the current candidate and move to the next one. Pop from the combination (cause it was the last item added) and do dfs on the remaining after i (thats why its i + 1) and see if there are any solutions:
            current_combination.pop() #Backtracking (undoing it and checking other possibilities)
            dfs(i + 1, current_combination, total)
        
        #Initialize the pointer to 0, combination to [] and total to 0 (because [] gives 0)
        dfs(0, [], 0)
        return res