# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:04:48 2016

@author: yumkong
"""
#regular expression module
import re 
#import numpy as np
import matplotlib.pyplot as plt

base_num = 245
cnt = 1
epoch = []
loss = []
epoch_substr = str(base_num * 1) + ':'
try:
    f = open('../retrieve_learningrate/log0827_2.txt', 'r')
    for line in f.readlines():
        if line.find(epoch_substr) >= 0:
            tmpstr = re.split(r'[\s\,a-zA-Z]+', line)
            #print 'epoch' + str(cnt) + ': ' + tmpstr[2]
            epoch.append(cnt)
            loss.append(tmpstr[2])
            #update
            cnt = cnt + 1
            epoch_substr = str(base_num * cnt) + ':'
finally:
    if f:
        f.close()

plt.plot(epoch, loss, 'g')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('YOLO training on VOC2007+VOC2012')
plt.savefig('../result/yolo_cfg_yolo2_iter_40000_batch_64.png',bbox_inches='tight',dpi=200)
plt.close()