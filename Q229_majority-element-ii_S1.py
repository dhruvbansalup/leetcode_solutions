class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        count={x:0 for x in set(nums)}
        for num in nums:
            count[num]+=1
        
        reqele=[x for x in count.keys() if count[x]>len(nums)/3]
        return reqele