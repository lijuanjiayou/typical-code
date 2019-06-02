# git 使用教程

### 1. 步骤&作用：



##### 第一步：git clone 远端网址

*作用：创建远端仓库并连接到本地仓库。*

##### 第二步：git add .

作用：*更新本地仓库到缓存区*。

##### 第三步：git commit -m "注释一下更新了什么"

*作用：commit*缓存区内容到本地仓库*。

##### 第四步：git pull origin master

*作用：将远端仓库拉到本地仓库，查看是否有修改和冲突。*

##### 第五步：git push origin master

*作用：若有冲突则见下方讲解解决冲突，若无冲突则将本地仓库内容推送到远端仓库，使远端仓库更新到最新版本。*

##### 另外：git status可以查看当前状态。



### 2. 详解：

##### 使用git的前提：

首先要在本地电脑某个位置建立一个文件夹，然后在该文件夹里右键，选择Git Bash Here,打开git命令行。然后开始执行上面步骤。

##### 如何解决冲突：

当从远端pull过来的文件有修改，和本地仓库的文件存在conflict时，会在本地文件中出现以下显示：<<<<<<与======之间是本地内容，======与>>>>>>之间是远端仓库内容，这是两者之间存在conflict的地方，而>>>>>>下方是两者一致及没有conflict的地方。此时需要修改本地文件内容，解决冲突，然后重新add,commit，push到远端仓库。

```java
class HelloWorld{
    
<<<<<<< HEAD
    private shazi String sayContent = "hello world !!!"
=======
    private haha String sayContent = "hello world !!!"
>>>>>>> d234c0dfb697264c6e10f32c23e2c86d73409d39
    public static void main(String[] args){
        System.out.println(sayContent);
    }
}
```

正确格式：

```java


class HelloWorld{
    private String sayContent = "hello world !!!"
    public static void main(String[] args){
        System.out.println(sayC    }
}
```

##### SVN和git的区别：

SVN是集中式版本控制系统，只有一个版本库在中央，本地没有版本库，当较多人数使用版本库时，经常提交代码容易产生代码冲突，解决冲突耗时费力；而git就解决了这一难题，每个人都有自己的暂存区和版本库，只有当最终完成时才和远端版本库进行交互，如果有冲突一次就解决了。

##### 额外小知识：

1）在typero里按`三下可以打开编程语言格式，选择java即可使用java代码格式。

2）键盘上的上下键可以自动选择DOS命令行里使用过的命令，从最近一个命令开始。

3）学习git的网址：https://www.liaoxuefeng.com/wiki/896043488029600

