class Solution {
public:
    void sortColors(vector<int>& nums) {
        // Insertion Sort
        int n=size(nums);
        for (int i=1;i<n;i++){
            for (int j=i;j>0;j--){
            if (nums[j]<nums[j-1]){
                std::swap(nums[j],nums[j-1]);
            }}
        }


    }
};