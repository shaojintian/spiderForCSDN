![在这里插入图片描述](https://img-blog.csdnimg.cn/20190407042008244.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

```cpp
//C++
class Solution {
public:
    int romanToInt(string s) {
       
        map<char,int> m{{'M',1000},{'D',500},{'C',100},{'L',50},{'X',10},{ 'V',5 },{'I',1}};
        
        int ans =0 ,j=0;
        for(int i=0;i<s.size();i++)
        {
            if(i<s.size()-1 && m[s[i]] < m[s[i+1]])
            {
                ans-=m[s[i]];
            }else{
                ans+=m[s[i]];
            }
        }
        
        return ans;
        
    }
};
```
从左往右遍历字符串，比较前后，如果小的话就先减再加
eg：IV  ----->   4  ------> -1 +5 

这样就可以避免“IV”整体匹配了

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190407045704705.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
