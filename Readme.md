
python真的超级超级好玩呐，不管是爬虫还是数据挖掘，真的都超级有意思。

今天，来说一说python一个好玩的模块wordcloud

构建词云的方法很多, 但是个人觉得python的wordcloud包功能最为强大,可以自定义图片. 

官网: https://amueller.github.io/word_cloud/ 

github: https://github.com/amueller/word_cloud

# 例子: 

闲着无聊，用wordcloud做了个词云标签，Jieba分词分析了一下给木木写的日记，捂脸ing⊂(˃̶͈̀ε ˂̶͈́ ⊂ )⋯⋯
![image](http://oavk3bisu.bkt.clouddn.com/wordcloud-2.png)




又顺便从网上爬了几百句英文情诗，差不多都是这些套路

又是一项撩妹新技能get，可惜我木有妹子可以撩～～郁闷o(￣ヘ￣o❀)
![image](http://oavk3bisu.bkt.clouddn.com/wordcloud-1.png)

**字体用的是cabin-sketch.bold**

**大家也可以自己来调模板和字体**



# 安装
## 方法1

`pip install wordcloud`

## 方法2
- github下载并解压
```
wget  https://github.com/amueller/word_cloud/archive/master.zip
unzip master.zip
rm master.zip
cd word_cloud-master
```

- 安装依赖包

`sudo pip install -r requirements.txt`

- 安装wordcloud

`python setup.py install`


## 方法三

- 下载[.whl文件](http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud)

- 使用cd命令进入whl文件的路径

- 运行这条命令：

`python -m pip install <filename> `


# 源码在word.py中
源码的运行结果就像下面这个样子
![](http://oavk3bisu.bkt.clouddn.com/wordcloud.png)


# Reference:
[python好玩的词云wordcloud](http://zyy1314.com/2016/07/31/python%E7%9A%84%E4%B8%80%E4%B8%AA%E5%A5%BD%E7%8E%A9%E6%A8%A1%E5%9D%97wordcloud/)
