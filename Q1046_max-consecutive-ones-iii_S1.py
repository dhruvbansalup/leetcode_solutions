class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        zeros=0
        l=0
        maxarr=0

        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            maxarr=max(maxarr,r-l+1)

        return maxarr