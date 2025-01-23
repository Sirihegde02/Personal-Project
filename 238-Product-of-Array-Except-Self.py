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

        # #Using the division operator:
        # #Time complexity: O(n)
        # #Space complexity: O(1) since the output array is excluded from space analysis.
        # n = len(nums)
        # output = [1] * n
        # product = 1
        # zero_flag = 0
        # for num in nums:
        #     if num:
        #         product *= num
        #     else:
        #         zero_flag += 1
        # if zero_flag > 1:
        #     return [0] * n

        # for i,c in enumerate(nums):
        #     if zero_flag:
        #         if c:
        #             output[i] = 0
        #         else:
        #             output[i] = product
        #     else:
        #         output[i] = product // c
        # return output

        # #Best approach:
        # #Using three lists , where two lists store the previous and upcoming number products
        # #Time complexity: O(n)
        # #Space complexity: O(n)
        # n = len(nums)
        # output = [0] * n
        # pref = [0] * n
        # suff = [0] * n

        # pref[0] = suff[n - 1] = 1
        # for i in range(1, n):
        #     pref[i] = nums[i - 1] * pref[i - 1]
        # #Traversing from n-2 end to -1 beginning:
        # for i in range(n - 2, -1, -1):
        #     suff[i] = nums[i + 1] * suff[i + 1]
        # for i in range(n):
        #     output[i] = pref[i] * suff[i]
        # return output

        #More optimal solution:
        #Time complexity: O(n)
        #Space complexity: O(1) Since the output array is excluded from space analysis
        n = len(nums)
        output = [1] * n
        pref = 1
        for i in range(n):
            output[i] = pref
            pref *= nums[i] #Update the prefix for the next output number
        posf = 1
        for i in range(n - 1, -1, -1):
            output[i] *= posf
            posf *= nums[i] #Update the postfix for the next output number
        return output