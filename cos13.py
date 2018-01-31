import cv2 as cv
import numpy as np
import time
import socket
import sys

HOST, PORT = "localhost", 50007


sibu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sibu.connect((HOST, PORT))

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
#import pymouse

img = np.zeros((720,990,3), np.uint8)
img[:] = (255,255,255)
cv.rectangle(img,(0,180),(990,270),(105,105,105),-1)
cv.rectangle(img,(0,450),(990,540),(105,105,105),-1)
cv.rectangle(img,(180,0),(270,720),(105,105,105),-1)
cv.rectangle(img,(450,0),(540,720),(105,105,105),-1)
cv.rectangle(img,(720,0),(810,720),(105,105,105),-1)

def nothing():
	pass
def drawhorline(a):
    i = a
    while(i<180+a):
        cv.line(img,(i+5,194),(i+15,194),(255,255,255),1)
        cv.line(img,(i+5,208),(i+15,208),(255,255,255),1)
        cv.line(img,(i+5,240),(i+15,240),(255,255,255),1)
        cv.line(img,(i+5,254),(i+15,254),(255,255,255),1)
        cv.line(img,(i+5,464),(i+15,464),(255,255,255),1)
        cv.line(img,(i+5,478),(i+15,478),(255,255,255),1)
        cv.line(img,(i+5,510),(i+15,510),(255,255,255),1)
        cv.line(img,(i+5,524),(i+15,524),(255,255,255),1)
        i = i+15;
def drawverline(a):
    i = a
    while(i<180+a):
        cv.line(img,(194,i+5),(194,i+15),(255,255,255),1)
        cv.line(img,(208,i+5),(208,i+15),(255,255,255),1)
        cv.line(img,(240,i+5),(240,i+15),(255,255,255),1)
        cv.line(img,(254,i+5),(254,i+15),(255,255,255),1)
        cv.line(img,(464,i+5),(464,i+15),(255,255,255),1)
        cv.line(img,(478,i+5),(478,i+15),(255,255,255),1)
        cv.line(img,(510,i+5),(510,i+15),(255,255,255),1)
        cv.line(img,(524,i+5),(524,i+15),(255,255,255),1)
        cv.line(img,(734,i+5),(734,i+15),(255,255,255),1)
        cv.line(img,(748,i+5),(748,i+15),(255,255,255),1)
        cv.line(img,(780,i+5),(780,i+15),(255,255,255),1)
        cv.line(img,(794,i+5),(794,i+15),(255,255,255),1)
        i = i+15;

drawhorline(0)
drawhorline(270)
drawhorline(540)
drawhorline(810)
drawverline(0)
drawverline(270)
drawverline(540)


def drawmotaline():
    cv.line(img,(0,224),(180,224),(220,220,220),2)
    cv.line(img,(270,224),(450,224),(220,220,220),2)
    cv.line(img,(540,224),(720,224),(220,220,220),2)
    cv.line(img,(810,224),(990,224),(220,220,220),2)
    cv.line(img,(0,494),(180,494),(220,220,220),2)
    cv.line(img,(270,494),(450,494),(220,220,220),2)
    cv.line(img,(540,494),(720,494),(220,220,220),2)
    cv.line(img,(810,494),(990,494),(220,220,220),2)
    cv.line(img,(224,0),(224,180),(220,220,220),2)
    cv.line(img,(224,270),(224,450),(220,220,220),2)
    cv.line(img,(224,540),(224,720),(220,220,220),2)
    cv.line(img,(494,0),(494,180),(220,220,220),2)
    cv.line(img,(494,270),(494,450),(220,220,220),2)
    cv.line(img,(494,540),(494,720),(220,220,220),2)
    cv.line(img,(766,0),(766,180),(220,220,220),2)
    cv.line(img,(766,270),(766,450),(220,220,220),2)
    cv.line(img,(766,540),(766,720),(220,220,220),2)




car_exists = 0
"""startpoints =
        [1,0] = lane - 3 = [0,187] dirn = 2
        [1,0] = lane - 2 = [0,202] dirn = 2 
        [1,0] = lane - 1 = [0,217] dirn = 2
        
        [2,0] = lane - 3 = [0,457] dirn = 2
        [2,0] = lane - 2 = [0,472] dirn = 2
        [2,0] = lane - 1 = [0,487] dirn = 2

        [0,1] = lane - 1 = [233,0] dirn = 3 
        [0,1] = lane - 2 = [248,0] dirn = 3
        [0,1] = lane - 3 = [263,0] dirn = 3

        [0,2] = lane - 1 = [503,0] dirn = 3
        [0,2] = lane - 2 = [518,0] dirn = 3
        [0,2] = lane - 3 = [533,0] dirn = 3

        [0,3] = lane - 1 = [773,0] dirn = 3
        [0,3] = lane - 2 = [788,0] dirn = 3
        [0,3] = lane - 3 = [803,0] dirn = 3

        [1,4] = lane - 1 = [990,233] dirn = 4
        [1,4] = lane - 2 = [990,248] dirn = 4
        [1,4] = lane - 3 = [990,263] dirn = 4

        [2,4] = lane - 1 = [990,503] dirn = 4
        [2,4] = lane - 2 = [990,518] dirn = 4
        [2,4] = lane - 3 = [990,533] dirn = 4

        [3,1] = lane - 3 = [187,720] dirn = 1
        [3,1] = lane - 2 = [202,720] dirn = 1
        [3,1] = lane - 1 = [217,720] dirn = 1

        [3,2] = lane - 3 = [457,720] dirn = 1
        [3,2] = lane - 2 = [472,720] dirn = 1
        [3,2] = lane - 1 = [487,720] dirn = 1

        [3,3] = lane - 3 = [727,720] dirn = 1
        [3,3] = lane - 2 = [742,720] dirn = 1
        [3,3] = lane - 1 = [757,720] dirn = 1
    endpoints
        [1,0] = lane - 1 = [0,233]
        [1,0] = lane - 2 = [0,248]
        [1,0] = lane - 3 = [0,263]
        
        [2,0] = lane - 1 = [0,503]
        [2,0] = lane - 2 = [0,518]
        [2,0] = lane - 3 = [0,533] 

        [0,1] = lane - 3 = [187,0] 
        [0,1] = lane - 2 = [202,0] 
        [0,1] = lane - 1 = [217,0] 

        [0,2] = lane - 3 = [457,0] 
        [0,2] = lane - 2 = [472,0] 
        [0,2] = lane - 1 = [487,0] 

        [0,3] = lane - 3 = [727,0] 
        [0,3] = lane - 2 = [742,0] 
        [0,3] = lane - 1 = [757,0] 

        [1,4] = lane - 3 = [990,187] 
        [1,4] = lane - 2 = [990,202] 
        [1,4] = lane - 1 = [990,217] 

        [2,4] = lane - 3 = [990,457] 
        [2,4] = lane - 2 = [990,472] 
        [2,4] = lane - 1 = [990,487] 

        [3,1] = lane - 1 = [233,720] 
        [3,1] = lane - 2 = [248,720] 
        [3,1] = lane - 3 = [263,720] 

        [3,2] = lane - 1 = [503,720] 
        [3,2] = lane - 2 = [518,720] 
        [3,2] = lane - 3 = [533,720] 

        [3,3] = lane - 1 = [773,720] 
        [3,3] = lane - 2 = [788,720] 
        [3,3] = lane - 3 = [803,720]
"""
"""
    state =
        forward = 1
        left = 2
        right = 3
        laneleft = 4
        laneright = 5
"""

#car_original mat = [startx,starty,endx,endy,curx,cury,state,dirn,pathmatrix,startangle,lane,lanestate]
car_mat = [[742,0,0,457,1,2,[[200,200,200,0,200],[200,3,2,1,200],[200,4,3,2,200],[200,200,200,200,200]],0,3,0,0]]

weight_hor_lr_mat = [[0,0,0,0],[0,0,0,0]]
weight_hor_rl_mat = [[0,0,0,0],[0,0,0,0]]
weight_ver_ud_mat = [[0,0,0],[0,0,0],[0,0,0]]
weight_ver_du_mat = [[0,0,0],[0,0,0],[0,0,0]]
flag = 0


