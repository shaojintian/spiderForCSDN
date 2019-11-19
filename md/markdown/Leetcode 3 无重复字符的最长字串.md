![在这里插入图片描述](https://img-blog.csdnimg.cn/20190404003712354.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans=0,left=-1;
        //（元素，位置）
        map<int,int> m;
        for(int i=0;i<s.size();++i)
        {	//维护一个滑动窗口，【left】【窗口】，left不属于窗口，紧挨窗口最左侧
            if(m.count(s[i]) && (m[s[i]] > left))
            {	
                left=m[s[i]];
            }
            
            m[s[i]] = i;
            
		//更新ans
            ans=max(ans,i-left);
            
        }
        
        return ans;
    }
};

```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190404012556482.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
