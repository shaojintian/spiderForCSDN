
DP

状态转移方程：


m(i,j) = max(m[i][j] = m[i - 1][j] , m[i - 1][j - weight[i]] + value[i])    (weight[i] <= j)
m(i,j)=m[i-1][j] (weight[i] > j)




```cpp
#include <iostream>
#define V 500
using namespace std;
int weight[20 + 1];
int value[20 + 1];
int f[20 + 1][V + 1];
int main() {
    int n, m;
    cout << "请输入物品个数:";
    cin >> n;
    cout << "请分别输入" << n << "个物品的重量和价值:" << endl; 
    for (int i = 1; i <= n; i++) {
        cin >> weight[i] >> value[i];
    }
    cout << "请输入背包容量:";
    cin >> m;//i==前i个包，1，2，3，····，i.     j=bag capacity 
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (weight[i] > j) {
                f[i][j] = f[i - 1][j];
            }
            else {
                f[i][j] = max(f[i - 1][j] ,f[i - 1][j - weight[i]] + value[i]);//f[1][1] = 5;f[1][2]= 5 , f[1][5] =5
                //f[2][1] = f[1][1] =5 ; 
        }
    }    
    cout << "背包能放的最大价值为:" << f[n][m] << endl;
}
```

