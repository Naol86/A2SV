class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set<int> temp(nums.begin(),nums.end());
        vector<int> temp2(temp.begin(),temp.end());
        nums.swap(temp2);
        nums.shrink_to_fit();
        return nums.size();
    }
};