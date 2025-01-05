class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort() #Sorting the numbers
        i = 0 #Making sure the numbers are incrementing by one
        while i < len(nums):
            if nums[i] == i: #Its good if the number is equal to it's index
                i += 1 #Incrementing for the next loop
                continue
            else:
                return i
        return i #This has already been incremented before the loop broke because i == len(nums)

        #The follow-up answer:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum