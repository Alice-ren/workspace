import os
import linecache
import sys
import argparse
import numpy as np
from PIL import Image, ImageDraw

filelist=open('output.txt').readlines()
count = len(filelist)
txtName = "output.txt"
imgSaveDir = '/home/rentingting/project/caffessd/caffe/fddb_result'
for i in range(count-1):
    line = linecache.getline('output.txt',i)
    while i<2:
      i=i+1
    if line == ' ' :
      continue
    else:
      fst_line=linecache.getline('output.txt',i)
      fst_line_name=fst_line.split(" ")[0]
      fst_line_data_raw=fst_line.split(" ")[-5:]
      fst_line_data=' '.join(fst_line_data_raw).rstrip('\n')
     
      print(fst_line_name)
      print(fst_line_data)

      path=os.path.abspath(fst_line_name)     
      img = Image.open(path)
      draw = ImageDraw.Draw(img)
      xmin = int(fst_line_data.split(" ")[1])
      ymin = int(fst_line_data.split(" ")[2])
      xmax = int(fst_line_data.split(" ")[3])
      ymax = int(fst_line_data.split(" ")[4])
      print(xmin)
      print(xmax)
      print(ymin)
      print(ymax)
      mode = img.mode
      print(mode)
      if mode=='RGB':
        draw.rectangle([xmin, ymin, xmax, ymax], outline=(255, 0, 0))
      if mode=='GRAY':
        draw.rectangle([xmin, ymin, xmax, ymax], outline=(255))
      if  mode=='BINARY':
        draw.rectangle([xmin, ymin, xmax, ymax], outline=(255))
      p,imgname=os.path.split(fst_line_name)
      print(imgname)
      savename = os.path.join(imgSaveDir,imgname)
      print(savename) 
      img.save(savename)

