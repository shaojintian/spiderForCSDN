![在这里插入图片描述](https://img-blog.csdnimg.cn/20190407050437880.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

```cpp
//C++
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string str = "";
        
        if(strs.empty())return "";
        
        if(strs.size()==1) return strs[0];
        
        int j=0 ,i=0,min_len=strs[j].size();
        
        for(j=1;j<strs.size();j++)
        {
            if(strs[j].size() < min_len)min_len=strs[j].size();
        }
        
        
        
        
        for(j=0;j<min_len;j++)
        {   
           for(i=0;i<strs.size()-1;i++)
           {
               if(strs[i][j] != strs[i+1][j])
                   return str;
               if(i==strs.size()-2)
                   str+=strs[0][j];
           }
            
        }
            
            
        
        
        
        
        return str;
    }
};
```



![在这里插入图片描述](https://img-blog.csdnimg.cn/20190407055027495.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
