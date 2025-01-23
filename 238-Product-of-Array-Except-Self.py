class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # #Brute Force:
        # #Time complexity: O(n^2)
        # #Space complexity: O(1) since the output array is excluded from space analysis.
        # n = len(nums)
        # output = [0] * n
        # for i in range(n):
        #     product = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         product *= nums[j]
        #     output[i] = product
        # return output

        #Using the division operator:
        #Time complexity: O(n)
        #Space complexity: O(1) since the output array is excluded from space analysis.
        n = len(nums)
        output = [1] * n
        product = 1
        zero_flag = 0
        for num in nums:
            if num:
                product *= num
            else:
                zero_flag += 1
        if zero_flag > 1:
            return [0] * n

        for i,c in enumerate(nums):
            if zero_flag:
                if c:
                    output[i] = 0
                else:
                    output[i] = product
            else:
                output[i] = product // c
        return output