class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute-force:
        # max_area = 0
        # for l in range(len(height)):
        #     for r in range(l+1, len(height)):
        #         curr_area = min(height[left], height[right]) * (right-left)
        #         max_area = max(max_area, curr_area)
        # return max_area

        #optimal solution:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            curr_area = min(height[left], height[right]) * (right-left)
            max_area = max(max_area, curr_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area