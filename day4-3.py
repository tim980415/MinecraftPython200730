# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:33:12 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from  random import randrange

for i in range(10):
    x,y,z = mc.player.getTilePos()
    x = x+i
    for j in range(10):
        r = randrange(16) 
        #隨機抽顏色放進r
        z = z+1
        mc.setBlock(x,y,z,35,r)

r = randrange(1,16)
#隨機抽的顏色
while True:
    hits = mc.events.pollBlockHits()
    #hits 打到的所有清單
    if len(hits) > 0 :
        hit = hits[0]
        # hit 清單裡的第一個
        block = mc.getBlockWithData(hit.pos)
        d = block.data
        # d是方塊的資料
        if d == r :
            mc.postToChat("恭喜你找到了!!!")
            mc.setBlock(hit.pos,41)
            break
        elif d < r :
            mc.postToChat("找錯了!!! 要再大一點")
        elif d > r : 
            mc.postToChat("找錯了!!! 要再小一點")