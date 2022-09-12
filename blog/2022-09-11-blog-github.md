# 使用github搭建个人博客

好久没有更新博客了，相信大家都想知道如何用github搭建个人博客，网上看过许多教程，都把这么简单的事弄得很复杂，后来自己摸索了一套方法

- [Github建库](#Github建库)
- [配置环境](#配置环境)
- [写博客](#写博客)

# Github建库
建库，你首先得有账号，不过注册账号我就不再赘述，输入`https://github.com/new`，这里就是建库页面

像我下面这样填：

![https://rainwangpupil.github.io/assets/建库.jpg](https://rainwangpupil.github.io/assets/建库.jpg)

`UserName`指的是你的用户名

> Q:我必须要填UserName.Github.io么？
> A:不一定，但是这样的话，你就不能以`UserName.Github.io`的形式访问博客，得以UserName.Github.io/你的仓库名的形式访问博客

点击下方的`Creat repository`就可以建库了

# 配置环境
建完库以后，得配置环境，方便我们放置博客

找到`Settings`按钮

![https://rainwangpupil.github.io/assets/配置p1.jpg](https://rainwangpupil.github.io/assets/配置p1.jpg)

点击`Pages`按钮

![https://rainwangpupil.github.io/assets/配置p2.jpg](https://rainwangpupil.github.io/assets/配置p2.jpg)

打开选项勾，调整完毕后点`Save`

![https://rainwangpupil.github.io/assets/配置p3.jpg](https://rainwangpupil.github.io/assets/配置p3.jpg)

![https://rainwangpupil.github.io/assets/配置p4.jpg](https://rainwangpupil.github.io/assets/配置p4.jpg)

点击`Code`回到主页，点击`Add file`,选择`Creat New file`

![https://rainwangpupil.github.io/assets/配置p5.jpg](https://rainwangpupil.github.io/assets/配置p5.jpg)

标题改成`__config.yml`在编辑栏里写入以下内容：
```
theme: jekyll-theme-cayman
```
![https://rainwangpupil.github.io/assets/配置p6.jpg](https://rainwangpupil.github.io/assets/配置p6.jpg)

点击下面的`Commit New file`

![https://rainwangpupil.github.io/assets/配置p7.jpg](https://rainwangpupil.github.io/assets/配置p7.jpg)

# 写博客

写博客用`Markdown`语法编写，按照之前的方法创建一个文件叫`文件名.md`
使用`Markdown`语法编写完毕后，点击`Commit Changes`即可以`UserName.github.io/文件名.html`查看博客了