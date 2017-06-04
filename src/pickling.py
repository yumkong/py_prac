# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:57:36 2016

@author: yumkong
"""

try:
    import cPickle as pickle
except ImportError:
    import pickle
    
d = dict(name='Wang', age=20, score=100)

# save to a pickle string
ss = pickle.dumps(d)
# recover from the pickle string
dd = pickle.loads(ss)
print dd

#save to file (aka: file-like object)
f1 = open('dump.txt', 'wb')
pickle.dump(d, f1)
f1.close()
#recover from file (aka: file-like object)
f2 = open('dump.txt', 'rb')
d2 = pickle.load(f2)
f2.close()
print d2

import json
#dumps()方法返回一个str，内容就是标准的JSON
ss1 = json.dumps(d)
#反序列化得到的字符串对象dd1默认都是unicode而不是str
dd1 = json.loads(ss1)