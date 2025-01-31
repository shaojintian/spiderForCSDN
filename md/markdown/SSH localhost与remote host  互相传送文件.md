<div id="content_views" class="markdown_views">
							<!-- flowchart 箭头图标 勿删 -->
							<svg xmlns="http://www.w3.org/2000/svg" style="display: none;"><path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path></svg>
							<ul>
<li><p>安装 SSH(Secure Shell) 服务以提供远程管理服务 <br>
<code>sudo apt-get install ssh</code></p></li>
<li><p>SSH 远程登入 Ubuntu 机 <br>
<code>$ssh username@192.168.0.1</code></p></li>
<li><p>将 文件/文件夹 从远程 Ubuntu 机拷至本地(scp) <br>
<code>$scp -r username@192.168.0.1:/home/username/remotefile.txt</code></p></li>
<li><p>将 文件/文件夹 从本地拷至远程 Ubuntu 机(scp) <br>
<code>$scp -r localfile.txt username@192.168.0.1:/home/username/</code></p></li>
<li><p>将 文件/文件夹 从远程 Ubuntu 机拷至本地(rsync)</p></li>
</ul>



<pre class="prettyprint" name="code"><code class="hljs ruby has-numbering" onclick="mdcp.copyCode(event)">rsync -v -u -a --delete --rsh=ssh --stats username<span class="hljs-variable">@192</span>.<span class="hljs-number">168.0</span>.<span class="hljs-number">1</span><span class="hljs-symbol">:/home/username/remotefile</span>.txt .<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<ul>
<li>将 文件/文件夹 从本地拷至远程 Ubuntu 机(rsync)</li>
</ul>

<pre class="prettyprint" name="code"><code class="hljs ruby has-numbering" onclick="mdcp.copyCode(event)">rsync -v -u -a --delete --rsh=ssh --stats localfile.txt username<span class="hljs-variable">@192</span>.<span class="hljs-number">168.0</span>.<span class="hljs-number">1</span><span class="hljs-symbol">:/home/username/</span><div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<p>在 Windows 机上用 SSH 远程登录 Ubuntu 机</p>

<p>下载 <a href="http://www.putty.org/" rel="nofollow" target="_blank">PuTTY</a></p>

<p>如何在 Windows 机上拷贝 文件/文件夹 从/到 远程 Ubuntu 机</p>

<p>下载 <a href="https://filezilla-project.org/" rel="nofollow" target="_blank">FileZilla</a></p>

<p>ssh -X guoshuang@192.168.100.4</p>

<p>支持 SSH 图形界面。也就是说，gedit 打开和另存都是在服务器端操作的。nautilus 打开服务器端的文件管理器。这下就比只用命令行方便多了。不知道 windows 下的 putty 支持不。</p>

<p>ssh -X guoshuang@192.168.100.4 ls</p>

<p>直接在服务器端执行 ls 返回结果到客户端</p>

<p>如何限制通过SSH远程连接的用户帐号</p>

<p>如，假如你启用了SSH服务，那么任何有有效帐号的用户都可以远程连接。这可能会导致一些安全问题，由于有一些远程密码破解工具可以尝试常见的用户名／密码</p>

<p>备份SSH服务的配置文件</p>

<p>sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.ORIGINAL</p>

<p>编辑配置文件</p>

<p>sudo gedit /etc/ssh/sshd_config</p>

<ul>
<li>将参数 PermitRootLogin 由 yes 更改为 no。 超级用户不能直接通过远程联机。</li>
<li>添加参数 AllowUsers 设定远程连接的用户名 (用空格来分割) 。</li>
<li>您也可以使用 DenyUsers for fine-grained selection of users.</li>
<li>If you enable the openssh server and you have no intention for now to enable remote connections, you may add AllowUsers nosuchuserhere to disable anyone connecting.</li>
</ul>

<p>SSH 命令</p>

<p>ssh 命令可以用来在远程机器上不经 shell 提示登录而执行命令。它的语法格式是： ssh hostname command。譬如，如果你想在远程主机 penguin.example.net 上执行 ls /usr/share/doc 命令，在 shell 提示下键入下面的命令：</p>

<p>ssh penguin.example.net ls /usr/share/doc</p>

<p>3.2. 使用 scp 命令</p>

<p>　　scp 命令可以用来通过安全、加密的连接在机器间传输文件。它与 rcp 相似。</p>

<p>　　把本地文件传输给远程系统的一般语法是：</p>

<p>　　scp localfile username@tohostname:/newfilename</p>

<p>　　localfile 指定源文件，username@tohostname:/newfilename 指定目标文件。</p>

<p>　　要把本地文件 shadowman 传送到你在 penguin.example.net 上的账号内，在 shell 提示下键入(把 username 替换成你的用户名)：</p>

<p>　　scp shadowman username@penguin.example.net:/home/username</p>

<p>　　这会把本地文件 shadowman 传输给 penguin.example.net 上的 /home/username/shadowman 文件。</p>

<p>　　把远程文件传输给本地系统的一般语法是：</p>

<p>　　scp username@tohostname:/remotefile /newlocalfile</p>

<p>　　remotefile 指定源文件，newlocalfile 指定目标文件。</p>

<p>　　源文件可以由多个文件组成。譬如，要把目录 /downloads 的内容传输到远程机器 penguin.example.net 上现存的 uploads 目录，在 shell 提示下键入下列命令：</p>

<p>　　scp /downloads/* username@penguin.example.net:/uploads/</p>

<p>　　3.3. 使用 sftp 命令</p>

<p>　 　sftp 工具可以用来打开一次安全互动的 FTP 会话。它与 ftp 相似，只不过，它使用安全、加密的连接。它的一般语法是：sftp username@hostname.com。一旦通过 验证，你可以使用一组和使用 FTP 相似的命令。请参阅 sftp 的说明书页(man)来获取这些 命令的列表。要阅读说明书页，在 shell 提示下执行 man sftp 命令。sftp 工具只在 OpenSSH 版本 2.5.0p1 以上才有。</p>

<p>SSH 概念</p>

<p>SSH是指Secure Shell，SSH协议族由IETF（Internet Engineering Task Force）的Network Working Group制定，SSH协议的内容SSH协议是建立在应用层和传输层基础上的安全协议。</p>

<p>传 统的网络服务程序，如FTP、Pop和Telnet其本质上都是不安全的；因为它们在网络上用明文传送数据、用户帐号和用户口令，很容易受到中间人 （man-in-the-middle）攻击方式的攻击。就是存在另一个人或者一台机器冒充真正的服务器接收用户传给服务器的数据，然后再冒充用户把数据 传给真正的服务器。</p>

<p>SSH(Secure Shell)是目前比较可靠的为远程登录会话和其他网络服务提供安全性的协议。利用SSH协议可以有效防止远程管理过程中的信息泄露问题。通过SSH，可以把所有传输的数据进行加密，也能够防止DNS欺骗和IP欺骗。 <br>
SSH，还有一个额外的好处就是传输的数据是经过压缩的，所以可以加快传输的速度。SSH有很多功能，它既可以代替Telnet，又可以为FTP、Pop、甚至为PPP提供一个安全的”通道”。</p>            </div>
