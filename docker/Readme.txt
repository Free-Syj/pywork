docker search http ����images�б�
docker pull httpd ���ذ�װhttpd
docker run httpd  ���о���
docker ps �鿴�������

���¾��� runoob@runoob:~$ docker commit -m="has update" -a="runoob" e218edb10161 runoob/ubuntu:v2 sha256:70bf1840fd7c0d2d8ef0a42a817eb29f854c1af8f7c59fc03ac7bdee9545aff8

��������˵����

	* -m:�ύ��������Ϣ

	* -a:ָ����������

	* e218edb10161������ID

	* runoob/ubuntu:v2:ָ��Ҫ������Ŀ�꾵����   REPOSITORY��TAG

	* -d ��̨����

��������
runoob@runoob:~$ docker run -t -i runoob/ubuntu:v2 /bin/bash                            
root@1a9fbdeb5da3:/#


��������
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

ÿһ��ָ����ھ����ϴ���һ���µĲ㣬ÿһ��ָ���ǰ׺�������Ǵ�д�ġ�
��һ��FROM��ָ��ʹ���ĸ�����Դ
RUN ָ�����docker �ھ�����ִ�������װ��ʲô������
Ȼ������ʹ�� Dockerfile �ļ���ͨ�� docker build ����������һ������
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

���������ñ�ǩ��
runoob@runoob:~$ docker tag 860c279d2fec runoob/centos:dev

docker tag ����ID�������� 860c279d2fec ,�û����ơ�����Դ��(repository name)���µı�ǩ��(tag)��
ʹ�� docker images ������Կ�����IDΪ860c279d2fec�ľ����һ����ǩ�� 

���о���ָ���˿ڣ�
docker run -d -p 127.0.0.1:5001:5002 training/webapp python app.py
�������ǾͿ���ͨ������127.0.0.1:5001������������5002�˿ڡ�
����������У�Ĭ�϶��ǰ� tcp �˿ڣ����Ҫ�� UPD �˿ڣ������ڶ˿ں������ /udp�� 
docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py
�鿴�˿ڰ������
docker port ������������ǿ�ݵز鿴�˿ڵİ������
docker port adoring_stonebraker 5002

Docker��������
�˿�ӳ�䲢����Ψһ�� docker ���ӵ���һ�������ķ�����
docker��һ������ϵͳ�����������������һ�𣬹���������Ϣ��
docker���ӻᴴ��һ�����ӹ�ϵ�����и��������Կ�������������Ϣ��
�������������Ǵ���һ��������ʱ��docker���Զ������������������⣬����Ҳ����ʹ��--name��ʶ���������������磺
runoob@runoob:~$  docker run -d -P --name runoob training/webapp python app.py

nginx����
docker run -p 80:80 --name mynginx -v $PWD/www:/www -v $PWD/conf/nginx.conf:/etc/nginx/nginx.conf -v $PWD/logs:/wwwlogs  -d nginx  
-v $PWD/logs:/wwwlogs���������е�ǰĿ¼�µ�logs���ص�������/wwwlogs

python ��װ��ִ�У�
docker run  -v $PWD/myapp:/usr/src/myapp  -w /usr/src/myapp python:3.5 python helloworld.py

����˵����
-v $PWD/myapp:/usr/src/myapp :�������е�ǰĿ¼�µ�myapp���ص�������/usr/src/myapp
-w /usr/src/myapp :ָ��������/usr/src/myappĿ¼Ϊ����Ŀ¼
python helloworld.py :ʹ��������python������ִ�й���Ŀ¼�е�helloworld.py�ļ� 

redis ��װ�����:
docker pull redis:3.2
mkdir data
docker run -p 6379:6379 -v $PWD/data:/data  -d redis:3.2 redis-server --appendonly yes
-p 6379:6379 :��������6379�˿�ӳ�䵽������6379�˿�
-v $PWD/data:/data :�������е�ǰĿ¼�µ�data���ص�������/data
redis-server --appendonly yes :������ִ��redis-server�����������redis�־û����� 
docker ps
docker run -it redis:3.2 redis-cli -h 172.17.0.1

jq����   �����н���json����

mongo��װ����ԣ�
docker pull mongo:3.2
mkdir db
docker run -p 27017:27017 -v $PWD/db:/data/db -d mongo:3.2
docker ps
docker run -it mongo:3.2 mongo --host 172.17.0.1
