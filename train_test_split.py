#!/usr/bin/env python
# coding: utf-8

import glob
import shutil
import os

src_dir = "NWPU-RESISC13"
dst_dir = "RESISC13"

train = '/train/'
test = '/test/'
val = '/val/'
for cal in os.listdir(src_dir):
    images = []
    for jpgfile in glob.iglob(os.path.join(src_dir+"/"+cal, "*.jpg")):
        images.append(jpgfile)
    #images = sorted(images)
    
    direct_train = dst_dir+train+cal+"/" 
    direct_test = dst_dir+test+cal+"/"
    direct_val = dst_dir+val+cal+"/"
    os.makedirs(direct_train)
    os.makedirs(direct_val)
    os.makedirs(direct_test)
    count = 0
    for jpgfile in images:
        #Split 400 to train
        if count>=0 and count<400:
            shutil.copy(jpgfile, direct_train)
        #Split 50 to val
        if count>=400 and count<550:
            shutil.copy(jpgfile, direct_val)
        #Split 250 to test
        if count>=550 and count<700:
            shutil.copy(jpgfile, direct_test)
        count +=1
