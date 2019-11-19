
![在这里插入图片描述](https://img-blog.csdnimg.cn/2019040811124447.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
方法一：暴力遍历
```cpp
//cpp
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        if(nums.size() < 3 ) return 0;
        int gap=INT_MAX;
        int ans=0;
        for(int i=0;i<nums.size()-2;++i)
        {
            if(i>0 && nums[i]==nums[i-1]) continue;
            
            int j=i+1,k=nums.size()-1;
            while(j<k)
            {   int now = nums[i]+nums[k]+nums[j] ;
                if(now == target) return target;
                else if(abs(now -target) < gap)
                {
                    gap=abs(now -target) ;
                    ans=now;
                }
                if(now > target ) --k;
                else ++j;
            }
            
            
            
        }
        
        return ans;
        
    }
};
```


固定一个数字，双指针，左右逼近，定一个gap为目前距离target的最小距离
更新gap到最小即为最接近的数字。

![!\[](https://img-blog.csdnimg.cn/20190408112715354.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)在这里插入图片描述](https://img-blog.csdnimg.cn/20190408111100285.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
