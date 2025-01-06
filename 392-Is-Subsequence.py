class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        t_pointer = 0
        s_pointer = 0
        while t_pointer < len(t) and s_pointer < len(s):
            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1
            t_pointer += 1
        return s_pointer == len(s)