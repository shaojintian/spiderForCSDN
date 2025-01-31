
<h2><a name="t0"></a>一、注意力机制回顾</h2>

<p>简单来说，注意力本质上就是一个经过softmax层输出的向量。</p>

<p>在早期机器翻译应用中，神经网络结构一般如下图，是一个RNN的Encoder-Decoder模型。左边是Encoder，代表输入的sentence。右边代表Decoder，是根据输入sentence对应的翻译。Encoder会通过RNN将最后一个step的隐藏状态向量c作为输出，Deocder利用向量c进行翻译。这样做有一个缺点，翻译时过分依赖于这个将整个sentence压缩成固定输入的向量。输入的sentence有可能包含上百个单词，这么做不可避免会造成信息的丢失，翻译结果也无法准确了。</p>

<p style="text-align:center;"><img alt="" class="has" height="328" src="https://img-blog.csdn.net/20181011165935693?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA5NjAxNTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="716"></p>

<p>注意力机制的引入就是为了解决此问题，注意力机制使得机器翻译中利用原始的sentence信息，减少信息损失。在解码层，生成每个时刻的y，都会利用到x1,x2,x3....，而不再仅仅利用最后时刻的隐藏状态向量。同时注意力机制还能使翻译器zoom in or out（使用局部或全局信息）。</p>

<p>注意力机制听起来很高大上、很神秘，其实它的整个实现只需要一些参数和简单的数学运算。那么注意力机制到底是如何实现的呢？</p>

<p style="text-align:center;"><img alt="" class="has" src="https://img-blog.csdnimg.cn/20190215104836321.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA5NjAxNTU=,size_16,color_FFFFFF,t_70"></p>

<p>在基本的Encoder-Decoder模型中，注意力机制在Encoder和Decoder加入了上下文向量context vector，如上图所示，左边蓝色的代表Encoder，红色的代表Decoder。对于Decoder中每个要生成的y，都会生成一个上下文向量。这个上下文向量是由每个输入的words的信息加权求和得到的，其中权重向量就是注意力向量，它代表在此刻生成y时输入的单词的重要程度。最后将上下文向量和此刻的y的信息进行融合作为输出。</p>

<p>构建上下文向量过程也很简单，首先对于一个固定的target word，我们把这个target state跟所有的Encoder的state进行比较，这样对每个state得到了一个score;然后使用softmax对这些score进行归一化，这样就得到了基于target state的条件概率分布。最后，对source的state进行加权求和，得到上下文向量，将上下文向量与target state融合作为最终的输出。</p>

<p>具体流程的数学表达如下：</p>

<p style="text-align:center;"><img alt="" class="has" height="156" src="https://img-blog.csdnimg.cn/2019021510501288.JPG" width="579"></p>

<p>为了理解这个看起来有些复杂的数学公式，我们需要记住三点：</p>

<ol><li>在解码时，对于每个输出的word都需要计算上下文向量。所以，我们会得到一个<img alt="n\ast m" class="mathcode" src="https://private.codecogs.com/gif.latex?n%5Cast%20m">的2D矩阵，&nbsp;<img alt="n" class="mathcode" src="https://private.codecogs.com/gif.latex?n">代表source word数量，<img alt="m" class="mathcode" src="https://private.codecogs.com/gif.latex?m">代表target word数量</li>
	<li>我们可以通过context vector,target word,attention function&nbsp;<img alt="f" class="mathcode" src="https://private.codecogs.com/gif.latex?f">计算attention vevtor</li>
	<li>attention mechanism是可以训练的。</li>
</ol><h2><a name="t1"></a>二、BahdanauAttention与LuongAttention</h2>

<h3><a name="t2"></a>2.1&nbsp;BahdanauAttention</h3>

<p>BahdanauAttention是Bahdanau在论文<a href="https://arxiv.org/pdf/1409.0473.pdf" rel="nofollow" target="_blank">NEURAL MACHINE TRANSLATION BY JOINTLY LEARNING TO ALIGN AND TRANSLATE</a>中提出的，整体Attention结构如下图：</p>

<p style="text-align:center;"><img alt="" class="has" height="492" src="https://img-blog.csdn.net/20180926170405403?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA5NjAxNTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="292"></p>

