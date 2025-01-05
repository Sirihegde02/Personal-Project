class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        #We will expand from the center to check for palindrome:
        def expand_from_center(left, right):
            #While the indices are valid and the chars are equal, keep expanding from the middle
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1 #Expanding the left pointer to the left
                right += 1 #Expanding the right pointer to the right
            return s[left + 1:right] #Returning the most expanded palindrome

        #Variable for finding the longest substring:
        max_str = s[0]

        #Setting the starting index to do the expanding from:
        for i in range(len(s) - 1):
            odd = expand_from_center(i, i) #If there is an odd palindrome, it will expand from one index
            even = expand_from_center(i, i + 1) #If there is a even palindrome, it will expand from two neighbouring indicies
            
            #Whichever palindrome yeilds the longest substring, is returned:
            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str