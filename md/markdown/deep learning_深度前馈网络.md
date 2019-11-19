深度学习是监督学习的一个分支。
简单来说就是当线性模型无法解决问题时，引入的一种方法。
它综合多种线行模型来从x空间——>学习到h空间，h空间为可用线行模型解决的空间

深度前馈网络（deep feedforward network)又叫多层感知机，是深度学习最典型的模型。
 
 引入一个例子：
 XOR异或问题
 

![在这里插入图片描述](https://img-blog.csdnimg.cn/20181108013846134.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

当 x1不变时，x2递增，输出结果的趋势相反，即出现了递增，也出现了递减。这不是线性变化的，所以无法用线性模型来分类。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181108020035803.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)
上图两个输出空间，黑；绿
引出神经网络核心思想，多线性模型一起工作。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20181108021624255.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5ODcxNDk4,size_16,color_FFFFFF,t_70)

## 接下来使用python制作自己的神经网络：

构架：
1：初始化函数：设定输入层节点，隐藏层节点和输出层节点（上图所示）
2：训练：学习给定训练集样本后，优化权重
3：查询：给定输入，从输出节点得到输出结果

```py
import numpy
# scipy.special for the sigmoid function expit()
import scipy.special

# neural network class definition
class neuralNetwork:
    
    
    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        # link weight matrices, wih and who
        # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc 
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        # learning rate
        self.lr = learningrate
        
        # activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)
        
        pass

    
    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        
        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors) 
        
        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        
        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        
        pass

    
    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        
        return final_outputs


if __name__ =="__main__":
    # number of input, hidden and output nodes
    input_nodes =2  
    hidden_nodes = 5
    output_nodes = 1

    # learning rate is 0.3
    learning_rate =  00.3
    n = neuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)
    print(n.query([1,1]))
```


