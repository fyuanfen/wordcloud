#coding: utf-8

import os
from os import path
from PIL import Image
import numpy as np
import matplotlib
matplotlib.use('qt4agg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import jieba


stopwords = {}

def stopword(filename = ''):
    global stopwords
    f = open(filename, 'r',encoding= 'utf-8')
    line = f.readline().rstrip()

    while line:
        stopwords.setdefault(line, 0)
        stopwords[line] = 1
        line = f.readline().rstrip()

    f.close()

stopword(filename = './stopwords.txt')



# # 导入
# d = path.dirname(__file__)
# text = open(path.join(d, 'letter_one.rtf')).read().decode("gbk")
# print text


with open ('./中国宪法.txt',encoding ='utf-8') as f:

    text = f.read()
    seg_generator = jieba.cut(text)

    seg_list = [i for i in seg_generator if i not in stopwords]

    seg_list = [i for i in seg_list if i != u' ']

    seg_list = r' '.join(seg_list)



# 词云
# wordcloud = WordCloud(max_font_size=40, relative_scaling=.5)
wordcloud = WordCloud(font_path='./simheittf/simhei.ttf',    background_color="black",   margin=5, width=1800, height=800)

wordcloud = wordcloud.generate(seg_list)
#画图

plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
