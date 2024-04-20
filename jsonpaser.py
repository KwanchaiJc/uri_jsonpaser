#!/usr/bin/env python
# coding: utf-8

##oldcodde
#import json

#with open('D:\S_R_I\SECUPI\Siammakro\KhunNanLog\SecuPi-011f559d-0518-4ac9-bdbc-863a133b0231-btxs.json') as f:
  #data2 = json.load(f)

#length = len(data2)
#for i in range(length):
    #print(data2[i]["uri"])
#--------------------------------------------------------------------------------------------------------------
#Coding by Kwanchai jaroensirichot
import os
import json

path = 'Directory'

folder = os.fsencode(path)

filenames = []

for file in os.listdir(folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.json') ):
        filenames.append(filename)
length = len(filenames)
for i in range(length):
    mergepath = path + "\\" + filenames[i]
    with open(mergepath) as f:
        data2 = json.load(f)
        length2 = len(data2)
        for j in range(length2):
            print(data2[j]["uri"])
          
