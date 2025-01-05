class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        # OR nums = [i: for i in range(1, n + 1)]
        nums = []
        for i in range(1, n+1):
            nums.append(i)

        def dfs(i, current_combination):
            #Base case-1: (Success) If the combination has k elements
            if len(current_combination) == k:
                res.append(current_combination.copy()) #Append a copy
                return

            #Base case-2: (Failure) We reached the end of the branch:
            if i == len(nums):
                return

            #Decision-1: Include the current number in the combination:
            current_combination.append(nums[i])
            dfs(i + 1, current_combination)

            #Decision-2: Exclude that number from the combination:
            current_combination.pop()
            dfs(i + 1, current_combination)

        dfs(0, [])
        return res