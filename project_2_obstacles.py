import numpy as np
import math


x=np.linspace(0,300,301,dtype=int)
y=np.linspace(200,0,201,dtype=int)
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

textfile1=open("visualize.txt", "a")
textfile1.write(str(mask2))
textfile1.close()




map_img = 255*np.ones((height, width, 3), np.uint8)

def draw_map(map):
    global height, width, map_img
    # Create a white base image to draw map onto
    #block_size = 10
    #map_img = 255*np.ones((height*block_size, width*block_size, 3), np.uint8)
    # Convert dtype
    map_img = 255*np.array(map, np.uint8)
    # Upscale before imshow
    scale_percent = 1000 # percent of original size
    w = int(map_img.shape[1] * scale_percent / 100)
    h = int(map_img.shape[0] * scale_percent / 100)
    # resize image
    resized = cv2.resize(map_img, (w,h), interpolation = cv2.INTER_AREA)
    
    cv2.imshow('Current map', resized)
    cv2.waitKey(50)  # in ms - adjust as needed for display speed

    return


draw_map(mask2)