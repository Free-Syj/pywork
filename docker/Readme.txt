docker search http 搜索images列表
docker pull httpd 下载安装httpd
docker run httpd  运行镜像
docker ps 查看运行情况

更新镜像 runoob@runoob:~$ docker commit -m="has update" -a="runoob" e218edb10161 runoob/ubuntu:v2 sha256:70bf1840fd7c0d2d8ef0a42a817eb29f854c1af8f7c59fc03ac7bdee9545aff8

各个参数说明：

	* -m:提交的描述信息

	* -a:指定镜像作者

	* e218edb10161：容器ID

	* runoob/ubuntu:v2:指定要创建的目标镜像名   REPOSITORY：TAG

	* -d 后台运行

启动镜像：
runoob@runoob:~$ docker run -t -i runoob/ubuntu:v2 /bin/bash                            
root@1a9fbdeb5da3:/#


创建镜像：
runoob@runoob:~$ cat Dockerfile 
FROM    centos:6.7 
MAINTAINER      Fisher "fisher@sudops.com" 
 RUN     /bin/echo 'root:123456' |chpasswd 
RUN     useradd runoob 
RUN     /bin/echo 'runoob:123456' |chpasswd 
RUN     /bin/echo -e "LANG=\"en_US.UTF-8\"" >]]>/etc/default/local 
EXPOSE  22 
EXPOSE  80 
CMD     /usr/sbin/sshd -D

每一个指令都会在镜像上创建一个新的层，每一个指令的前缀都必须是大写的。
第一条FROM，指定使用哪个镜像源
RUN 指令告诉docker 在镜像内执行命令，安装了什么。。。
然后，我们使用 Dockerfile 文件，通过 docker build 命令来构建一个镜像。
runoob@runoob:~$ docker build -t runoob/centos:6.7 . 
Sending build context to Docker daemon 17.92 kB 
Step 1 : FROM centos:6.7 
 ---&gt; d95b5ca17cc3 
Step 2 : MAINTAINER Fisher "fisher@sudops.com" 
 ---&gt; Using cache 
 ---&gt; 0c92299c6f03 
Step 3 : RUN /bin/echo 'root:123456' |chpasswd 
 ---&gt; Using cache 
 ---&gt; 0397ce2fbd0a 
Step 4 : RUN useradd runoob ......

给镜像设置标签：
runoob@runoob:~$ docker tag 860c279d2fec runoob/centos:dev

docker tag 镜像ID，这里是 860c279d2fec ,用户名称、镜像源名(repository name)和新的标签名(tag)。
使用 docker images 命令可以看到，ID为860c279d2fec的镜像多一个标签。 

运行镜像并指定端口：
docker run -d -p 127.0.0.1:5001:5002 training/webapp python app.py
这样我们就可以通过访问127.0.0.1:5001来访问容器的5002端口。
上面的例子中，默认都是绑定 tcp 端口，如果要绑定 UPD 端口，可以在端口后面加上 /udp。 
docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py
查看端口绑定情况：
docker port 命令可以让我们快捷地查看端口的绑定情况。
docker port adoring_stonebraker 5002

Docker容器连接
端口映射并不是唯一把 docker 连接到另一个容器的方法。
docker有一个连接系统允许将多个容器连接在一起，共享连接信息。
docker连接会创建一个父子关系，其中父容器可以看到子容器的信息。
容器命名当我们创建一个容器的时候，docker会自动对它进行命名。另外，我们也可以使用--name标识来命名容器，例如：
runoob@runoob:~$  docker run -d -P --name runoob training/webapp python app.py

nginx启动
docker run -p 80:80 --name mynginx -v $PWD/www:/www -v $PWD/conf/nginx.conf:/etc/nginx/nginx.conf -v $PWD/logs:/wwwlogs  -d nginx  
-v $PWD/logs:/wwwlogs：将主机中当前目录下的logs挂载到容器的/wwwlogs

python 安装与执行：
docker run  -v $PWD/myapp:/usr/src/myapp  -w /usr/src/myapp python:3.5 python helloworld.py

命令说明：
-v $PWD/myapp:/usr/src/myapp :将主机中当前目录下的myapp挂载到容器的/usr/src/myapp
-w /usr/src/myapp :指定容器的/usr/src/myapp目录为工作目录
python helloworld.py :使用容器的python命令来执行工作目录中的helloworld.py文件 

redis 安装与测试:
docker pull redis:3.2
mkdir data
docker run -p 6379:6379 -v $PWD/data:/data  -d redis:3.2 redis-server --appendonly yes
-p 6379:6379 :将容器的6379端口映射到主机的6379端口
-v $PWD/data:/data :将主机中当前目录下的data挂载到容器的/data
redis-server --appendonly yes :在容器执行redis-server启动命令，并打开redis持久化配置 
docker ps
docker run -it redis:3.2 redis-cli -h 172.17.0.1

jq命令   命令行解析json数据

mongo安装与测试：
docker pull mongo:3.2
mkdir db
docker run -p 27017:27017 -v $PWD/db:/data/db -d mongo:3.2
docker ps
docker run -it mongo:3.2 mongo --host 172.17.0.1
