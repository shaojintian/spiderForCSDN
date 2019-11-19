![在这里插入图片描述](https://img-blog.csdnimg.cn/20190406211406181.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int sl=s.size(), pl=p.size();
        vector<vector<bool> > dp(sl+1, vector<bool>(pl+1, false));
        dp[0][0]=true;
        for(int i=0; i<=sl; i++){
            for(int j=1; j<=pl; j++){
                if(j>1 && p[j-1]=='*')
                    dp[i][j] = dp[i][j-2] 
                    || (i>0 && (p[j-2]=='.' || s[i- 1]==p[j-2])
                     && dp[i-1][j]);
                else dp[i][j] = i>0 
                && (s[i-1]==p[j-1] || p[j-1]=='.') && dp[i-1][j-1];
            }
        }
        return dp[sl][pl];
    }
};
```
dynamic programming : 
time complexity : O(n^2)

