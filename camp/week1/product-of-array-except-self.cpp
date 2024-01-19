class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int zero=0;
        int product=1;
        vector<int> answer;
        for(int i = 0 ; i<nums.size() ; i++){
            if(nums[i]==0)
                zero++;
            else{
                product*=nums[i];
            }
        }
        if(zero!=0){
            if(zero==1){
                for(int i=0;i<nums.size();i++){
                    if(nums[i]==0)
                        answer.push_back(product);
                    else
                        answer.push_back(0);
                }
            }
            else{
                for(int i=0;i<nums.size();i++){
                    answer.push_back(0);
                }
            }
        }
        else{
            for(int i=0;i<nums.size();i++){
                answer.push_back(product/nums[i]);
            }
        }
        return answer;
    }
};