# Django 顺序23_nginx+uwsgi部署



## 安装 nginx

查看是否安装 nginx

```python
$ apt-cache search nginx
```

 

安装 nginx

```python
$ sudo apt-get install nginx
```



安装完成后，查看进程中是否存在 nginx

```python
$ ps aux|grep nginx
```

显示以下进程即表示安装好了 nginx。root 启动的是主进程，www-data 启动的是 work 进程。

```python
root      1951  0.0  0.2  85888  1340 ?        Ss   06:53   0:00 nginx: master process /usr/sbin/nginx
www-data  1952  0.0  0.3  86228  1756 ?        S    06:53   0:00 nginx: worker process
www-data  1953  0.0  0.3  86228  1756 ?        S    06:53   0:00 nginx: worker process
www-data  1954  0.0  0.3  86228  1756 ?        S    06:53   0:00 nginx: worker process
www-data  1955  0.0  0.3  86228  1756 ?        S    06:53   0:00 nginx: worker process
vagrant   1965  0.0  0.1  10432   668 pts/0    S+   06:54   0:00 grep --color=auto nginx
```



查看 nginx 版本号

```python
$ nginx -v
nginx version: nginx/1.4.6 (Ubuntu)
```



通过 ip 地址访问 nginx，首先查到 IP 地址，然后浏览器访问。

```python
$ ifconfig
eth0      Link encap:Ethernet  HWaddr 08:00:27:7e:84:45  
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          #...
```



这时用浏览器并不能访问 `10.0.2.15`。需要在虚拟机 VirtualBox 软件中去设置端口转发。

**退出、挂起虚拟机**

```php
$ exit

$ vagrant suspend 
```



**VirtualBox中设置端口转发**

选中虚拟机 / Settings / Network / Advanced / Port Forwarding / Add new forwarding rule

- nginx, Host IP 127.0.0.1, Host Port 8888, Guest Port 80
- apache, Host IP 127.0.0.1, Host Port 8889, Guest Port 8888

**启动虚拟机**

```php
$ vagrant up
```

**进入虚拟机**

```
$ vagrant ssh
```

**浏览器测试**

```php
127.0.0.1:8888
```

即可看到 nginx 的欢迎页面。



## 安装 MySQL

**安装mysql-server**

```python
$ sudo apt-get install mysql-server
```

安装过程需要输入密码。因为是本地环境，所以三次都是回车，空密码。但是线上环境，一定要16位以上的复杂密码。



确认 mysql 进程已经启动

```python
$ ps aux|grep mysql
mysql     4415  0.2  8.8 623936 44600 ?        Ssl  07:11   0:00 /usr/sbin/mysqld
vagrant   4581  0.0  0.1  10432   668 pts/0    S+   07:12   0:00 grep --color=auto mysql
```

其中 `/usr/sbin/mysqld` 进程是 mysql-server 的进程。



测试进入 mysql

```python
$ mysql -uroot -p
```

退出 mysql

```python
$ exit
```



**mysqld 的配置**

进入 `/etc/mysql/conf.d` 目录，查找是否存在 `mysqld.cnf` 配置文件。

```python
/etc/mysql/conf.d$ ls -a
.  ..  .keepme  mysqld_safe_syslog.cnf
```



如果没有，则将上一层的 `my.cnf` 拷贝到该目录下。

```python
/etc/mysql$ ls
conf.d  debian-start  debian.cnf  my.cnf

/etc/mysql$ sudo cp my.cnf ./conf.d/mysqld.cnf

/etc/mysql$ cd conf.d

/etc/mysql/conf.d$ ls
mysqld.cnf  mysqld_safe_syslog.cnf
```

* 查看 `/etc/mysql` 目录是否存在 `my.cnf` 配置文件。
* 把 `my.cnf`  拷贝到 `/etc/mysql/conf.d` 目录下
* 进入  `/etc/mysql/conf.d` 目录
* 查看 `mysqld.cnf` 已经拷贝进来。



编辑 `mysqld.cnf`文件

```python
$ sudo vim mysqld.cnf
```

第47行左右是需要修改的绑定 IP，输入 `47dd`可以直达47行，再点击小写的 `i` 就可以编辑。

这里是为了桌面上 navicat 操作方便。**真正部署用 127.0.0.1 。**

```python
bind-address = 0.0.0.0
```

按ESC退出编辑状态，输出 `:wq` 退出 vim。



重启 mysql

```python
$ sudo service mysql restart
```



同时也需要在 mysql 配置中指明哪些 IP 可以连接进来。

修改mysql的权限，让所有的 IP 地址都可以链接上来。

```python
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '输入你的密码' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```



## 安装 Python 环境

查看环境中有 Python 2.7.6 以及 Python 3.4，但是没有pip。

安装 Python 的 pip，后面的`python-dev`也要安装，否则安装失败。

```python
$ sudo apt-get install python-pip python-dev build-essential
```



把 `virtualenvwrapper` 写进 bash 配置文件。进入 bash 配置文件

```python
$ vim ~/.bashrc
```

按 i 编辑。

第一行是仓库位置，这里是用户目录下的 `virtualenvs` 目录。第二行是指定运行的位置。

```python
export WORKON_HOME=~/virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

哪里去找 `virtualenvwrapper.sh` 位置，使用改名了

```
which python3
```



出来以后再刷新配置文件

```python
$ source ~/.bashrc
```



建立 python3 的虚拟环境

```python
$ mkvirtualenv --python=/usr/bin/python3 py3django9
```



安装依赖包 `mysqlclient` ，出现错误

```python
 OSError: mysql_config not found
```



因为需要安装系统的包

```python
$ sudo apt-get install libmysqlclient-dev python3-dev
```







## uWSGI



```python
uwsgi –http :8000 –module MxOnline.wsgi
```









