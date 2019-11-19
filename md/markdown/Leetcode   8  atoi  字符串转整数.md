
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190406205448509.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

```cpp
class Solution {
public:
    int myAtoi(string str) {
        int size =str.size();
        long ans=0;
        int i=0 ,j=0;
        while(str[i] == ' ')
        {
            i++;
        }
    
        if((str[i]<'0' || str[i] > '9') && str[i] != '+' && str[i] != '-'  ){
            
            return 0;
        }
        
        bool flag = true;
        
        if(str[i]=='-')
        {
            flag=false;
            i++;
        }else if(str[i]== '+')
        {
            i++;
        }
        
        while(str[i]>='0' && str[i] <='9' && i <size)
        {
            int tmp = str[i] - '0';
            if((ans*10 + tmp) > INT_MAX ) {
                if(flag) return INT_MAX;
                else return INT_MIN;
            }
            ans=ans*10+tmp;
            i++;
        }
        
        if(!flag)
        {
            ans*=-1;
        }
            
            
            
            
            
            
        return ans;
    }
};
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190406205436655.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
