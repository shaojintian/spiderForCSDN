
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190404003529978.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)


```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
       
      int v1 =0 , v2 = 0,sum=0,carry=0;  
        
        ListNode* ans = new ListNode(-1);
        
        ListNode* now =ans;
        
     while( l1 || l2) {
         
         v1 = l1 ? l1->val : 0;
         v2 = l2 ? l2->val : 0;
         
         sum=v1+v2+carry;
         //更新 carry
         carry=0;
         
         if(sum >=10)  
         {
             sum-=10;
             carry=1;
             
         }
         
         now->next = new ListNode(sum);
         
         now = now->next;
         
         if(l1 != NULL)  l1=l1->next;
         if(l2 != NULL)  l2=l2->next;
     }
        //如果此时carry==1，说明还需要往前进一位
        if(carry) now->next = new ListNode(1);
        return ans->next;
        
        
    }
};
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190404003551848.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

创建一个新链表(-1->null)

carry为标识位表示进制是否加1
