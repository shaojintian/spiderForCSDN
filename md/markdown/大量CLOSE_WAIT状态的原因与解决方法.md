原因：

## **Server端在某些异常情况时，没有关闭Socket。**

TCP套接字中
被动关闭的server端在接受到FIN后立即返回一个ACK报文，进入CLOSE_WAIT状态。
**应用程序层面**来看，会是抛出一个SOCKET.ERROR。
抛出ERROR之后如果没有closesocket(),则会处于CLOSE_WAIT


