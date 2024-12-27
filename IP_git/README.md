git命令一览：
git pull  
git add .  
git commit -m '123'  
git push  

---



$ touch README.me  
$ git init  
$ git add .  
$ git commit -m 'first commit'  
$ git remote add origin http://118.117.161.28:13580/code_xie/IP.git  
$ git push -u origin master  




安装本地 git 

初始化仓库
git init

git config --global user.email "gaozhengj@foxmail.com"
git config --global user.name "gaozhengjie"

将远程仓库与本地关联
git remote add origin https://github.com/gaozhengjie/AddressBook.git

将远程仓库的东西拉取到本地
git pull origin master

添加修改信息
git add .

提交修改信息
git commit -m "init"

将本地文件推送到远程仓库
git push -u origin master

origin是本地仓库的名称，也可以替换为其它

master是远程主分支的名称，目前改为了main


## 常见报错

>fatal: refusing to merge unrelated histories

解决办法，在操作命令后添加`--allow-unrelated-histories`

```
git pull origin master --allow-unrelated-histories
```

>执行`git add .`命令是出现警告信息 warning: in the working copy of ‘...‘, LF will be replaced by CRLF the next time Git touche

原因是CR/LF是不同操作系统上使用的换行符，解决办法
windows平台

```
git config --global core.autocrlf true
```

linux平台

```
git config --global core.autocrlf input
```