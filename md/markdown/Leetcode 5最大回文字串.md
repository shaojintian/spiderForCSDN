
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190404032343593.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)


```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        int n=s.size();
        
        if(s.size() <2 ) return s;
        
        int left=0,right=0,max_length=1,start=0;
        
        for(int i =0; i < n;)
        {
          left = i,right =i;
            
          while(right<n-1 && s[right]==s[right+1]) 
              ++right;
        
          i=right+1;
         
            
          //从中心扩展
          while(right <n-1 && left > 0 && s[left-1]==s[right+1])
          {
              --left;
              ++right;
             
          }
            
            if(max_length < right - left +1)
            {
                max_length = right - left + 1;
                start = left;
            }
        }
        
        
        
        return s.substr(start,max_length);
        
    }
};
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190404032254882.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

此为中心扩展法，自里向外搜索回文子串
