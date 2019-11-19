
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190408170718909.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

```cpp
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
       
        vector<vector<int>> ans;
        
        if(nums.size() <4) return {};
        sort(nums.begin(),nums.end());//find consistent duplications
        
        
        
        for(int i=0;i<nums.size()-3;i++)
        {
            if(nums[i] > target && nums[i] >0) break;
            
            if(i>0 && nums[i]==nums[i-1] ) continue;
            
            int fixed = target - nums[i];
            
            for(int j=i+1;j<nums.size()-2;j++)
            {   //no duplications
                if(j > i+1 &&  nums[j] == nums[j-1])continue;  
                int k=j+1,l=nums.size()-1;
                while(k<l)
                {
                    int tmp = nums[j]+nums[k]+nums[l];
                    if(tmp == fixed)
                    {
                        ans.push_back({nums[i],nums[j],nums[k],nums[l]});
                        
                        while(k<l && nums[k]==nums[k+1]) ++k;
                        while(k<l && nums[l]==nums[l-1]) --l;
                        --l;
                        ++k;
                        
                    }else if(tmp > fixed ) --l;
                    else ++k;
                    
                    
                    
                    
                    
                }
            }
            
        }
        
        
        return ans;
    }
};
```
4sum  和3sum原理一致

都是（n-2）层循环+双指针

注意每层循环都要比较是否fixed的数字有重复，有重复就continue
eg：==“if(j > i+1 &&  nums[j] == nums[j-1])continue;  ”==
int j=i-1;
j>i+1 是因为第1个j没有 j-1，第一个数字没有前一位数。
