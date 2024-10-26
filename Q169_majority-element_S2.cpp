#include<bits/stdc++.h>
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // Moore's Voting Algo
    
        // Get Possible element
        int count=0;
        int element;
        for (int i=0;i<size(nums);i++){
            if (nums[i]==element) count+=1;
            else if (nums[i]!=element & count>0) count-=1;
            else if (nums[i]!=element & count==0){
                count+=1;
                element=nums[i];
            }
        }
        if (count==0) return -1;

        //Verify the result:
        count=0;
        for (int i=0;i<size(nums);i++){
            if (nums[i]==element) count+=1;
        }
        if (count>(size(nums)/2)) return element;

        return -1;
    }
};