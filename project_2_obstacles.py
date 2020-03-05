# ENPM661, Spring 2020, Project 2
# Shelly Bagchi & Omololu Makinde

import math
import numpy as np
import cv2





height = 200 #mask2.shape[0]
width  = 300 #mask2.shape[1]
# Create a white base image to draw map onto
map_img = 255*np.ones((height, width, 3), np.uint8)

# Old function for drawing mask
def draw_map(map):
    global height, width, map_img

    # Convert dtype - only works for 0s & 1s
    #map_img = 255*np.array(map, np.uint8)

    #map_img = 255*np.ones((height, width, 3), np.uint8)
    for (i,row) in enumerate(map):
        for (j,value) in enumerate(row):
            if value==0:
                map_img[i,j] = np.array([0,0,255], np.uint8);
            elif value>5:
                map_img[i,j] = np.array([0,0,0], np.uint8);



    # Upscale before imshow
    scale_percent = 200  # percent of original size
    w = int(map_img.shape[1] * scale_percent / 100)
    h = int(map_img.shape[0] * scale_percent / 100)
    # resize image
    resized = cv2.resize(map_img, (w,h), interpolation = cv2.INTER_AREA)
    

    cv2.imshow('Current map', resized)
    cv2.waitKey(50)  # in ms - adjust as needed for display speed

    return

# New function for using OpenCV built-in drawing functions
def draw_obstacles():
    global height, width, map_img

    # Convert dtype - only works for 0s & 1s
    #map_img = 255*np.array(map, np.uint8)

    # Draw obstacles - remember coords are (w,h)!
    #rect = cv2.minAreaRect([(), (), (), ()])
    #rect = ((95-75, height-30-10), (75, 10), 210)
    rect = ((95, height-30-10), (-75, -10), 30)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(map_img, [box], 0, (0,0,0), thickness=1)#cv2.FILLED)
    #cv2.rectangle(img=map_img, pt1=(95-75, height-30-10), pt2=(95, height-30), color=(0,0,0), thickness=1)#cv2.FILLED)
    #map_img = cv2.rotate(map_img, 30)

    cv2.circle(img=map_img, center=(width-50,50), radius=25, color=(0,0,0), thickness=1)
    cv2.ellipse(img=map_img, center=(width//2,height//2), axes=(40,20), angle=0, startAngle=0, endAngle=360, color=(0,0,0), thickness=1)
    # Starting at top left pt
    cv2.line(img=map_img, pt1=(25, height-185), pt2=(75, height-185), color=(0,0,0), thickness=1)
    cv2.line(img=map_img, pt1=(75, height-185), pt2=(100,height-150), color=(0,0,0), thickness=1)
    cv2.line(img=map_img, pt1=(100,height-150), pt2=(75, height-120), color=(0,0,0), thickness=1)
    cv2.line(img=map_img, pt1=(75, height-120), pt2=(50, height-150), color=(0,0,0), thickness=1)
    cv2.line(img=map_img, pt1=(50, height-150), pt2=(20, height-120), color=(0,0,0), thickness=1)
    cv2.line(img=map_img, pt1=(20, height-120), pt2=(25, height-185), color=(0,0,0), thickness=1)


    # Upscale before displaying
    scale_percent = 200  # percent of original size
    w = int(map_img.shape[1] * scale_percent / 100)
    h = int(map_img.shape[0] * scale_percent / 100)
    # resize image
    resized = cv2.resize(map_img, (w,h), interpolation = cv2.INTER_AREA)
    

    cv2.imshow('Map with obstacles', resized)
    cv2.waitKey(50)  # in ms - adjust as needed for display speed

    return map_img




x=np.linspace(0,299,300,dtype=int)
y=np.linspace(199,0,200,dtype=int)
x_1,y_1=np.meshgrid(x,y)
##a,b,d,e=7.5-x_1,x_1-7.5,10-x_1,x_1-2
######################################OBSTACLE 1#############################################################
triangle1=np.where((x_1<=25)&(x_1>=20)&(y_1<=((120+(13*(x_1-20)))))&(y_1>=(65/55)*(x_1-20)+120),2,1)
triangle2=np.where((x_1<=100)&(x_1>=50)&(y_1<=(35/25)*(x_1-50)+150)&(y_1<=(35/25)*(100-x_1)+150)&(y_1>=150),2,1)
triangle3=np.where((x_1<=100)&(x_1>=50)&(y_1>=(35/25)*(x_1-75)+120)&(y_1>=(35/25)*(75-x_1)+120)&(y_1<=150),2,1)
######################################OBSTACLE 2##############################################################
def cosdeg(x):
    cosdeg=math.cos((x*math.pi)/180)
    return cosdeg
def tandeg(x):
    tandeg=math.tan((x*math.pi)/180)
    return tandeg
def sindeg(x):
    sindeg=math.tan((x*math.pi)/180)
    return sindeg
c30,t30,s30,c60,t60,s60=cosdeg(30),tandeg(30),sindeg(30),cosdeg(60),tandeg(60),sindeg(60)
print(c30,t30,s30,c60,t60,s60)
rectangle=np.where((x_1<=90)&(x_1>=75)&(y_1>=t30*(95-x_1)+30)&(y_1<=(t30*(95+(s30*20))-x_1)+((c30*20)+3))&(y_1>=((t60*(95+(s30*20)))-x_1)+(20*s30+3))&(y_1<=(t60*(x_1-95))+s30*75),2,1)
###################################RECTANGLE##############################################################
star=np.where((x_1<=250)&(x_1>=200)&(y_1>=(15/25)*(255-x_1)+10)&(y_1>=(15/25)*(x_1-225)+10)&(y_1<=(15/25)*(x_1-200)+25)&(y_1>=(15/25)*(250-x_1)+25),2,1)
###################################CIRCLE#################################################################
circle= np.where((x_1-225)^2+(y_1-150)^2>=25^2,2,1)
###################################ELIPSE#################################################################
#ellipse= np.where((((x_1-225)^2)/(40^2)+((y_1-150))^2/(20^2))>=1,2,1)
                 

##mask=np.where((x_1<=5)&(x_1>=2)&((12+1.3*e)>=y_1)&(y_1>=(12+e)), 2,0)
mask2=(triangle1) + (triangle2)+(triangle3)+(star)+circle#+elipse
##print("mask = ")
##print(mask)
##upper_triangl=np.where((
print("mask2 = ")
print(mask2)
print("x_1 = ") 
print(x_1) 
print("y_1 = ") 
print(y_1) 

textfile1=open("visualize.txt", "w")
np.set_printoptions(threshold=np.inf)
#textfile1.write(str(mask2))
#textfile1.close()

print(mask2.shape)


#draw_map(mask2)
map_img = draw_obstacles()


textfile1.write(str(map_img))
textfile1.close()



cv2.waitKey(0)
cv2.destroyAllWindows()

