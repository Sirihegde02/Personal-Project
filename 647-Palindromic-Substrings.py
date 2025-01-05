class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def find_palindromes(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                nonlocal res
                res += 1
                l -= 1 #Expand l towards left
                r += 1 #Expand r towards right
        for i in range(len(s)):
            #For odd palindromes:
            find_palindromes(i, i)
            #For even palindromes:
            find_palindromes(i, i + 1)
        return res