class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = [] #List of all valid IP addresses
        #If the length of s is longer than 12 characters, it cannot be a valid IP address:
        if len(s) > 12:
            return res
        #Helper function to perform backtracking:
        def dfs(i, dots, current_IP):
            #Base case-1: (Success) When the 4 dots are already placed and all the characters in s are processed:
            if dots == 4 and i == len(s):
                res.append(current_IP[:-1]) #Appending the solution without the \.\ on the end to the result
                return
            #Base case-2: (Failure) If more than 4 dots are placed, the IP is invalid
            if dots > 4:
                return
            
            #Explore placing a dot after each valid segment of the string (segments of length 1 through 3)
            for j in range(i, min(i + 3, len(s))):
                #To form a valid segment the number must be less than 256 and shouldn't have leading 0s (unless it's a 0)
                if int(s[i:j + 1]) < 256 and (i == j or s[i] != \0\):
                    #Recur for the next segment, adding the current segment to `current_IP`:
                    dfs(j + 1, dots + 1, current_IP + s[i:j + 1] + \.\)

        dfs(0, 0, \\)
        return res