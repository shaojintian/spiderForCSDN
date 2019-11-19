
# **一：pytorch基础**

1：张量：Tensor
	定义为：多维度的矩阵。
	例如：
	
	0维度：点；    一维：向量；    二维：普通矩阵
	
	有torch.FloatTensor ;  torch.DoubleTensor; torch.IntTrnsor;


2:变量：Variable
	![在这里插入图片描述](https://img-blog.csdnimg.cn/2018112209372062.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

3：模组 torch.nn.Module
	

```python
import torch as t
from torch import nn

class net_name(nn.Module):#模型
	def __int__(self,other_arguments):
		super(net_name,self).__int__()
		self.conv1=nn.Conv2d(in_channels,out_channels,kernel_size)#训练器

	def forward(self,x):
		x=self.conv1(x)
		return x
#loss function
criterion=nn.CrossEntropyLoss()
loss=criterion(output,target)

```



## 二：多形式回归
==**1）理论简介**==

对于一般的线性回归模型，由于该函数拟合出来的是一条直线，所以精度欠佳，我们可以考虑多项式回归来拟			合更多的模型。所谓多项式回归，其本质也是线性回归。也就是说，我们采取的方法是，提高每个属性的次数来增加维度数。比如，请看下面这样的例子：

如果我们想要拟合方程：



对于输入变量和输出值，我们只需要增加其平方项、三次方项系数即可。所以，我们可以设置如下参数方程：



可以看到，上述方程与线性回归方程并没有本质区别。所以我们可以采用线性回归的方式来进行多项式的拟合。下面请看代码部分。

==2）代码实现==

```python
import torch as t
from torch import nn
import matplotlib.pyplot as plt
import numpy 
from torch.autograd import Variable

def make_features(x):
	
	x=x.unsqueeze(1)# n -> nx1 
	
	return t.cat([x ** i for i in range(1,4)],1) #nx1-->nx3
	#columns --> x,x^2,x^3
	



	#true fx
def f(x):

	return x.mm(W_target)+b_target[0] # nx1 


#建立（x,f(X)) pairs
def get_batch(batch_size=32):
	random=t.randn(batch_size)
	# 32个 == 1x32
	random=t.from_numpy(numpy.sort(random))
	x=make_features(random) #x-->nx3

	y=f(x) #nx1

	return Variable(x),Variable(y)

#Define model
class multi_linear_model(nn.Module):
	def __init__(self):
		super(multi_linear_model,self).__init__()
		self.poly=nn.Linear(3,1) #x 三维 y一维
	
	def forward(self,x):
		out=self.poly(x)
		return out #nx1 prediction y


if __name__ == '__main__':
	# true parameter
	W_target=t.FloatTensor([0.5,3,2.4]).unsqueeze(1)# 3->3x1
	b_target=t.FloatTensor([0.9])
	

	model =multi_linear_model()

	# 定义loss function --> mean square error
	criterion=nn.MSELoss()

	#优化器->随机梯度下降 learning rate 0.001
	optimizer=t.optim.SGD(model.parameters(),lr=1e-3)

	epoch=0 # 记录从开始到达模型最优化的训练次数
	
	while True:
		# Get true data
		batch_x,batch_y=get_batch()
		#out -> predict y
		output=model.forward(batch_x)

		#require loss
		loss=criterion(output,batch_y)

		print_loss=loss.item()


		#清0 梯度 
		optimizer.zero_grad()
	
		#反向传播->计算此时的x的梯度
		loss.backward()


		#梯度下降
		optimizer.step()
		epoch+=1

		#达到最优
		if print_loss<1e-3:#0.001
			break;
	predict = model(batch_x)
	x = batch_x.numpy()[:, 0]
	plt.plot(x, batch_y.numpy(), 'rx')

	predict = predict.data.numpy()
	plt.plot(x, predict, 'b')
	plt.show()





	
	













```

![多项式回归](https://img-blog.csdnimg.cn/20181122093738257.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

结果发现拟合的很好，损失小于0.001.
