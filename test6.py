# -*- coding: utf-8 -*-
"""
@Time: 2017/9/24 8:25
@Author: sunxiang
"""

# 词性标注

import nltk

text = nltk.word_tokenize("And now for something completely different")

print nltk.pos_tag(text)

