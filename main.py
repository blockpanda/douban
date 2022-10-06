
#预测一部电影的评分，属于分类问题。输入一段具体的文本，输出具体的评分
#需要完成：
#1.文本预处理，分词，停用词过滤、低频次过滤、特殊符号的过滤
#文本转化为向量，三种方式，tf—idf,word2vec以及BERT
#训练逻辑回归和朴素贝叶斯模型，做交叉验证
#评估模型的正确率


#导入数据处理基础包
import numpy as np
import pandas as pd

#导入用于计数的包
from collections import Counter

#导入tf_idf相关的包
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

#导入模型评估的包
from sklearn import metrics

#导入与word2vec相关的包
from gensim.models import KeyedVectors

#导入与bert embedding相关的包
# from m bert_embedding import BertEmbedding
# import mxnet

#tqdm包是用来对可迭代对执行时生成一个进度条用以监视程序运行过程
from tqdm import tqdm

#导入其他功能包
import requests
import os

#读取数据
data = pd.read_csv('DMSC.csv')

#观察数据格式
data.head()

#输出数据的一些相关信息
data.info()

#只保留数据中需要的两列：Comment列和Star列
data = data[['Comment','Star']]
#观察新的数据的格式
# print(data.head())

#star代表具体的评分，这个项目中，预测正面还是负面，1.2是负面，345是正面
data['Star']=(data.Star/3).astype(int)
print(data.head())


#去掉一些无用的字符，自定义一个几何字符，并从文本中去掉
stop_words = ["啊"]
filtered_words = [word for word in word_list if word not in stop_words]
print (filtered_words)





