class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        my_sum = 0
        i = 0
        
        while i < len(s):
            # Check if the next character exists and if it represents a larger value
            if i + 1 < len(s) and my_dict[s[i]] < my_dict[s[i + 1]]:
                my_sum += my_dict[s[i + 1]] - my_dict[s[i]]
                i += 2  # Skip the next character since it is already processed
            else:
                my_sum += my_dict[s[i]]
                i += 1  # Move to the next character
        
        return my_sum
