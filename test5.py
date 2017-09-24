# -*- coding: utf-8 -*-
"""
@Time: 2017/9/23 12:25
@Author: sunxiang
排序
"""




# tricky = sorted([w for w in set(text2) if 'cie' in w or 'cei' in w])
# for word in tricky:
#    print word,

# con = ["dsjjsjd", "dd22", "djskdjasfkashfak"]
# def f(x):
#     return len(x)
# sort(key=f)
# print L
#
# print sorted(con)

# L = [{1:5,3:4},{1:3,6:3},{1:1,2:4,5:6},{1:9}]
# def f2(a,b):
#     return a[1]-b[1]
# L.sort(cmp=f2)
# print L

L = ["dsjjsjd", "dd22", "djskdjasfkashfak"]


def f(x):
    return len(x)


L.sort(key=f)
print L

print sorted(L)