def drawlights(a,b,c,d,e,f):
    cv.rectangle(img,(175,180),(180,270),(105,105,105),-1)
    cv.rectangle(img,(180,175),(270,180),(105,105,105),-1)
    cv.rectangle(img,(270,180),(275,270),(105,105,105),-1)
    cv.rectangle(img,(180,270),(270,275),(105,105,105),-1)

    cv.rectangle(img,(445,180),(450,270),(105,105,105),-1)
    cv.rectangle(img,(450,175),(540,180),(105,105,105),-1)
    cv.rectangle(img,(540,180),(545,270),(105,105,105),-1)
    cv.rectangle(img,(450,270),(540,275),(105,105,105),-1)

    cv.rectangle(img,(715,180),(720,270),(105,105,105),-1)
    cv.rectangle(img,(720,175),(810,180),(105,105,105),-1)
    cv.rectangle(img,(810,180),(815,270),(105,105,105),-1)
    cv.rectangle(img,(720,270),(810,275),(105,105,105),-1)

    cv.rectangle(img,(175,450),(180,540),(105,105,105),-1)
    cv.rectangle(img,(180,445),(270,450),(105,105,105),-1)
    cv.rectangle(img,(270,450),(275,540),(105,105,105),-1)
    cv.rectangle(img,(180,540),(270,545),(105,105,105),-1)

    cv.rectangle(img,(445,450),(450,540),(105,105,105),-1)
    cv.rectangle(img,(450,445),(540,450),(105,105,105),-1)
    cv.rectangle(img,(540,450),(545,540),(105,105,105),-1)
    cv.rectangle(img,(450,540),(540,545),(105,105,105),-1)

    cv.rectangle(img,(715,450),(720,540),(105,105,105),-1)
    cv.rectangle(img,(720,445),(810,450),(105,105,105),-1)
    cv.rectangle(img,(810,450),(815,540),(105,105,105),-1)
    cv.rectangle(img,(720,540),(810,545),(105,105,105),-1)
    
    cv.rectangle(img,(180,180),(270,270),(105,105,105),-1)
    cv.rectangle(img,(450,180),(540,270),(105,105,105),-1)
    cv.rectangle(img,(720,450),(810,540),(105,105,105),-1)
    cv.rectangle(img,(180,450),(270,540),(105,105,105),-1)
    cv.rectangle(img,(450,450),(540,540),(105,105,105),-1)
    cv.rectangle(img,(720,450),(810,540),(105,105,105),-1)
    if(a == 1):
        cv.rectangle(img,(233-3,175),(233+3,180),(0,0,255),-1)
        cv.rectangle(img,(248-3,175),(248+3,180),(0,0,255),-1)
        cv.rectangle(img,(270,233-3),(275,233+3),(0,0,255),-1)
        cv.rectangle(img,(270,248-3),(275,248+3),(0,0,255),-1)
        cv.rectangle(img,(202-3,270),(202+3,275),(0,0,255),-1)
        cv.rectangle(img,(217-3,270),(217+3,275),(0,0,255),-1)
    elif(a == 2):
        cv.rectangle(img,(175,202-3),(180,202+3),(0,0,255),-1)
        cv.rectangle(img,(175,217-3),(180,217+3),(0,0,255),-1)
        cv.rectangle(img,(270,233-3),(275,233+3),(0,0,255),-1)
        cv.rectangle(img,(270,248-3),(275,248+3),(0,0,255),-1)
        cv.rectangle(img,(202-3,270),(202+3,275),(0,0,255),-1)
        cv.rectangle(img,(217-3,270),(217+3,275),(0,0,255),-1)
    elif(a == 3):
        cv.rectangle(img,(233-3,175),(233+3,180),(0,0,255),-1)
        cv.rectangle(img,(248-3,175),(248+3,180),(0,0,255),-1)
        cv.rectangle(img,(175,202-3),(180,202+3),(0,0,255),-1)
        cv.rectangle(img,(175,217-3),(180,217+3),(0,0,255),-1)
        cv.rectangle(img,(202-3,270),(202+3,275),(0,0,255),-1)
        cv.rectangle(img,(217-3,270),(217+3,275),(0,0,255),-1)
    elif(a == 4):
        cv.rectangle(img,(233-3,175),(233+3,180),(0,0,255),-1)
        cv.rectangle(img,(248-3,175),(248+3,180),(0,0,255),-1)
        cv.rectangle(img,(270,233-3),(275,233+3),(0,0,255),-1)
        cv.rectangle(img,(270,248-3),(275,248+3),(0,0,255),-1)
        cv.rectangle(img,(175,202-3),(180,202+3),(0,0,255),-1)
        cv.rectangle(img,(175,217-3),(180,217+3),(0,0,255),-1)
    if(b == 1):
        cv.rectangle(img,(503-3,175),(503+3,180),(0,0,255),-1)
        cv.rectangle(img,(518-3,175),(518+3,180),(0,0,255),-1)
        cv.rectangle(img,(540,233-3),(545,233+3),(0,0,255),-1)
        cv.rectangle(img,(540,248-3),(545,248+3),(0,0,255),-1)
        cv.rectangle(img,(472-3,270),(472+3,275),(0,0,255),-1)
        cv.rectangle(img,(487-3,270),(487+3,275),(0,0,255),-1)
    elif(b == 2):
        cv.rectangle(img,(445,202-3),(450,202+3),(0,0,255),-1)
        cv.rectangle(img,(445,217-3),(450,217+3),(0,0,255),-1)
        cv.rectangle(img,(540,233-3),(545,233+3),(0,0,255),-1)
        cv.rectangle(img,(540,248-3),(545,248+3),(0,0,255),-1)
        cv.rectangle(img,(472-3,270),(472+3,275),(0,0,255),-1)
        cv.rectangle(img,(487-3,270),(487+3,275),(0,0,255),-1)
    elif(b == 3):
        cv.rectangle(img,(503-3,175),(503+3,180),(0,0,255),-1)
        cv.rectangle(img,(518-3,175),(518+3,180),(0,0,255),-1)
        cv.rectangle(img,(445,202-3),(450,202+3),(0,0,255),-1)
        cv.rectangle(img,(445,217-3),(450,217+3),(0,0,255),-1)
        cv.rectangle(img,(472-3,270),(472+3,275),(0,0,255),-1)
        cv.rectangle(img,(487-3,270),(487+3,275),(0,0,255),-1)
    elif(b == 4):
        cv.rectangle(img,(503-3,175),(503+3,180),(0,0,255),-1)
        cv.rectangle(img,(518-3,175),(518+3,180),(0,0,255),-1)
        cv.rectangle(img,(540,233-3),(545,233+3),(0,0,255),-1)
        cv.rectangle(img,(540,248-3),(545,248+3),(0,0,255),-1)
        cv.rectangle(img,(445,202-3),(450,202+3),(0,0,255),-1)
        cv.rectangle(img,(445,217-3),(450,217+3),(0,0,255),-1)
    if(c == 1):
        cv.rectangle(img,(773-3,175),(773+3,180),(0,0,255),-1)
        cv.rectangle(img,(788-3,175),(788+3,180),(0,0,255),-1)
        cv.rectangle(img,(810,233-3),(815,233+3),(0,0,255),-1)
        cv.rectangle(img,(810,248-3),(815,248+3),(0,0,255),-1)
        cv.rectangle(img,(742-3,270),(742+3,275),(0,0,255),-1)
        cv.rectangle(img,(757-3,270),(757+3,275),(0,0,255),-1)
    elif(c == 2):
        cv.rectangle(img,(715,202-3),(720,202+3),(0,0,255),-1)
        cv.rectangle(img,(715,217-3),(720,217+3),(0,0,255),-1)
        cv.rectangle(img,(810,233-3),(815,233+3),(0,0,255),-1)
        cv.rectangle(img,(810,248-3),(815,248+3),(0,0,255),-1)
        cv.rectangle(img,(742-3,270),(742+3,275),(0,0,255),-1)
        cv.rectangle(img,(757-3,270),(757+3,275),(0,0,255),-1)
    elif(c == 3):
        cv.rectangle(img,(773-3,175),(773+3,180),(0,0,255),-1)
        cv.rectangle(img,(788-3,175),(788+3,180),(0,0,255),-1)
        cv.rectangle(img,(715,202-3),(720,202+3),(0,0,255),-1)
        cv.rectangle(img,(715,217-3),(720,217+3),(0,0,255),-1)
        cv.rectangle(img,(742-3,270),(742+3,275),(0,0,255),-1)
        cv.rectangle(img,(757-3,270),(757+3,275),(0,0,255),-1)
    elif(c == 4):
        cv.rectangle(img,(773-3,175),(773+3,180),(0,0,255),-1)
        cv.rectangle(img,(788-3,175),(788+3,180),(0,0,255),-1)
        cv.rectangle(img,(810,233-3),(815,233+3),(0,0,255),-1)
        cv.rectangle(img,(810,248-3),(815,248+3),(0,0,255),-1)
        cv.rectangle(img,(715,202-3),(720,202+3),(0,0,255),-1)
        cv.rectangle(img,(715,217-3),(720,217+3),(0,0,255),-1)
    if(d == 1):
        cv.rectangle(img,(233-3,445),(233+3,450),(0,0,255),-1)
        cv.rectangle(img,(248-3,445),(248+3,450),(0,0,255),-1)
        cv.rectangle(img,(270,503-3),(275,503+3),(0,0,255),-1)
        cv.rectangle(img,(270,518-3),(275,518+3),(0,0,255),-1)
        cv.rectangle(img,(202-3,540),(202+3,545),(0,0,255),-1)
        cv.rectangle(img,(217-3,540),(217+3,545),(0,0,255),-1)
    elif(d == 2):
        cv.rectangle(img,(175,472-3),(180,472+3),(0,0,255),-1)
        cv.rectangle(img,(175,488-3),(180,488+3),(0,0,255),-1)
        cv.rectangle(img,(270,503-3),(275,503+3),(0,0,255),-1)
        cv.rectangle(img,(270,518-3),(275,518+3),(0,0,255),-1)
        cv.rectangle(img,(202-3,540),(202+3,545),(0,0,255),-1)
        cv.rectangle(img,(217-3,540),(217+3,545),(0,0,255),-1)
    elif(d == 3):
        cv.rectangle(img,(233-3,445),(233+3,450),(0,0,255),-1)
        cv.rectangle(img,(248-3,445),(248+3,450),(0,0,255),-1)
        cv.rectangle(img,(175,472-3),(180,472+3),(0,0,255),-1)
        cv.rectangle(img,(175,488-3),(180,488+3),(0,0,255),-1)
        cv.rectangle(img,(202-3,540),(202+3,545),(0,0,255),-1)
        cv.rectangle(img,(217-3,540),(217+3,545),(0,0,255),-1)
    elif(d == 4):
        cv.rectangle(img,(233-3,445),(233+3,450),(0,0,255),-1)
        cv.rectangle(img,(248-3,445),(248+3,450),(0,0,255),-1)
        cv.rectangle(img,(270,503-3),(275,503+3),(0,0,255),-1)
        cv.rectangle(img,(270,518-3),(275,518+3),(0,0,255),-1)
        cv.rectangle(img,(175,472-3),(180,472+3),(0,0,255),-1)
        cv.rectangle(img,(175,488-3),(180,488+3),(0,0,255),-1)
    if(e == 1):
        cv.rectangle(img,(503-3,445),(503+3,450),(0,0,255),-1)
        cv.rectangle(img,(518-3,445),(518+3,450),(0,0,255),-1)
        cv.rectangle(img,(540,503-3),(545,503+3),(0,0,255),-1)
        cv.rectangle(img,(540,518-3),(545,518+3),(0,0,255),-1)
        cv.rectangle(img,(472-3,540),(472+3,545),(0,0,255),-1)
        cv.rectangle(img,(487-3,540),(487+3,545),(0,0,255),-1)
    elif(e == 2):
        cv.rectangle(img,(445,472-3),(450,472+3),(0,0,255),-1)
        cv.rectangle(img,(445,488-3),(450,488+3),(0,0,255),-1)
        cv.rectangle(img,(540,503-3),(545,503+3),(0,0,255),-1)
        cv.rectangle(img,(540,518-3),(545,518+3),(0,0,255),-1)
        cv.rectangle(img,(472-3,540),(472+3,545),(0,0,255),-1)
        cv.rectangle(img,(487-3,540),(487+3,545),(0,0,255),-1)
    elif(e == 3):
        cv.rectangle(img,(503-3,445),(503+3,450),(0,0,255),-1)
        cv.rectangle(img,(518-3,445),(518+3,450),(0,0,255),-1)
        cv.rectangle(img,(445,472-3),(450,472+3),(0,0,255),-1)
        cv.rectangle(img,(445,488-3),(450,488+3),(0,0,255),-1)
        cv.rectangle(img,(472-3,540),(472+3,545),(0,0,255),-1)
        cv.rectangle(img,(487-3,540),(487+3,545),(0,0,255),-1)
    elif(e == 4):
        cv.rectangle(img,(503-3,445),(503+3,450),(0,0,255),-1)
        cv.rectangle(img,(518-3,445),(518+3,450),(0,0,255),-1)
        cv.rectangle(img,(540,503-3),(545,503+3),(0,0,255),-1)
        cv.rectangle(img,(540,518-3),(545,518+3),(0,0,255),-1)
        cv.rectangle(img,(445,472-3),(450,472+3),(0,0,255),-1)
        cv.rectangle(img,(445,488-3),(450,488+3),(0,0,255),-1)
    if(f == 1):
        cv.rectangle(img,(773-3,445),(773+3,450),(0,0,255),-1)
        cv.rectangle(img,(788-3,445),(788+3,450),(0,0,255),-1)
        cv.rectangle(img,(810,503-3),(815,503+3),(0,0,255),-1)
        cv.rectangle(img,(810,518-3),(815,518+3),(0,0,255),-1)
        cv.rectangle(img,(742-3,540),(742+3,545),(0,0,255),-1)
        cv.rectangle(img,(757-3,540),(757+3,545),(0,0,255),-1)
    elif(f == 2):
        cv.rectangle(img,(715,472-3),(720,472+3),(0,0,255),-1)
        cv.rectangle(img,(715,488-3),(720,488+3),(0,0,255),-1)
        cv.rectangle(img,(810,503-3),(815,503+3),(0,0,255),-1)
        cv.rectangle(img,(810,518-3),(815,518+3),(0,0,255),-1)
        cv.rectangle(img,(742-3,540),(742+3,545),(0,0,255),-1)
        cv.rectangle(img,(757-3,540),(757+3,545),(0,0,255),-1)
    elif(f == 3):
        cv.rectangle(img,(773-3,445),(773+3,450),(0,0,255),-1)
        cv.rectangle(img,(788-3,445),(788+3,450),(0,0,255),-1)
        cv.rectangle(img,(715,472-3),(720,472+3),(0,0,255),-1)
        cv.rectangle(img,(715,488-3),(720,488+3),(0,0,255),-1)
        cv.rectangle(img,(742-3,540),(742+3,545),(0,0,255),-1)
        cv.rectangle(img,(757-3,540),(757+3,545),(0,0,255),-1)
    elif(f == 4):
        cv.rectangle(img,(773-3,445),(773+3,450),(0,0,255),-1)
        cv.rectangle(img,(788-3,445),(788+3,450),(0,0,255),-1)
        cv.rectangle(img,(810,503-3),(815,503+3),(0,0,255),-1)
        cv.rectangle(img,(810,518-3),(815,518+3),(0,0,255),-1)
        cv.rectangle(img,(715,472-3),(720,472+3),(0,0,255),-1)
        cv.rectangle(img,(715,488-3),(720,488+3),(0,0,255),-1)
    
    
