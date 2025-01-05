class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            #Base case-1: (success) We have processed all elements in the list:
            if i == len(nums):
                res.append(subset.copy()) #Append a copy
                return

            #Decision-1: Include the current element in the subset:
            subset.append(nums[i])
            dfs(i + 1, subset) #Do DFS on the updated subset

            #Decision-2: Exclude the last added element in the subset:
            subset.pop()
            dfs(i + 1, subset) #Do DFS on the subset

        dfs(0, [])
        return res