# -*- coding: utf-8 -*-
"""
@Time: 2017/9/20 20:27
@Author: sunxiang

python中文分句
"""

def cut_sentences(sentence):
    if not isinstance(sentence, unicode):
        sentence = unicode(sentence)
    puns = frozenset(u'。！？')
    tmp = []
    for ch in sentence:
        tmp.append(ch)
        if puns.__contains__(ch):
            yield ''.join(tmp)
            tmp = []
    yield ''.join(tmp)


s = u'计算机评价效果，需要给定参考摘要作为标准答案，通过制定一些规则来给生产的摘要打分。    目前使用最广泛的是ROUGH系统(Recall-Oriented Understudy for Gisting Evaluation),基本思想是将待审的摘要和参考摘要的n元组共现统计量作为评价作为评价依据，然后通过一系列标准进行打分。包括(ROUGH-N, ROUGH-L, ROUGH-W，ROUGH-S和ROUGH-SU)几个类型。  通俗地将就是通过一些定量化的指标来描述待审摘要和参考文摘之间的相似性，维度考虑比较多，在一定程度上可以很好地评价Extracive产生的摘要'

sentences = cut_sentences(s)
# print type(sentences)
for i in sentences:
    print("-----")
    print(i)


