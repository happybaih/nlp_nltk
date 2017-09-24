# -*- coding: utf-8 -*-

import jieba
import codecs

"""
1. 文本切割
"""
def sent2word(sentence):
    """
    Segment a sentence to words
    Delete stopwords
    """
    segList = jieba.cut(sentence)
    segResult = []
    for w in segList:
        segResult.append(w)

    # 1加载分词 去除词
    f = codecs.open("stop_words.txt", "rb", encoding="utf-8")
    stopwords = f.read().split(u",")

    # stopwords = list()
    # with open("stop_words.txt", "rb") as f:
    #     f_list = f.readlines()
    #     for f_one in f_list:
    #         stopwords.append(f_one.strip())
    # 2加载分词 去除词

    newSent = []
    for word in segResult:
        if word in stopwords:
            print "stopword: %s" % word
            continue
        else:
            newSent.append(word)
    return newSent

str = "这样的酒店配这样的价格还算不错"
result_list = sent2word(str)
for re_one in result_list:
    print re_one