<p>1）第<img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i">个target word上下文向量<img alt="c_i{}" class="mathcode" src="https://private.codecogs.com/gif.latex?c_i%7B%7D">会根据每个source word的隐向量<img alt="h_j{}" class="mathcode" src="https://private.codecogs.com/gif.latex?h_j%7B%7D">加权求和得到：</p>

<p><img alt="" class="has" height="77" src="https://img-blog.csdn.net/2018092617125253?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA5NjAxNTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="149"></p>

<p>2）对于每个&nbsp;<img alt="h_j{}" class="mathcode" src="https://private.codecogs.com/gif.latex?h_j%7B%7D">的<img alt="a_{ij}" class="mathcode" src="https://private.codecogs.com/gif.latex?a_%7Bij%7D">计算如下</p>

<p><img alt="" class="has" height="106" src="https://img-blog.csdn.net/20180926171933731?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA5NjAxNTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="293"></p>

<p>其中</p>

<p><img alt="" class="has" height="57" src="https://img-blog.csdn.net/20180926172008662?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA5NjAxNTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="217"></p>

<p><img alt="e_{ij}" class="mathcode" src="https://private.codecogs.com/gif.latex?e_%7Bij%7D">是对齐模型，代表位置<img alt="j" class="mathcode" src="https://private.codecogs.com/gif.latex?j">的输入和位置<img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i">的输出匹配程度的分数，这个分数基于RNN的 i-1 位置的隐含状态<img alt="s_{i-1}" class="mathcode" src="https://private.codecogs.com/gif.latex?s_%7Bi-1%7D">和 j 位置的<img alt="h_{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?h_%7Bj%7D">计算得到。</p>

<h3><a name="t3"></a>2.2&nbsp;LuongAttention</h3>

<p>LuongAttention是Luong在论文<a href="https://arxiv.org/pdf/1508.04025.pdf" rel="nofollow" target="_blank">Effective Approaches to Attention-based Neural Machine Translation</a>中提出的。整体结构如下</p>

<p style="text-align:center;"><img alt="" class="has" height="386" src="https://img-blog.csdn.net/20180926173621689?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA5NjAxNTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="428"></p>

<p>&nbsp;与BahdanauAttention整体结构类似，LuongAttention对原结构进行了一些调整，其中Attention向量计算方法如下</p>

<p><img alt="" class="has" height="117" src="https://img-blog.csdn.net/20180926174909188?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA5NjAxNTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="333"></p>

<p>&nbsp;其中与BahdanauAttention机制有以下几点改进：</p>

<ol><li>BahdanauAttention对Encoder和Decoder的双向的RNN的state拼接起来作为输出，LuongAttention仅使用最上层的RNN输出</li>
	<li>BahdanauAttention的计算流程为 ht−1 → at → ct → ht，它使用前一个位置t-1的state计算t时刻的ht。LuongAttention计算流程为&nbsp; ht → at → ct → h˜t 使用t位置的state当前位置的ht</li>
	<li>BahdanauAttention只在concat对齐函数上进行了实验，LuongAttention在多种对齐函数进行了实验，下图为LuongAttention设计的三种对齐函数</li>
</ol><p style="text-align:center;"><img alt="" class="has" height="137" src="https://img-blog.csdn.net/20180926191629666?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA5NjAxNTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" width="475"></p>

<h3><a name="t4"></a>2.3 总结&nbsp;</h3>

<p>BahdanauAttention与LuongAttention两种注意力机制大体结构类似，都是基于第一节中的attention框架设计，主要的不同点就是在对齐函数上，在计算第 <img alt="i" class="mathcode" src="https://private.codecogs.com/gif.latex?i">个位置的score，前者是需要使用&nbsp;<img alt="s_{i-1}" class="mathcode" src="https://private.codecogs.com/gif.latex?s_%7Bi-1%7D">和<img alt="h_{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?h_%7Bj%7D">&nbsp;来进行计算，后者使用<img alt="s_{i}" class="mathcode" src="https://private.codecogs.com/gif.latex?s_%7Bi%7D">和<img alt="h_{j}" class="mathcode" src="https://private.codecogs.com/gif.latex?h_%7Bj%7D">计算，这么来看还是后者直观上更合理些，逻辑上也更顺滑。两种机制在不同任务上的性能貌似差距也不是很大，具体的细节还待进一步做实验比较。</p>            </div>
                      </div>
	</article>
</div>
