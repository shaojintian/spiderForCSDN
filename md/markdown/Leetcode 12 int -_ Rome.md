![在这里插入图片描述](https://img-blog.csdnimg.cn/20190407033756773.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

```cpp
class Solution {
public:
    string intToRoman(int num) {
       string str = "";
       vector<int> number{1000,900,500,400,100,90,50,40,10,9,5,4,1};
       vector<string> rome{"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        
        for(int i=0;i<number.size();i++)
        {
            while(num >= number[i] ){
                num-=number[i];
                str+=rome[i];
                
            }
            
            if(num == 0)break;
        }
        
        return str;
        
    }
};
```

1:I
2:II
3:III
4:IV
5:V
6:VI
7:VII
8:VIII
9:IX
10:X
so: 5 种 I，IV，V，IX，X
各种位数均如上
从大到小遍历，如果大于某个数，就对它进行循环递减，Rome字符串递加。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190407041927386.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
