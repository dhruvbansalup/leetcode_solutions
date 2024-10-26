class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for i in nums:
            try:
                count[i]+=1
            except:
                count[i]=1
        return(max(count,key=lambda x:count[x]))