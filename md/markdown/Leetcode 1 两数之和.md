
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int ,int> m;
        //(元素，位置)
        for(int i=0;i<nums.size();++i)
        {
            if(m.count(target-nums[i]))
            {
                
                return {i , m[target - nums[i]]};
            }
            //放后面避免同一元素计算两次如【3，2】target =6
            m[nums[i]]=i;
        }
        
        return {};
        
        
    }
};
```

map基于红黑树，查找为O（logn）
