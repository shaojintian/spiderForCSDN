
**simulate  shell command "ps aux  | grep  QQ"**

进程间通信（即IPC问题）是并发中最关键，重要的问题。

基本有三个大的解决方式

1：基于通信

 - 管道pipe
 - 消息队列 message queue


2：基于信号（唯一的异步I/O）

- 信号 signal



3:  基于同步

 - 信号量 semaphore


现在介绍一种最简单的方式 ： **管道**

eg：shell 中    “ |”    就是一个管道符

管道符是一种半双工的通信方式 ， 即一个进程的输出作为另一个进程的输入

管道符的实现如下
```go

//copyright by sjt@hnu.edu.cn
package main

// simulate  shell command "ps aux  | grep  QQ"
import (
	"bytes"
	"fmt"
	"log"
	"os/exec"



)



func main(){

	cmd1 := exec.Command("ps","aux")
	cmd2 := exec.Command("grep","QQ")


	var outbuf1   bytes.Buffer

	cmd1.Stdout = &outbuf1

	if err := cmd1.Start() ; err != nil {
		log.Fatalln("Error : cmd1 start err ",err)
	}

	if err := cmd1.Wait(); err != nil {
		log.Fatalln("Error : cmd1 can not wait",err)
	}


	var outbuf2  bytes.Buffer

	cmd2.Stdin = &outbuf1

	cmd2.Stdout = &outbuf2

	if err := cmd2.Start() ; err != nil {
		log.Fatalln("Error : cmd2 start err ",err)
	}

	if err := cmd2.Wait(); err != nil {
		log.Fatalln("Error : cmd2 can not wait",err)
	}


	fmt.Println(outbuf2.String())



}

```

os/exec  是go的标准i/o包
代码中
第39行和第41行

	cmd2.Stdin = &outbuf1

	cmd2.Stdout = &outbuf2

表明了cmd1的输出作为cmd2的输入实现管道符的功能

最后一行

	fmt.Println(outbuf2.String())
	转换为string类型显示在终端shell中

结果如下：完全模拟了ps aux | grep  QQ   的shell 命令
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190610200317844.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
