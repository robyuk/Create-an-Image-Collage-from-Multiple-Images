#! /usr/bin/env /usr/bin/python3
#
# Creates a collage of 6 images
# The images must be all the same size and resolution

import cv2
import os
import numpy as np

columns=3
rows=2
margin=20
imageDir='images'

images=os.listdir(imageDir)
imageObjects=[cv2.imread(f'{imageDir}/{filename}') for filename in images]
#print(images)

shape=cv2.imread(f'{imageDir}/{images[0]}').shape
#print(shape)

bigImage=np.full(((shape[0]+margin)*rows+margin,(shape[1]+margin)*columns+margin,shape[2]),255,np.uint8)
print(bigImage.shape)

positions=[(x,y) for x in range(columns) for y in range(rows)]
print(positions)

for (posx, posy), image in zip(positions, imageObjects):
  x=posx*(shape[1]+margin)+margin
  y=posy*(shape[0]+margin)+margin
  bigImage[y:y+shape[0],x:x+shape[1]]=image
  
cv2.imwrite('grid.jpeg',bigImage)

