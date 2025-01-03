class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Using two pointers:
        l, r = 0, len(numbers) - 1
        while l < r:
            #If their sum makes the target, good return that:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            #If their sum is less than the target, it means you need to make the sum higher, so move the left pointer up by one to make the new sum bigger:
            elif numbers[l] + numbers[r] < target:
                l += 1
            #If their sum is more than the target, it means you need to make the sum lower, so move the right pointer down by one to make the new sum smaller:
            else:
                r -= 1