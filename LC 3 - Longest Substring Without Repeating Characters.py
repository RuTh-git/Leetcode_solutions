class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 # first pointer
        res = 0
        
        for r in range(len(s)): # r is second pointer
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        # TC - O(n), SC - O(m)
        # Where n = len(s) and m = total no. of unique characters in s.
