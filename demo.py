# coding:utf-8

from os import path
import chnSegment
import plotWordcloud


if __name__=='__main__':

    # 读取文件
    d = path.dirname(__file__)
    #  text = open(path.join(d, ”users“.txt')).read()
    text = open(path.join(d,'doc//alice.txt')).read()
  

    # 若是中文文本，则先进行分词操作
    text=chnSegment.word_segment(text)
    
    # 生成词云
    plotWordcloud.generate_wordcloud(text)
