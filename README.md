<img width="2688" height="4038" alt="image" src="https://github.com/user-attachments/assets/022e3a4e-19d4-420b-9629-71cc72b5c792" />

# 网页在线版

你好，感谢你体验这个项目，我是把原来[大佬](https://github.com/Xinger006)的项目搬到Web网页上，首先确实文字长了不太行，推荐先查一次重，拿着查重结果，看论文中哪里和其他论文重复率高了，使用[汉语反向词典](https://wantwords.net/)找近义词替换，一部分一部分的降重，我当时就是这么降重的。

[大佬](https://github.com/Xinger006)和我也没时间去优化，推荐本地运行，现在是部署在免费python服务器上，很不稳定。
  
最后现在有了更好的选择，可以使用ChatGPT去降重，比这个工具好用。诶，我原来那时候还没有ChatGPT用呀，现在有的用真好！

当然用这个项目也行：

此项目非常适合需要提交学术论文（如毕业论文、期刊投稿）的学生和研究人员。例如，如果你正为论文查重率过高而焦虑，却不信任在线降重服务或不想支付高昂费用，这个工具能帮你免费、私密地在本地进行初步的相似度自查和修改。与直接使用ChatGPT重写不同，它更专注于发现并辅助你自主修改相似语句，让你更好地掌控降重过程。

在线版使用的是[免费服务器 pythonanywhere](https://www.pythonanywhere.com/)，不保证服务稳定性，你可以自己本地安装python环境，本地使用
## 自己本地使用
安装好python环境后，运行
```shell
pip install -r requirements.txt
```
```shell
python -m flask run -p 8088 -h 0.0.0.0
```
打开 http://127.0.0.1:8088 即可在本地使用

## 打包EXE

```shell
pyinstaller -F --add-data="./templates;templates" .\app.py
```
打开 http://127.0.0.1:8088 即可在本地使用

## 已打包好的EXE
[下载](https://github.com/liulinboyi/Dissertation-weight-reduction/releases/latest)到本地后，双击即可使用

![](/img/app.png)
打开 http://127.0.0.1:8088 即可在本地使用

# 两段文字相似度对比程序（带界面,可用于论文降重）
![icon](icon.ico)
## （1）使用Python及其simtext包，逐句计算两段文本相似度
（一段自己的，一段别人的），
并实现相似度大于阈值的文字标红。
##  (2) 使用PyQt5，实现界面
## （3）实现相似度大于阈值的句子标红
## （3）使用pyinstaller打包成exe

## 达到的效果（GUI）：
![GUI](gui.png)

## 打包好的下载链接：
论文降重小工具下载全部链接（免费免安装，两段文字相似度对比） - 星未的文章 - 知乎
https://zhuanlan.zhihu.com/p/378432331

## 代码中有从网络上参考或者直接复制过来的内容，对原作者致以谢意！
## 但因时间有些久了，来源无法一一追溯，故没有列出来源。报以歉意！
## 本人为编程爱好者，以实现功能为目标，所以代码写的天马行空。欢迎交流、批评和指正！
