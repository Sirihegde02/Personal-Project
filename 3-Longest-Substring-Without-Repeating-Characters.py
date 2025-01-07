class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 #Sliding window left pointer
        res = 0
        for r in range(len(s)): #Sliding window right pointer changing
            while s[r] in charSet: #If the char is in charSet already
                charSet.remove(s[l]) #Then remove it from the set
                l += 1 #And move the left up
            charSet.add(s[r]) #Add the new char into the set
            res = max(res, r - l + 1) #Where r - l + 1 is the size of the window (substring)
        return res