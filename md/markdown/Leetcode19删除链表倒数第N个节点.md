![在这里插入图片描述](https://img-blog.csdnimg.cn/20190408171315256.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
1:扫描两次

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
            if(head == NULL || head->next ==NULL) return NULL;
            
            ListNode *node = head;
            int size=1;
            while(node != NULL && node->next != NULL){
                node=node->next;
                ++size;
                
            }
            if(n==size) return head->next;
            node=head;
            for(int i=0 ; i<size-n-1;++i)
            {
                node=node->next;
            }
            
            node->next=node->next->next;
        
            return head;
    }
};
```
 * [x] 先记录总共有多少个节点为size个
 * [x] 随后找到倒数第n个然后删掉

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190408173511470.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
2：扫描一次,双指针，创建一个pre——head节点指向head，
倒数第N个之前的那个数字和最后一个数字规律两个相差n步，则和最后一个的next相差n+1步数。
找到规律以后往前推，创建快慢指针相差n+1步。
当快的为NULL时，则慢指针的NEXT为所要删掉的节点。

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head==NULL ||head->next==NULL ) return NULL;
        ListNode *pre_head =new ListNode(-1);
        pre_head->next =head;
        
        ListNode *p = head;
        ListNode *q =pre_head;
        for(int i=0;i<n;i++){
            p=p->next;
        }
        while(p != NULL)
        {
            p=p->next;
            q=q->next;
        }
        
        q->next=q->next->next;
        
        return pre_head->next;
        
        
    }
};
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190408180901360.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
