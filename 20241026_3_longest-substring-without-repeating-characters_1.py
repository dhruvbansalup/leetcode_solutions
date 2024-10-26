class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l=0
        maxlen=0
        seen={} #char:index
        for r in range(len(s)):           
            if s[r] in seen.keys():
                if l<=seen[s[r]]:
                    l=seen[s[r]]+1
                    
            seen[s[r]]=r
            maxlen=max(maxlen,r-l+1)
        
        return maxlen