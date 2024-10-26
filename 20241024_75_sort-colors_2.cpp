class Solution {
public:
    void sortColors(vector<int>& nums) {
        // // Insertion Sort
        // int n=size(nums);
        // for (int i=1;i<n;i++){
        //     for (int j=i;j>0;j--){
        //     if (nums[j]<nums[j-1]){
        //         std::swap(nums[j],nums[j-1]);
        //     }}
        // }


        // //Quik Sort
        // int n=size(nums);
        // int small, large=0,0
        // int pivot=nums[0]
        // for (int i<)


        //Better Approach
        int c0=0;
        int c1=0;
        int c2=0;
        for (int i=0;i<size(nums);i++){
            if (nums[i]==0) c0+=1;
            if (nums[i]==1) c1+=1;
            if (nums[i]==2) c2+=1;
        }
        for (int i=0;i<c0;i++) nums[i]=0;
        for (int i=c0;i<c0+c1;i++) nums[i]=1;
        for (int i=c0+c1;i<c0+c1+c2;i++) nums[i]=2;

    }
};