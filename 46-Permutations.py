class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #Using backtracking
        result = [] #List to store all possible permutations:
        #Base case - 1:If there is only one number left, return it as the sole permutation: 
        if len(nums) == 1:
            return [nums.copy()] #Copy the list to avoid modifying the original #Or do nums[:] to make the running faster.
        #Iterating over the numbers in the list:
        for i in range(len(nums)):
            n = nums.pop(0) #Remove the first number (index 0) to explore permutations of the rest
            permutations = self.permute(nums) #Recursively look for permutations for remaining nums (after modification)
            #Add the removed number to each of the permutations:
            for perm in permutations:
                perm.append(n)
            result.extend(permutations) #When appending multiple values you can use extend
            nums.append(n) #Restoring the original list by adding back the removed number
        return result
