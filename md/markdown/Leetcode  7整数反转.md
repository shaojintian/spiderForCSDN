![在这里插入图片描述](https://img-blog.csdnimg.cn/20190406200617644.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

```cpp
class Solution {
public:
    int reverse(int x) {
        //only < 10
        if(x/10 == 0) return x;
        bool flag=true;
        long xx=x;
        if(x<0)
        {   
            xx*=-1;
            flag=false;
        }
        long ans =0 ;
        
        while(xx != 0 )
        {   if(ans*10+xx%10 > INT_MAX) return 0;
            ans=ans*10+xx%10;
            xx=xx/10;
            
        }
        
        
        if(!flag)
        {
           ans=ans*(-1); 
        }
        
        
        return ans;
    }
};
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190406200600678.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

range int [-2^31     ,   2^31 -1]

like reverse  -2^31   --------> 2^31   ,that doesn't work  .

so we need to use ==long== to store x


INT_MAX  --->2^31 -1



