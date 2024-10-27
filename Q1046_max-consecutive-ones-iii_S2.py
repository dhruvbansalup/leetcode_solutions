class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        Curr0=[]#Queue for index of last 0
        l=0
        maxarr=0
  
        for r in range(len(nums)):
           
            if nums[r]==0:
                Curr0.append(r)
                if len(Curr0)>k:  
                    l=Curr0.pop(0)+1    
            maxarr=max(maxarr,r-l+1)

        return maxarr