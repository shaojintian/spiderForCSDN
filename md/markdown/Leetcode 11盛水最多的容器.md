![在这里插入图片描述](https://img-blog.csdnimg.cn/20190407025819200.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
解法一：暴力法
```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        
        int max=0;
        
        for(int i =0; i< height.size()-1;i++)
        {
            
           for(int j = i+1 ;j<height.size();++j)
           {
               int minOfTwo=height[i]<height[j] ? height[i] : height[j];
               
               int tem=minOfTwo * (j-i);
               if(max<tem) max = tem;
               
           }
            
        }
        
        return max;
        
    }
};
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190407032113963.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

2：解法2----贪心

双指针移动----->左右双指针，减少的距离换更长的长度

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        
        int ans=0,i=0,j=height.size()-1;
        
        while(i<j)
        {   int tmp = min(height[i],height[j]) * (j-i);
            ans = max(ans,tmp);
            
            if( height[i] < height[j])
                i++;
            else j--;
            
        }
        
        return ans;
        
    }
};
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190407033652832.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
