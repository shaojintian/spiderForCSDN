![在这里插入图片描述](https://img-blog.csdnimg.cn/20190408113225750.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
首先你不知道有多少位数，因此用循环不知道嵌套多少层，那么就不能使用循环嵌套！
第一种：recursion
```cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) 
    {
        vector<string> v;
        if(digits.empty()) return v;
        string tmp[]= {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        
        int index = 0;
        string str = "";
        recursive(digits,index,tmp,v,str);
        
        
        
        return v;
    }
    
    void recursive (string digits,int charsSize, string tmp[] ,vector<string> &v,string str)
        {   
            if(charsSize == digits.size())
            { 
                v.push_back(str);
                return;
            }
            string num2chars = tmp[digits[charsSize]-'0'];//abc  ,def
            for(int i=0;i<num2chars.size();++i)
            {
                recursive(digits,charsSize+1,tmp,v,str+string(1,num2chars[i]));
            }
        }
    
};
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190408142025520.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
第二种：入队列出队列

```cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> ans;
        if(digits.empty()) return ans;
        
        string tmp[]= {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        
        queue<string> que;
        que.push("");
        
        for(int i=0;i<digits.size();++i)
        {
            string str = tmp[digits[i]-'0'];//,abc,pqrs
            
            int queLength=que.size();
            for(int k=0;k<queLength;k++)
            {
                string now = que.front();
                que.pop();
                for(int j=0;j<str.size();j++)
                {
                    que.push(now+str[j]);
                }
            }
            
            
            
        }//1X3,3X3.......
        while(!que.empty())
        {
            ans.push_back(que.front());
            que.pop();
        }
        
        return ans;
        
        
    }
};
```

