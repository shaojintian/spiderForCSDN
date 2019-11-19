![在这里插入图片描述](https://img-blog.csdnimg.cn/20190404012715887.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

```cpp
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        vector<int > ans;
        
        ans.insert(ans.end(),nums1.begin(),nums1.end());
        ans.insert(ans.end(),nums2.begin(),nums2.end());
        
        sort(ans.begin(),ans.end());
        
        
        int size = ans.size();
        
        double res;
        if(size %2 ==0 )
        {
            res=(ans[size/2]+ans[size/2-1])/2.0;
        }else{
            
            res=ans[size/2];
        }
        
        return res;
        
    }
};
```

取了巧合而已，看一下C++sort（）源码。。。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190404020008240.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
