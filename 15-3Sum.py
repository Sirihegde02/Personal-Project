class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        #Loop to find the pair of integers that sum up with each number in nums from the for loop:
        for i, value in enumerate(nums):
            if i > 0 and value == nums[i-1]:
                continue
            #Two-pointer approach on the remaining of the list:
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum == 0:
                    result.append([value , nums[l], nums[r]])
                    #We need to add other pairs to this result, so we need to update the pointers after finding a result, to find the other results. We only need to update one of the pointers, cause the other pointer will get updated by the code below. So let's update the left pointer:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: #Making sure we aren't pointing to the same value
                        l += 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
        return result
