![在这里插入图片描述](https://img-blog.csdnimg.cn/20190406183836370.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        int size = s.size();
        
        if(numRows <= 1 )
        {
            return s;
        }
        int gap = 2*numRows -2;
        
        string  new_str = "";
        
       for(int i = 0;i < numRows; i++)
       {//i == row current 
           
         for(int j=i ; j< size; j+=gap)
         {
             
             new_str+=s[j];
             
             if(i > 0 && i < numRows -1 )
             {
               int t = j + gap -2*i;
                 if( t < size)
                new_str+=s[t];
                 
             }
             
             
         }
           
       }
        
        
        return new_str;
        
    }
};
```


![在这里插入图片描述](https://img-blog.csdnimg.cn/20190406183821328.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190406183916423.png)
黑色的位置规律为 +2n-2  用 gap 表示规律，j表示当前黑色位置
i表示为当前行
红色的位置规律为  j+ gap - 2*i 

两个循环：
外循环遍历行数，内循环遍历每一行的操作。