global p,q,r,s,t,u
global speed,window
speed = 'Speed'
window = 'Window'

class junc(object):
    def __init__(self,noc,rno):
        self.noc = noc
        self.rno = rno
        return
    def __cmp__(self, other):
        return cmp(self.noc, other.noc)

def movcar():
    ite = 0
    p =1
    q =1
    r =1
    s =1
    t =1
    u =1
    q1 = Q.PriorityQueue()
    q2 = Q.PriorityQueue()
    q3 = Q.PriorityQueue()
    q4 = Q.PriorityQueue()
    q5 = Q.PriorityQueue()
    q6 = Q.PriorityQueue()
    count = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    while(True):
        #junction1
	if (cv.waitKey(1)== 32):
		while(True):
			if (cv.waitKey(1)== 32):
				break
	if(cv.waitKey(1)== 27):
		break
        #dalai code
	sibu.send('Hello')
	goku = str(sibu.recv(150))
	l=list(goku)
	a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	#print len(a)
	#[990, 472, 788, 0, 1, 3, 0, 2, 0, 0,[[200, 200, 200, 200, 200], [200, 4, 3, 2, 200], [200, 3, 2, 1, 0], [200, 200, 200, 200, 200]]]
	c=0
	for i in range(len(l)):
	    l[i]=ord(l[i])- 48
	    if (l[i]==-1 or l[i]==-6):
	        c=c+1
      	    else :
        	a[c]=a[c]*10+l[i]
    
        #print a

	rows=4
	columns=5

	new_a = [[0 for x in range(columns)] for x in range(rows)]
	c=10
	for j in range(rows):
 	    for i in range(columns):
 	       new_a[j][i]=a[c]
 	       c=c+1
	
	for i in range(10,30):
	    a.pop(10)
	a.append(new_a)
	#print a
	if(a[0]!=0 and a[1] !=0):
		car_mat.append(a)

        if((ite-1)%50 ==0):
            #junction1
            q1.put(junc(-float(weight_hor_lr_mat[0][0])/count[0][0],1))
            q1.put(junc(-float(weight_ver_ud_mat[0][0])/count[0][1],2))
            q1.put(junc(-float(weight_hor_rl_mat[0][1])/count[0][2],3))
            q1.put(junc(-float(weight_ver_du_mat[1][0])/count[0][3],4))
            #junction2
            
            q2.put(junc(-float(weight_hor_lr_mat[0][1])/count[1][0],1))
            q2.put(junc(-float(weight_ver_ud_mat[0][1])/count[1][1],2))
            q2.put(junc(-float(weight_hor_rl_mat[0][2])/count[1][2],3))
            q2.put(junc(-float(weight_ver_du_mat[1][1])/count[1][3],4))
            #junction3
            
            q3.put(junc(-float(weight_hor_lr_mat[0][2])/count[2][0],1))
            q3.put(junc(-float(weight_ver_ud_mat[0][2])/count[2][1],2))
            q3.put(junc(-float(weight_hor_rl_mat[0][3])/count[2][2],3))
            q3.put(junc(-float(weight_ver_du_mat[1][2])/count[2][3],4))
            #junction4
            
            q4.put(junc(-float(weight_hor_lr_mat[1][0])/count[3][0],1))
            q4.put(junc(-float(weight_ver_ud_mat[1][0])/count[3][1],2))
            q4.put(junc(-float(weight_hor_rl_mat[1][1])/count[3][2],3))
            q4.put(junc(-float(weight_ver_du_mat[2][0])/count[3][3],4))
            #junction5
            
            q5.put(junc(-float(weight_hor_lr_mat[1][1])/count[4][0],1))
            q5.put(junc(-float(weight_ver_ud_mat[1][1])/count[4][1],2))
            q5.put(junc(-float(weight_hor_rl_mat[1][2])/count[4][2],3))
            q5.put(junc(-float(weight_ver_du_mat[2][1])/count[4][3],4))
            #junction6
            
            q6.put(junc(-float(weight_hor_lr_mat[1][2])/count[5][0],1))
            q6.put(junc(-float(weight_ver_ud_mat[1][2])/count[5][1],2))
            q6.put(junc(-float(weight_hor_rl_mat[1][3])/count[5][2],3))
            q6.put(junc(-float(weight_ver_du_mat[2][2])/count[5][3],4))
            
            #if(q1.empty()!=1 and q2.empty()!=1 and q3.empty()!=1 and q4.empty()!=1 and q5.empty()!=1 and q6.empty()!=1):
            p = q1.get().rno
            while not q1.empty():
                q1.get()
            q = q2.get().rno
            while not q2.empty():
                q2.get()
            r = q3.get().rno
            while not q3.empty():
                q3.get()
            s = q4.get().rno
            while not q4.empty():
                q4.get()
            t = q5.get().rno
            while not q5.empty():
                q5.get()
            u = q6.get().rno
            while not q6.empty():
                q6.get()
            count[0][p-1] = ite
            count[1][q-1] = ite
            count[2][r-1] = ite
            count[3][s-1] = ite
            count[4][t-1] = ite
            count[5][u-1] = ite
                

        #print p,q,r,s,t,u    
        drawlights(p,q,r,s,t,u)

        if(ite>=((ite/50)*50+1) and ite<=((ite/50)*50+15)):
                if(p == 1):
                    cv.rectangle(img,(175,202-3),(180,202+3),(0,255,255),-1)
                    cv.rectangle(img,(175,217-3),(180,217+3),(0,255,255),-1)
                elif(p == 2):
                    cv.rectangle(img,(233-3,175),(233+3,180),(0,255,255),-1)
                    cv.rectangle(img,(248-3,175),(248+3,180),(0,255,255),-1)
                elif(p == 3):
                    cv.rectangle(img,(270,233-3),(275,233+3),(0,255,255),-1)
                    cv.rectangle(img,(270,248-3),(275,248+3),(0,255,255),-1)
                elif(p == 4):
                    cv.rectangle(img,(202-3,270),(202+3,275),(0,255,255),-1)
                    cv.rectangle(img,(217-3,270),(217+3,275),(0,255,255),-1)
                if(q == 1):
                    cv.rectangle(img,(445,202-3),(450,202+3),(0,255,255),-1)
                    cv.rectangle(img,(445,217-3),(450,217+3),(0,255,255),-1)
                elif(q == 2):
                    cv.rectangle(img,(503-3,175),(503+3,180),(0,255,255),-1)
                    cv.rectangle(img,(518-3,175),(518+3,180),(0,255,255),-1)
                elif(q == 3):
                    cv.rectangle(img,(540,233-3),(545,233+3),(0,255,255),-1)
                    cv.rectangle(img,(540,248-3),(545,248+3),(0,255,255),-1)
                elif(q == 4):
                    cv.rectangle(img,(472-3,270),(472+3,275),(0,255,255),-1)
                    cv.rectangle(img,(487-3,270),(487+3,275),(0,255,255),-1)
                if(r == 1):
                    cv.rectangle(img,(715,202-3),(720,202+3),(0,255,255),-1)
                    cv.rectangle(img,(715,217-3),(720,217+3),(0,255,255),-1)
                elif(r == 2):
                    cv.rectangle(img,(773-3,175),(773+3,180),(0,255,255),-1)
                    cv.rectangle(img,(788-3,175),(788+3,180),(0,255,255),-1)
                elif(r == 3):
                    cv.rectangle(img,(810,233-3),(815,233+3),(0,255,255),-1)
                    cv.rectangle(img,(810,248-3),(815,248+3),(0,255,255),-1)
                elif(r == 4):
                    cv.rectangle(img,(742-3,270),(742+3,275),(0,255,255),-1)
                    cv.rectangle(img,(757-3,270),(757+3,275),(0,255,255),-1)
                if(s == 1):
                    cv.rectangle(img,(175,472-3),(180,472+3),(0,255,255),-1)
                    cv.rectangle(img,(175,488-3),(180,488+3),(0,255,255),-1)
                elif(s == 2):
                    cv.rectangle(img,(233-3,445),(233+3,450),(0,255,255),-1)
                    cv.rectangle(img,(248-3,445),(248+3,450),(0,255,255),-1)
                elif(s == 3):
                    cv.rectangle(img,(270,503-3),(275,503+3),(0,255,255),-1)
                    cv.rectangle(img,(270,518-3),(275,518+3),(0,255,255),-1)
                elif(s == 4):
                    cv.rectangle(img,(202-3,540),(202+3,545),(0,255,255),-1)
                    cv.rectangle(img,(217-3,540),(217+3,545),(0,255,255),-1)
                if(t == 1):
                    cv.rectangle(img,(445,472-3),(450,472+3),(0,255,255),-1)
                    cv.rectangle(img,(445,488-3),(450,488+3),(0,255,255),-1)
                elif(t == 2):
                    cv.rectangle(img,(503-3,445),(503+3,450),(0,255,255),-1)
                    cv.rectangle(img,(518-3,445),(518+3,450),(0,255,255),-1)
                elif(t == 3):
                    cv.rectangle(img,(540,503-3),(545,503+3),(0,255,255),-1)
                    cv.rectangle(img,(540,518-3),(545,518+3),(0,255,255),-1)
                elif(t == 4):
                    cv.rectangle(img,(472-3,540),(472+3,545),(0,255,255),-1)
                    cv.rectangle(img,(487-3,540),(487+3,545),(0,255,255),-1)
                if(u == 1):
                    cv.rectangle(img,(715,472-3),(720,472+3),(0,255,255),-1)
                    cv.rectangle(img,(715,488-3),(720,488+3),(0,255,255),-1)
                elif(u == 2):
                    cv.rectangle(img,(773-3,445),(773+3,450),(0,255,255),-1)
                    cv.rectangle(img,(788-3,445),(788+3,450),(0,255,255),-1)
                elif(u == 3):
                    cv.rectangle(img,(810,503-3),(815,503+3),(0,255,255),-1)
                    cv.rectangle(img,(810,518-3),(815,518+3),(0,255,255),-1)
                elif(u == 4):
                    cv.rectangle(img,(742-3,540),(742+3,545),(0,255,255),-1)
                    cv.rectangle(img,(757-3,540),(757+3,545),(0,255,255),-1)
                    

                
        #print 1
            
        """print weight_ver_ud_mat
        print 2
        print weight_hor_rl_mat
        print 3
        print weight_ver_du_mat
        print 4"""
	cv.namedWindow(window)
	cv.createTrackbar(speed,window,1,50,nothing)
	spd = cv.getTrackbarPos(speed,window)
        cv.waitKey(spd)
        
        for i in range(len(car_mat)):
            drawmotaline()
            drawhorline(0)
            drawhorline(270)
            drawhorline(540)
            drawhorline(810)
            drawverline(0)
            drawverline(270)
            drawverline(540)
            endx = car_mat[i][0]
            endy = car_mat[i][1]
            curx = car_mat[i][2]
            cury = car_mat[i][3]
            state = car_mat[i][4]
            dirn = car_mat[i][5]
            pathmatrix = car_mat[i][10]
	    #print pathmatrix
            startangle = car_mat[i][6]
            lane = car_mat[i][7]
            lanestate = car_mat[i][8]
            sf = car_mat[i][9]
            if(state == 1):
                if(dirn == 2 and (curx == 180-15 or curx == 450-15 or curx == 720-15)):
                    gridx = (curx+90+15)/270
                    gridy = (cury+90)/270
                    if(pathmatrix !=0):
		            if(pathmatrix[gridy-1][gridx]<pathmatrix[gridy][gridx]):
		                if(img[cury][curx+15+5][0] == 105 and img[cury-3][curx+15+5][0] == 105 and img[cury+3][curx+15+5][0] == 105):
		                    wx = curx/270
		                    wy = cury/270
		                    weight_hor_lr_mat[wy][wx] -= 1
		                    
		                    state = 2
		                    startangle = 90
		                    cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(105,105,105),-1)
		            elif(pathmatrix[gridy][gridx+1]<pathmatrix[gridy][gridx]):
		                """"""
		                if(img[cury][curx+15+5][0] == 105 and img[cury-3][curx+15+5][0] == 105 and img[cury+3][curx+15+5][0] == 105):
		                    state = 1
		                    wx = curx/270
		                    wy = cury/270
		                    weight_hor_lr_mat[wy][wx] -= 1
		                    cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(105,105,105),-1)
		                    curx = curx+5
		                    cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(255,0,0),-1)
		                    
		            elif(pathmatrix[gridy+1][gridx]<pathmatrix[gridy][gridx]):
		                """"""
		                if(img[cury][curx+15+5][0] == 105 and img[cury-3][curx+15+5][0] == 105 and img[cury+3][curx+15+5][0] == 105):
		                    wx = curx/270
		                    wy = cury/270
		                    weight_hor_lr_mat[wy][wx] -= 1
		                    state = 3
		                    startangle = 270
		                    cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(105,105,105),-1)
		                
                elif(dirn == 3 and (cury == 180-15 or cury == 450-15)):
                    gridx = (curx+90)/270
                    gridy = (cury+90+15)/270
                    
                    if(pathmatrix[gridy][gridx+1]<pathmatrix[gridy][gridx]):
                        if(img[cury+15+5][curx][0] == 105 and img[cury+15+5][curx-3][0] == 105 and img[cury+15+5][curx+3][0] == 105):
                            wx = curx/270
                            wy = cury/270
                            weight_ver_ud_mat[wy][wx] -= 1
                            state = 2
                            startangle = 180
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(105,105,105),-1)
                    elif(pathmatrix[gridy+1][gridx]<pathmatrix[gridy][gridx]):
                        
                        if(img[cury+15+5][curx][0] == 105 and img[cury+15+5][curx-3][0] == 105 and img[cury+15+5][curx+3][0] == 105):
                            wx = curx/270
                            wy = cury/270
                            weight_ver_ud_mat[wy][wx] -= 1
                            state = 1
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(105,105,105),-1)
                            cury = cury+5
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(255,0,0),-1)
                    elif(pathmatrix[gridy][gridx-1]<pathmatrix[gridy][gridx]):
                        if(img[cury+15+5][curx][0] == 105 and img[cury+15+5][curx-3][0] == 105 and img[cury+15+5][curx+3][0] == 105):
                            wx = curx/270
                            wy = cury/270
                            weight_ver_ud_mat[wy][wx] -= 1
                            state = 3
                            startangle = 0
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(105,105,105),-1)

                elif(dirn == 4 and (curx == 270+15 or curx== 540+15 or curx == 810+15)):
                    gridx = curx/270
                    gridy = (cury+90)/270
                    if(pathmatrix[gridy+1][gridx]<pathmatrix[gridy][gridx]):
                        if(img[cury][curx-15-5][0] == 105 and img[cury-3][curx-15-5][0] == 105 and img[cury+3][curx-15-5][0] == 105):
                            wx = curx/270
                            wy = cury/270
                            weight_hor_rl_mat[wy][wx] -= 1
                            state = 2
                            startangle = 270
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(105,105,105),-1)
                    elif(pathmatrix[gridy][gridx-1]<pathmatrix[gridy][gridx]):
                        
                        if(img[cury][curx-15-5][0] == 105 and img[cury-3][curx-15-5][0] == 105 and img[cury+3][curx-15-5][0] == 105):
                            wx = curx/270
                            wy = cury/270
                            weight_hor_rl_mat[wy][wx] -= 1
                            state = 1
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(105,105,105),-1)
                            curx = curx-5
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(255,0,0),-1)
                    elif(pathmatrix[gridy-1][gridx]<pathmatrix[gridy][gridx]):
                        if(img[cury][curx-15-5][0] == 105 and img[cury-3][curx-15-5][0] == 105 and img[cury+3][curx-15-5][0] == 105):
                            wx = curx/270
                            wy = cury/270
                            weight_hor_rl_mat[wy][wx] -= 1
                            state = 3
                            startangle =90
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(105,105,105),-1)
                        
                        
                elif(dirn == 1 and (cury == 270+15 or cury== 540+15)):
                    gridx = (curx+90)/270
                    gridy = cury/270
                    if(pathmatrix[gridy][gridx-1]<pathmatrix[gridy][gridx]):
                        if(img[cury-15-5][curx][0] == 105 and img[cury-15-5][curx-3][0] == 105 and img[cury-15-5][curx+3][0] == 105):
                            wx = curx/270
                            wy = cury/270
                            weight_ver_du_mat[wy][wx] -= 1
                            state = 2
                            startangle = 360
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(105,105,105),-1)
                        
                    elif(pathmatrix[gridy-1][gridx]<pathmatrix[gridy][gridx]):
                        
                        if(img[cury-15-5][curx][0] == 105 and img[cury-15-5][curx-3][0] == 105 and img[cury-15-5][curx+3][0] == 105):
                            wx = curx/270
                            wy = cury/270
                            weight_ver_du_mat[wy][wx] -= 1
                            state = 1
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(105,105,105),-1)
                            cury = cury-5
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(255,0,0),-1)
                             
                    elif(pathmatrix[gridy][gridx+1]<pathmatrix[gridy][gridx]):
                        if(img[cury-15-5][curx][0] == 105 and img[cury-15-5][curx-3][0] == 105 and img[cury-15-5][curx+3][0] == 105):
                            wx = curx/270
                            wy = cury/270
                            weight_ver_du_mat[wy][wx] -= 1
                            state = 3
                            startangle = 180
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(105,105,105),-1)
                            
                elif(dirn == 2):
                    if(curx ==0 and sf ==0):
                        wx = curx/270;
                        wy = cury/270;
                        weight_hor_lr_mat[wy][wx] += 1
                        sf =1
                    if((curx == 270 or curx == 540 or curx == 810)):
                        wx = curx/270;
                        wy = cury/270;
                        weight_hor_lr_mat[wy][wx] += 1
                    if(curx+15+5 == 990):
                        cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(105,105,105),-1)
                        state = 6
                    
                        
                    elif(img[cury][curx+15+5][0] == 105 and img[cury-3][curx+15+5][0] == 105 and img[cury+3][curx+15+5][0] == 105):
                        
                        if(endy>cury+45 and lane!=1 and img[cury+15][curx-5][0] == 105 and img[cury+15][curx+5][0]==105 and img[cury+15][curx+20][0]==105 and img[cury+15][curx+35][0]==105 and img[cury+15][curx+50][0]==105 and img[cury+15][curx+60][0]==105 and curx <= ((curx/270)*270)+120):
                            state = 5
                            lanestate = 1
                        elif(endy<cury-45 and lane!=3 and img[cury-15][curx-5][0] == 105 and img[cury-15][curx+5][0]==105 and img[cury-15][curx+20][0]==105 and img[cury-15][curx+35][0]==105 and img[cury-15][curx+50][0]==105 and img[cury-15][curx+60][0]==105 and curx <= ((curx/270)*270)+120):
                            state = 4
                            lanestate = 1
                        else:
                            cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(105,105,105),-1)
                            curx = curx+5
                            cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(255,0,0),-1)
                    else:
                        if(endy>cury+45 and lane!=1 and img[cury+15][curx-5][0] == 105 and img[cury+15][curx+5][0]==105 and img[cury+15][curx+20][0]==105 and img[cury+15][curx+35][0]==105 and img[cury+15][curx+50][0]==105 and img[cury+15][curx+60][0]==105 and curx <= ((curx/270)*270)+120):
                            state = 5
                            lanestate = 1
                        elif(endy<cury-45 and lane!=3 and img[cury-15][curx-5][0] == 105 and img[cury-15][curx+5][0]==105 and img[cury-15][curx+20][0]==105 and img[cury-15][curx+35][0]==105 and img[cury-15][curx+50][0]==105 and img[cury-15][curx+60][0]==105 and curx <= ((curx/270)*270)+120):
                            state = 4
                            lanestate = 1
                        
                        
                elif(dirn == 3):
                    if(cury == 0 and sf == 0):
                        wx = curx/270;
                        wy = cury/270;
                        weight_ver_ud_mat[wy][wx] += 1
                        sf =1
                    if((cury == 270 or cury == 540)):
                        wx = curx/270;
                        wy = cury/270;
                        weight_ver_ud_mat[wy][wx] += 1
                    if((cury == 5 or cury == 275 or cury == 545) and sf == 1):
                        sf = 0
                    if(cury+15 == 705):
                        cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(105,105,105),-1)
                        state = 6
                    elif(img[cury+15+5][curx][0] == 105 and img[cury+15+5][curx-3][0] == 105 and img[cury+15+5][curx+3][0] == 105):
                        if(endx>curx+45 and lane!=3 and img[cury-5][curx+15][0] == 105 and img[cury+5][curx+15][0]==105 and img[cury+20][curx+15][0]==105 and img[cury+35][curx+15][0]==105 and img[cury+50][curx+15][0]==105 and img[cury+60][curx+15][0]==105 and cury <= ((cury/270)*270)+120):
                            state = 4
                            lanestate = 1
                        elif(endx<curx-45 and lane!=1 and img[cury-5][curx-15][0] == 105 and img[cury+5][curx-15][0]==105 and img[cury+20][curx-15][0]==105 and img[cury+35][curx-15][0]==105 and img[cury+50][curx-15][0]==105 and img[cury+60][curx-15][0]==105 and cury <= ((cury/270)*270)+120):
                            state = 5
                            lanestate = 1
                        else:
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(105,105,105),-1)
                            cury = cury+5
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(255,0,0),-1)
                    else:
                        if(endx>curx+45 and lane!=3 and img[cury-5][curx+15][0] == 105 and img[cury+5][curx+15][0]==105 and img[cury+20][curx+15][0]==105 and img[cury+35][curx+15][0]==105 and img[cury+50][curx+15][0]==105 and img[cury+60][curx+15][0]==105 and cury <= ((cury/270)*270)+120):
                            state = 4
                            lanestate = 1
                        elif(endx<curx-45 and lane!=1 and img[cury-5][curx-15][0] == 105 and img[cury+5][curx-15][0]==105 and img[cury+20][curx-15][0]==105 and img[cury+35][curx-15][0]==105 and img[cury+50][curx-15][0]==105 and img[cury+60][curx-15][0]==105 and cury <= ((cury/270)*270)+120):
                            state = 5
                            lanestate = 1
                        
                elif(dirn == 4):
                    if(curx == 990 and sf ==0):
                        wx = curx/270;
                        wy = cury/270;
                        weight_hor_rl_mat[wy][wx] += 1
                        sf =1
                        
                    if((curx == 720 or curx == 450 or curx == 180)):
                        wx = curx/270;
                        wy = cury/270;
                        weight_hor_rl_mat[wy][wx] += 1
                    if((curx == 985 or curx == 715 or curx == 445 or curx == 175) and sf ==1):
                        sf = 0
                    if(curx-15 == 0):
                        cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(105,105,105),-1)
                        state = 6
                    elif(curx == 990):
                        cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(105,105,105),-1)
                        curx = curx-5
                        cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(255,0,0),-1)
                    elif(img[cury][curx-15-5][0] == 105 and img[cury-3][curx-15-5][0] == 105 and img[cury+3][curx-15-5][0] == 105):
                        if(endy<cury-45 and lane!=1 and img[cury+15][curx][0] == 105 and img[cury+15][curx-5][0]==105 and img[cury+15][curx-20][0]==105 and img[cury+15][curx-35][0]==105 and img[cury+15][curx-50][0]==105 and img[cury+15][curx-60][0]==105 and curx >= ((curx/270)*270)+60):
                            state = 5
                            lanestate = 1
                        elif(endy>cury+45 and lane!=3 and img[cury-15][curx][0] == 105 and img[cury-15][curx-5][0]==105 and img[cury-15][curx-20][0]==105 and img[cury-15][curx-35][0]==105 and img[cury-15][curx-50][0]==105 and img[cury-15][curx-60][0]==105 and curx >= ((curx/270)*270)+60):
                            state = 4
                            lanestate = 1
                        else:
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(105,105,105),-1)
                            curx = curx-5
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(255,0,0),-1)
                    else:
                        if(endy<cury-45 and lane!=1 and img[cury+15][curx][0] == 105 and img[cury+15][curx-5][0]==105 and img[cury+15][curx-20][0]==105 and img[cury+15][curx-35][0]==105 and img[cury+15][curx-50][0]==105 and img[cury+15][curx-60][0]==105 and curx >= ((curx/270)*270)+60):
                            state = 5
                            lanestate = 1
                        elif(endy>cury+45 and lane!=3 and img[cury-15][curx][0] == 105 and img[cury-15][curx-5][0]==105 and img[cury-15][curx-20][0]==105 and img[cury-15][curx-35][0]==105 and img[cury-15][curx-50][0]==105 and img[cury-15][curx-60][0]==105 and curx >= ((curx/270)*270)+60):
                            state = 4
                            lanestate = 1
                        
                elif(dirn == 1):
                    if(cury == 720 and sf == 0):
                        wx = curx/270;
                        wy = cury/270;
                        weight_ver_du_mat[wy][wx] += 1
                        sf = 1
                    if((cury == 450 or cury == 180)):
                        wx = curx/270;
                        wy = cury/270;
                        weight_ver_du_mat[wy][wx] += 1
                    if(cury-15 == 0):
                        cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(105,105,105),-1)
                        state = 6
                    elif(cury==720):
                        cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(105,105,105),-1)
                        cury = cury-5
                        cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(255,0,0),-1)
                    elif(img[cury-15-5][curx][0] == 105 and img[cury-15-5][curx-3][0] == 105 and img[cury-15-5][curx+3][0] == 105):
                        
                        if(endx<curx-45 and lane!=3 and img[cury][curx-15][0] == 105 and img[cury-5][curx-15][0]==105 and img[cury-20][curx-15][0]==105 and img[cury-35][curx-15][0]==105 and img[cury-50][curx-15][0]==105 and img[cury-60][curx-15][0]==105 and cury >= ((cury/270)*270)+60):
                            state = 4
                            lanestate = 1
                        elif(endx>curx+45 and lane!=1 and img[cury][curx+15][0] == 105 and img[cury-5][curx+15][0]==105 and img[cury-20][curx+15][0]==105 and img[cury-35][curx+15][0]==105 and img[cury-50][curx+15][0]==105 and img[cury-60][curx+15][0]==105 and curx >= ((curx/270)*270)+60):
                            state = 5

                            lanestate = 1
                        else:
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(105,105,105),-1)
                            cury = cury-5
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(255,0,0),-1)
                    else:
                        if(endx<curx-45 and lane!=3 and img[cury][curx-15][0] == 105 and img[cury-5][curx-15][0]==105 and img[cury-20][curx-15][0]==105 and img[cury-35][curx-15][0]==105 and img[cury-50][curx-15][0]==105 and img[cury-60][curx-15][0]==105 and curx >= ((curx/270)*270)+60):
                            state = 4
                            lanestate = 1
                        elif(endx>curx+45 and lane!=1 and img[cury][curx+15][0] == 105 and img[cury-5][curx+15][0]==105 and img[cury-20][curx+15][0]==105 and img[cury-35][curx+15][0]==105 and img[cury-50][curx+15][0]==105 and img[cury-60][curx+15][0]==105 and curx >= ((curx/270)*270)+60):
                            state = 5
                            lanestate = 1
                        
                
            elif(state == 3):
                if(dirn == 2):
                    if(lane == 1):
                        if(startangle == 270):
                            
                            cv.ellipse(img,(curx+15,cury+46+7),(53,53),0, startangle,startangle+15,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx+15,cury+46+7),(53,53),0, startangle,startangle+15,(255,0,0), 6)
                        elif(startangle+15 == 360):
                            cv.ellipse(img,(curx+15,cury+46+7),(53,53),0, startangle,startangle+15,(105,105,105), 6)
                            curx = curx+15+46+7
                            cury = cury+7+46
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(255,0,0),-1)
                            state = 1
                            dirn = 3
                            lane = 1
                        elif(startangle>270 and startangle+15<360):
                            cv.ellipse(img,(curx+15,cury+46+7),(53,53),0, startangle,startangle+15,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx+15,cury+46+7),(53,53),0, startangle,startangle+15,(255,0,0), 6)
                    elif(lane == 2):
                        if(startangle == 270):
                            
                            cv.ellipse(img,(curx+15,cury+46+22),(68,68),0, startangle,startangle+10,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx+15,cury+46+22),(68,68),0, startangle,startangle+10,(255,0,0), 6)
                        elif(startangle+10 == 360):
                            cv.ellipse(img,(curx+15,cury+46+22),(68,68),0, startangle,startangle+10,(105,105,105), 6)
                            curx = curx+15+46+22
                            cury = cury+22+46
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(255,0,0),-1)
                            state = 1
                            dirn = 3
                            lane = 2
                        elif(startangle>270 and startangle+10<360):
                            cv.ellipse(img,(curx+15,cury+46+22),(68,68),0, startangle,startangle+10,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx+15,cury+46+22),(68,68),0, startangle,startangle+10,(255,0,0), 6)
                    elif(lane == 3):
                        if(startangle == 270):
                            
                            cv.ellipse(img,(curx+15,cury+46+37),(83,83),0, startangle,startangle+5,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx+15,cury+46+37),(83,83),0, startangle,startangle+5,(255,0,0), 6)
                        elif(startangle+5 == 360):
                            cv.ellipse(img,(curx+15,cury+46+37),(83,83),0, startangle,startangle+5,(105,105,105), 6)
                            curx = curx+15+46+37
                            cury = cury+37+46
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(255,0,0),-1)
                            state = 1
                            dirn = 3
                            lane = 3
                        elif(startangle>270 and startangle+5<360):
                            cv.ellipse(img,(curx+15,cury+46+37),(83,83),0, startangle,startangle+5,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx+15,cury+46+37),(83,83),0, startangle,startangle+5,(255,0,0), 6)
                    
                elif(dirn == 3):
                    if(lane == 1):
                        if(startangle == 0):
                            cv.ellipse(img,(curx-46-7,cury+15),(53,53),0, startangle,startangle+15,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx-46-7,cury+15),(53,53),0, startangle,startangle+15,(255,0,0), 6)
                        elif(startangle+15 == 90):
                            cv.ellipse(img,(curx-46-7,cury+15),(53,53),0, startangle,startangle+15,(105,105,105), 6)
                            curx = curx-7-46
                            cury = cury+7+46+15
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(255,0,0),-1)
                            state = 1
                            dirn = 4
                            lane = 1
                        elif(startangle>0 and startangle+15<90):
                            cv.ellipse(img,(curx-46-7,cury+15),(53,53),0, startangle,startangle+15,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx-46-7,cury+15),(53,53),0, startangle,startangle+15,(255,0,0), 6)

                    elif(lane == 2):
                        if(startangle == 0):
                            cv.ellipse(img,(curx-46-22,cury+15),(68,68),0, startangle,startangle+10,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx-46-22,cury+15),(68,68),0, startangle,startangle+10,(255,0,0), 6)
                        elif(startangle+10 == 90):
                            cv.ellipse(img,(curx-46-22,cury+15),(68,68),0, startangle,startangle+10,(105,105,105), 6)
                            curx = curx-22-46
                            cury = cury+22+46+15
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(255,0,0),-1)
                            state = 1
                            dirn = 4
                            lane = 2
                        elif(startangle>0 and startangle+10<90):
                            cv.ellipse(img,(curx-46-22,cury+15),(68,68),0, startangle,startangle+10,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx-46-22,cury+15),(68,68),0, startangle,startangle+10,(255,0,0), 6)

                    elif(lane == 3):
                        if(startangle == 0):
                            
                            cv.ellipse(img,(curx-46-37,cury+15),(83,83),0, startangle,startangle+5,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx-46-37,cury+15),(83,83),0, startangle,startangle+5,(255,0,0), 6)
                        elif(startangle+5 == 90):
                            cv.ellipse(img,(curx-46-37,cury+15),(83,83),0, startangle,startangle+5,(105,105,105), 6)
                            curx = curx-46-37
                            cury = cury+37+46+15
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(255,0,0),-1)
                            state = 1
                            dirn = 4
                            lane = 3
                        elif(startangle>0 and startangle+5<90):
                            cv.ellipse(img,(curx-46-37,cury+15),(83,83),0, startangle,startangle+5,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx-46-37,cury+15),(83,83),0, startangle,startangle+5,(255,0,0), 6)            
                        
                elif(dirn == 4):
                    if(lane == 1):
                        if(startangle == 90):
                            cv.ellipse(img,(curx-15,cury-46-7),(53,53),0, startangle,startangle+15,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx-15,cury-46-7),(53,53),0, startangle,startangle+15,(255,0,0), 6)
                        elif(startangle+15 == 180):
                            cv.ellipse(img,(curx-15,cury-46-7),(53,53),0, startangle,startangle+15,(105,105,105), 6)
                            curx = curx-7-46-15
                            cury = cury-7-46
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(255,0,0),-1)
                            state = 1
                            dirn = 1
                            lane = 1
                        elif(startangle>90 and startangle+15<180):
                            cv.ellipse(img,(curx-15,cury-46-7),(53,53),0, startangle,startangle+15,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx-15,cury-46-7),(53,53),0, startangle,startangle+15,(255,0,0), 6)

                    elif(lane == 2):
                        if(startangle == 90):
                            cv.ellipse(img,(curx-15,cury-46-22),(68,68),0, startangle,startangle+10,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx-15,cury-46-22),(68,68),0, startangle,startangle+10,(255,0,0), 6)
                        elif(startangle+10 == 180):
                            cv.ellipse(img,(curx-15,cury-46-22),(68,68),0, startangle,startangle+10,(105,105,105), 6)
                            curx = curx-22-46-15
                            cury = cury-22-46
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(255,0,0),-1)
                            state = 1
                            dirn = 1
                            lane = 2
                        elif(startangle>90 and startangle+10<180):
                            cv.ellipse(img,(curx-15,cury-46-22),(68,68),0, startangle,startangle+10,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx-15,cury-46-22),(68,68),0, startangle,startangle+10,(255,0,0), 6)

                    elif(lane == 3):
                        if(startangle == 90):
                            cv.ellipse(img,(curx-15,cury-46-37),(83,83),0, startangle,startangle+5,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx-15,cury-46-37),(83,83),0, startangle,startangle+5,(255,0,0), 6)
                        elif(startangle+5 == 180):
                            cv.ellipse(img,(curx-15,cury-46-37),(83,83),0, startangle,startangle+5,(105,105,105), 6)
                            curx = curx-46-37-15
                            cury = cury-46-37
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(255,0,0),-1)
                            state = 1
                            dirn = 1
                            lane = 3
                        elif(startangle>90 and startangle+5<180):
                            cv.ellipse(img,(curx-15,cury-46-37),(83,83),0, startangle,startangle+5,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx-15,cury-46-37),(83,83),0, startangle,startangle+5,(255,0,0), 6)            
                     
                elif(dirn == 1):
                    if(lane == 1):
                        if(startangle == 180):
                            cv.ellipse(img,(curx+46+7,cury-15),(53,53),0, startangle,startangle+15,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx+46+7,cury-15),(53,53),0, startangle,startangle+15,(255,0,0), 6)
                        elif(startangle+15 == 270):
                            cv.ellipse(img,(curx+46+7,cury-15),(53,53),0, startangle,startangle+15,(105,105,105), 6)
                            curx = curx+7+46
                            cury = cury-7-46-15
                            cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(255,0,0),-1)
                            state = 1
                            dirn = 2
                            lane = 1
                        elif(startangle>180 and startangle+15<270):
                            cv.ellipse(img,(curx+46+7,cury-15),(53,53),0, startangle,startangle+15,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx+46+7,cury-15),(53,53),0, startangle,startangle+15,(255,0,0), 6)

                    elif(lane == 2):
                        if(startangle == 180):
                            cv.ellipse(img,(curx+46+22,cury-15),(68,68),0, startangle,startangle+10,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx+46+22,cury-15),(68,68),0, startangle,startangle+10,(255,0,0), 6)
                        elif(startangle+10 == 270):
                            cv.ellipse(img,(curx+46+22,cury-15),(68,68),0, startangle,startangle+10,(105,105,105), 6)
                            curx = curx+22+46
                            cury = cury-22-46-15
                            cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(255,0,0),-1)
                            state = 1
                            dirn = 2
                            lane = 2
                        elif(startangle>180 and startangle+10<270):
                            cv.ellipse(img,(curx+46+22,cury-15),(68,68),0, startangle,startangle+10,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx+46+22,cury-15),(68,68),0, startangle,startangle+10,(255,0,0), 6)

                    elif(lane == 3):
                        if(startangle ==180):
                            
                            cv.ellipse(img,(curx+46+37,cury-15),(83,83),0, startangle,startangle+5,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx+46+37,cury-15),(83,83),0, startangle,startangle+5,(255,0,0), 6)
                        elif(startangle+5 ==270):
                            cv.ellipse(img,(curx+46+37,cury-15),(83,83),0, startangle,startangle+5,(105,105,105), 6)
                            curx = curx+37+46
                            cury = cury-46-37-15
                            cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(255,0,0),-1)
                            state = 1
                            dirn = 2
                            lane = 3
                        elif(startangle>180 and startangle+5<270):
                            cv.ellipse(img,(curx+46+37,cury-15),(83,83),0, startangle,startangle+5,(105,105,105), 6)
                            startangle = startangle+5
                            cv.ellipse(img,(curx+46+37,cury-15),(83,83),0, startangle,startangle+5,(255,0,0), 6)            
                     

            elif(state == 2):
                if(dirn == 2):
                    if(lane == 1):
                        if(startangle == 90):
                            cv.ellipse(img,(curx+15,cury-37),(37,37),0, startangle-15,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx+15,cury-37),(37,37),0, startangle-15,startangle,(255,0,0), 6)
                        elif(startangle-15 == 0):
                            cv.ellipse(img,(curx+15,cury-37),(37,37),0, startangle-15,startangle,(105,105,105), 6)
                            curx = curx+37+15
                            cury = cury-37
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(255,0,0),-1)
                            state = 1
                            dirn = 1
                            lane = 1
                        elif(startangle<90 and startangle-15>0):
                            cv.ellipse(img,(curx+15,cury-37),(37,37),0, startangle-15,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx+15,cury-37),(37,37),0, startangle-15,startangle,(255,0,0), 6)

                    elif(lane == 2):
                        if(startangle == 90):
                            cv.ellipse(img,(curx+15,cury-22),(22,22),0, startangle-30,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx+15,cury-22),(22,22),0, startangle-30,startangle,(255,0,0), 6)
                        elif(startangle-30 == 0):
                            cv.ellipse(img,(curx+15,cury-22),(22,22),0, startangle-30,startangle,(105,105,105), 6)
                            curx = curx+22+15
                            cury = cury-22
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(255,0,0),-1)
                            state = 1
                            dirn = 1
                            lane = 2
                        elif(startangle<90 and startangle-30>0):
                            cv.ellipse(img,(curx+15,cury-22),(22,22),0, startangle-30,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx+15,cury-22),(22,22),0, startangle-30,startangle,(255,0,0), 6)

                    elif(lane == 3):
                        if(startangle == 90):
                            cv.ellipse(img,(curx+15,cury-7),(7,7),0, startangle-60,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx+15,cury-7),(7,7),0, startangle-60,startangle,(255,0,0), 6)
                        elif(startangle-60 == 0):
                            cv.ellipse(img,(curx+15,cury-7),(7,7),0, startangle-60,startangle,(105,105,105), 6)
                            curx = curx+7+15
                            cury = cury-7
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(255,0,0),-1)
                            state = 1
                            dirn = 1
                            lane = 3
                        elif(startangle<90 and startangle-60>0):
                            cv.ellipse(img,(curx+15,cury-7),(7,7),0, startangle-60,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx+15,cury-7),(7,7),0, startangle-60,startangle,(255,0,0), 6)            
                    
                elif(dirn == 3):
                    if(lane == 1):
                        if(startangle == 180):
                            cv.ellipse(img,(curx+37,cury+15),(37,37),0, startangle-15,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx+37,cury+15),(37,37),0, startangle-15,startangle,(255,0,0), 6)
                        elif(startangle-15 == 90):
                            cv.ellipse(img,(curx+37,cury+15),(37,37),0, startangle-15,startangle,(105,105,105), 6)
                            curx = curx+37
                            cury = cury+15+37
                            cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(255,0,0),-1)
                            state = 1
                            dirn = 2
                            lane = 1
                        elif(startangle<180 and startangle-15>90):
                            cv.ellipse(img,(curx+37,cury+15),(37,37),0, startangle-15,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx+37,cury+15),(37,37),0, startangle-15,startangle,(255,0,0), 6)

                    elif(lane == 2):
                        if(startangle == 180):
                            cv.ellipse(img,(curx+22,cury+15),(22,22),0, startangle-30,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx+22,cury+15),(22,22),0, startangle-30,startangle,(255,0,0), 6)
                        elif(startangle-30 == 90):
                            cv.ellipse(img,(curx+22,cury+15),(22,22),0, startangle-30,startangle,(105,105,105), 6)
                            curx = curx+22
                            cury = cury+15+22
                            cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(255,0,0),-1)
                            state = 1
                            dirn = 2
                            lane = 2
                        elif(startangle<180 and startangle-30>90):
                            cv.ellipse(img,(curx+22,cury+15),(22,22),0, startangle-30,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx+22,cury+15),(22,22),0, startangle-30,startangle,(255,0,0), 6)

                    elif(lane == 3):
                        if(startangle == 180):
                            
                            cv.ellipse(img,(curx+7,cury+15),(7,7),0, startangle-60,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx+7,cury+15),(7,7),0, startangle-60,startangle,(255,0,0), 6)
                        elif(startangle-60 == 90):
                            cv.ellipse(img,(curx+7,cury+15),(7,7),0, startangle-60,startangle,(105,105,105), 6)
                            curx = curx+7
                            cury = cury+7+15
                            cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(255,0,0),-1)
                            state = 1
                            dirn = 2
                            lane = 3
                        elif(startangle<180 and startangle-60>90):
                            cv.ellipse(img,(curx+7,cury+15),(7,7),0, startangle-60,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx+7,cury+15),(7,7),0, startangle-60,startangle,(255,0,0), 6)            
                        
                elif(dirn == 4):
                    if(lane == 1):
                        if(startangle == 270):
                            cv.ellipse(img,(curx-15,cury+37),(37,37),0, startangle-15,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx-15,cury+37),(37,37),0, startangle-15,startangle,(255,0,0), 6)
                        elif(startangle-15 == 180):
                            cv.ellipse(img,(curx-15,cury+37),(37,37),0, startangle-15,startangle,(105,105,105), 6)
                            curx = curx-37-15
                            cury = cury+37
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(255,0,0),-1)
                            state = 1
                            dirn = 3
                            lane = 1
                        elif(startangle<270 and startangle-15>180):
                            cv.ellipse(img,(curx-15,cury+37),(37,37),0, startangle-15,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx-15,cury+37),(37,37),0, startangle-15,startangle,(255,0,0), 6)

                    elif(lane == 2):
                        if(startangle == 270):
                            cv.ellipse(img,(curx-15,cury+22),(22,22),0, startangle-30,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx-15,cury+22),(22,22),0, startangle-30,startangle,(255,0,0), 6)
                        elif(startangle-30 == 180):
                            cv.ellipse(img,(curx-15,cury+22),(22,22),0, startangle-30,startangle,(105,105,105), 6)
                            curx = curx-22-15
                            cury = cury+22
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(255,0,0),-1)
                            state = 1
                            dirn = 3
                            lane = 2
                        elif(startangle<270 and startangle-30>180):
                            cv.ellipse(img,(curx-15,cury+22),(22,22),0, startangle-30,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx-15,cury+22),(22,22),0, startangle-30,startangle,(255,0,0), 6)

                    elif(lane == 3):
                        if(startangle == 270):
                            
                            cv.ellipse(img,(curx-15,cury+7),(7,7),0, startangle-60,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx-15,cury+7),(7,7),0, startangle-60,startangle,(255,0,0), 6)
                        elif(startangle-60 == 180):
                            cv.ellipse(img,(curx-15,cury+7),(7,7),0, startangle-60,startangle,(105,105,105), 6)
                            curx = curx-7-15
                            cury = cury+7
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(255,0,0),-1)
                            state = 1
                            dirn = 3
                            lane = 3
                        elif(startangle<270 and startangle-60>180):
                            cv.ellipse(img,(curx-15,cury+7),(7,7),0, startangle-60,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx-15,cury+7),(7,7),0, startangle-60,startangle,(255,0,0), 6)            
                                        
                     
                elif(dirn == 1):
                    if(lane == 1):
                        if(startangle == 360):
                            cv.ellipse(img,(curx-37,cury-15),(37,37),0, startangle-15,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx-37,cury-15),(37,37),0, startangle-15,startangle,(255,0,0), 6)
                        elif(startangle-15 == 270):
                            cv.ellipse(img,(curx-37,cury-15),(37,37),0, startangle-15,startangle,(105,105,105), 6)
                            curx = curx-37
                            cury = cury-37-15
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(255,0,0),-1)
                            state = 1
                            dirn = 4
                            lane = 1
                        elif(startangle<360 and startangle-15>270):
                            cv.ellipse(img,(curx-37,cury-15),(37,37),0, startangle-15,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx-37,cury-15),(37,37),0, startangle-15,startangle,(255,0,0), 6)

                    elif(lane == 2):
                        if(startangle == 360):
                            cv.ellipse(img,(curx-22,cury-15),(22,22),0, startangle-30,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx-22,cury-15),(22,22),0, startangle-30,startangle,(255,0,0), 6)
                        elif(startangle-30 == 270):
                            cv.ellipse(img,(curx-22,cury-15),(22,22),0, startangle-30,startangle,(105,105,105), 6)
                            curx = curx-22
                            cury = cury-22-15
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(255,0,0),-1)
                            state = 1
                            dirn = 4
                            lane = 2
                        elif(startangle<360 and startangle-30>270):
                            cv.ellipse(img,(curx-22,cury-15),(22,22),0, startangle-30,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx-22,cury-15),(22,22),0, startangle-30,startangle,(255,0,0), 6)

                    elif(lane == 3):
                        if(startangle == 360):
                            
                            cv.ellipse(img,(curx-7,cury-15),(7,7),0, startangle-60,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx-7,cury-15),(7,7),0, startangle-60,startangle,(255,0,0), 6)
                        elif(startangle-60 == 270):
                            cv.ellipse(img,(curx-7,cury-15),(7,7),0, startangle-60,startangle,(105,105,105), 6)
                            curx = curx-7
                            cury = cury-7-15
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(255,0,0),-1)
                            state = 1
                            dirn = 4
                            lane = 3
                        elif(startangle<360 and startangle-60>270):
                            cv.ellipse(img,(curx-7,cury-15),(7,7),0, startangle-60,startangle,(105,105,105), 6)
                            startangle = startangle-5
                            cv.ellipse(img,(curx-7,cury-15),(7,7),0, startangle-60,startangle,(255,0,0), 6)            
                    
            elif(state == 4):
                if(dirn == 2):
                    if(lane!=3):
                        
                        if(lanestate == 1):
                            cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(105,105,105),-1)
                            cv.line(img,(curx+7,cury-3),(curx+21,cury-8),(255,0,0),6)
                            lanestate = 2
                        elif(lanestate==2):
                            cv.line(img,(curx+7,cury-3),(curx+21,cury-8),(105,105,105),6)
                            cv.line(img,(curx+21,cury-8),(curx+35,cury-13),(255,0,0),6)
                            lanestate = 3
                        elif(lanestate == 3):
                            cv.line(img,(curx+21,cury-8),(curx+35,cury-13),(105,105,105),6)
                            curx = curx+35
                            cury = cury-15
                            cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(255,0,0),-1)
                            lanestate = 0
                            lane =lane+1
                            state = 1
                elif(dirn == 3):
                    if(lane!=3):
                        if(lanestate == 1):
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(105,105,105),-1)
                            cv.line(img,(curx+3,cury+7),(curx+8,cury+21),(255,0,0),6)
                            lanestate = 2
                        elif(lanestate==2):
                            cv.line(img,(curx+3,cury+7),(curx+8,cury+21),(105,105,105),6)
                            cv.line(img,(curx+8,cury+21),(curx+13,cury+35),(255,0,0),6)
                            lanestate = 3
                        elif(lanestate == 3):
                            cv.line(img,(curx+8,cury+21),(curx+13,cury+35),(105,105,105),6)
                            curx = curx+15
                            cury = cury+35
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(105,105,105),-1)
                            lanestate = 0
                            lane = lane+1
                            state = 1

                elif(dirn == 4):
                    if(lane!=3):
                        if(lanestate == 1):
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(105,105,105),-1)
                            cv.line(img,(curx-7,cury+3),(curx-21,cury+8),(255,0,0),6)
                            lanestate = 2
                        elif(lanestate==2):
                            cv.line(img,(curx-7,cury+3),(curx-21,cury+8),(105,105,105),6)
                            cv.line(img,(curx-21,cury+8),(curx-35,cury+13),(255,0,0),6)
                            lanestate = 3
                        elif(lanestate == 3):
                            cv.line(img,(curx-21,cury+8),(curx-35,cury+13),(105,105,105),6)
                            curx = curx-35
                            cury = cury+15
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(255,0,0),-1)
                            lanestate = 0
                            lane =lane+1
                            state = 1
                
                elif(dirn == 1):
                    if(lane!=3):
                        if(lanestate == 1):
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(105,105,105),-1)
                            cv.line(img,(curx-3,cury-7),(curx-8,cury-21),(255,0,0),6)
                            lanestate = 2
                        elif(lanestate==2):
                            cv.line(img,(curx-3,cury-7),(curx-8,cury-21),(105,105,105),6)
                            cv.line(img,(curx-8,cury-21),(curx-13,cury-35),(255,0,0),6)
                            lanestate = 3
                        elif(lanestate == 3):
                            cv.line(img,(curx-8,cury-21),(curx-13,cury-35),(105,105,105),6)
                            curx = curx-15
                            cury = cury-35
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(255,0,0),-1)
                            lanestate = 0
                            lane = lane+1
                            state = 1
            elif(state == 5):
                if(dirn == 2):
                    if(lane!=1):
                        
                        if(lanestate == 1):
                            cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(105,105,105),-1)
                            cv.line(img,(curx+7,cury+3),(curx+21,cury+8),(255,0,0),6)
                            lanestate = 2
                        elif(lanestate==2):
                            cv.line(img,(curx+7,cury+3),(curx+21,cury+8),(105,105,105),6)
                            cv.line(img,(curx+21,cury+8),(curx+35,cury+13),(255,0,0),6)
                            lanestate = 3
                        elif(lanestate == 3):
                            cv.line(img,(curx+21,cury+8),(curx+35,cury+13),(105,105,105),6)
                            curx = curx+35
                            cury = cury+15
                            cv.rectangle(img,(curx,cury-3),(curx+15,cury+3),(255,0,0),-1)
                            lanestate = 0
                            lane =lane-1
                            state = 1
                elif(dirn == 3):
                    if(lane!=1):
                        
                        if(lanestate == 1):
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(105,105,105),-1)
                            cv.line(img,(curx-3,cury+7),(curx-8,cury+21),(255,0,0),6)
                            lanestate = 2
                        elif(lanestate==2):
                            cv.line(img,(curx-3,cury+7),(curx-8,cury+21),(105,105,105),6)
                            cv.line(img,(curx-8,cury+21),(curx-13,cury+35),(255,0,0),6)
                            lanestate = 3
                        elif(lanestate == 3):
                            cv.line(img,(curx-8,cury+21),(curx-13,cury+35),(105,105,105),6)
                            curx = curx-15
                            cury = cury+35
                            cv.rectangle(img,(curx-3,cury),(curx+3,cury+15),(105,105,105),-1)
                            lanestate = 0
                            lane = lane-1
                            state = 1

                elif(dirn == 4):
                    if(lane!=1):
                        
                        if(lanestate == 1):
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(105,105,105),-1)
                            cv.line(img,(curx-7,cury-3),(curx-21,cury-8),(255,0,0),6)
                            lanestate = 2
                        elif(lanestate==2):
                            cv.line(img,(curx-7,cury-3),(curx-21,cury-8),(105,105,105),6)
                            cv.line(img,(curx-21,cury-8),(curx-35,cury-13),(255,0,0),6)
                            lanestate = 3
                        elif(lanestate == 3):
                            cv.line(img,(curx-21,cury-8),(curx-35,cury-13),(105,105,105),6)
                            curx = curx-35
                            cury = cury-15
                            cv.rectangle(img,(curx-15,cury-3),(curx,cury+3),(255,0,0),-1)
                            lanestate = 0
                            lane =lane-1
                            state = 1
                
                elif(dirn == 1):
                    if(lane!=1):
                        if(lanestate == 1):
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(105,105,105),-1)
                            cv.line(img,(curx+3,cury-7),(curx+8,cury-21),(255,0,0),6)
                            lanestate = 2
                        elif(lanestate==2):
                            cv.line(img,(curx+3,cury-7),(curx+8,cury-21),(105,105,105),6)
                            cv.line(img,(curx+8,cury-21),(curx+13,cury-35),(255,0,0),6)
                            lanestate = 3
                        elif(lanestate == 3):
                            cv.line(img,(curx+8,cury-21),(curx+13,cury-35),(105,105,105),6)
                            curx = curx+15
                            cury = cury-35
                            cv.rectangle(img,(curx-3,cury-15),(curx+3,cury),(255,0,0),-1)
                            lanestate = 0
                            lane = lane-1
                            state = 1

            car_mat[i][2] = curx
            car_mat[i][3] = cury
            car_mat[i][4] = state
            car_mat[i][5] = dirn
            car_mat[i][6] = startangle
            car_mat[i][7] = lane
            car_mat[i][8] = lanestate
            car_mat[i][9] = sf
        cv.imshow('draw01',img)
        """print weight_hor_lr_mat
        print weight_hor_rl_mat
        print weight_ver_ud_mat
        print weight_ver_du_mat"""
        ite = ite +1
        
        
cv.imshow('draw01',img)
movcar()

cv.waitKey(0)

