import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import sys




def A(image, image2, image3, gray, image4):
    
    height, width = image.shape[:2]
    Gx=[[0 for x in range(height)] for y in range(width)]
    Gy=[[0 for x in range(height)] for y in range(width)]
    Gxb=[[0 for x in range(height)] for y in range(width)]
    Gxg=[[0 for x in range(height)] for y in range(width)]
    Gxr=[[0 for x in range(height)] for y in range(width)]
    Gyb=[[0 for x in range(height)] for y in range(width)]
    Gyg=[[0 for x in range(height)] for y in range(width)]
    Gyr=[[0 for x in range(height)] for y in range(width)]
    temp=0
    print(gray)
    if (gray >= 1): #GrayScale Image
        print("Bernard")
        for x in range(height):
            for y in range(width):
                if (x==0) and (y==0):
                    temp= (-(0.50)*(image[x+1,y]) 
                    -(0.25)* (image[x+1, y+1]))
                elif (x==0) and (y==(width-1)):
                    temp = (-(0.25)*(image[x+1,y-1])
                    -(0.50)*(image[x+1,y]))
                elif (y==0) and (x==(height-1)):
                    temp = ((0.50)*(image[x-1,y]) + (0.25)*(image[x-1][y+1]))
                   
                elif x==0:
                    temp = (-(0.25)*(image[x+1,y-1])
                    -(0.50)*(image[x+1,y]) 
                    -(0.25)* (image[x+1, y+1]))
                elif y==0:
                    temp = ((0.50)*(image[x-1,y]) - (0.50)*(image[x+1,y]) + (0.25)*(image[x-1][y+1])
                    -(0.25)* (image[x+1, y+1]))
                elif (x==(height-1)) and (y==(width-1)):
                    temp = ((0.25)*(image[x-1, y-1]) +
                    (0.50)*(image[x-1,y]))
                elif x==(height-1):
                    temp = ((0.25)*(image[x-1, y-1]) +
                    (0.50)*(image[x-1,y])  + (0.25)*(image[x-1][y+1]))
                elif y==(width-1):
                    temp = ((0.25)*(image[x-1, y-1]) - (0.25)*(image[x+1,y-1]) +
                    (0.50)*(image[x-1,y]) - (0.50)*(image[x+1,y]))
                else:                    
                    temp = ((0.25)*(image[x-1, y-1]) - (0.25)*(image[x+1,y-1]) +
                    (0.50)*(image[x-1,y]) - (0.50)*(image[x+1,y]) + (0.25)*(image[x-1][y+1])
                    -(0.25)* (image[x+1, y+1]))
                    
                image[x,y]= ((temp + 255)/510)*255
                Gx[x][y]=temp
                


                
        for x in range(height): #Gy
            for y in range(width):
                if (x==0) and (y==0):
                    temp= (-(0.5)* (image[x,y+1]) -(0.25)* (image[x+1, y+1]))
                elif (x==0) and (y==(width-1)):
                    temp = ((0.50)* (image[x,y-1]) + (0.25)*(image[x+1,y-1]))
                elif (y==0) and (x==(height-1)):
                    temp = (-(0.25)*(image[x-1][y+1]) - (0.5)* (image[x,y+1])) 
                elif x==0:
                    temp = ( (0.50)* (image[x,y-1]) + (0.25)*(image[x+1,y-1]) 
                     - (0.5)* (image[x,y+1])
                    -(0.25)* (image[x+1, y+1]))
                elif y==0:
                    temp = ( -(0.25)*(image[x-1][y+1]) - (0.5)* (image[x,y+1])
                    -(0.25)* (image[x+1, y+1]))
                elif (x==(height-1)) and (y==(width-1)):
                    temp = ((0.25)*(image[x-1, y-1]) + (0.50)* (image[x,y-1]))
                elif x==(height-1):
                    temp = ((0.25)*(image[x-1, y-1]) + (0.50)* (image[x,y-1]) 
                    -(0.25)*(image[x-1][y+1]) - (0.5)* (image[x,y+1]))
                elif y==(width-1):
                    temp = ((0.25)*(image[x-1, y-1]) + (0.50)* (image[x,y-1]) + (0.25)*(image[x+1,y-1]) )
                else:                    
                    temp = ((0.25)*(image[x-1, y-1]) + (0.50)* (image[x,y-1]) + (0.25)*(image[x+1,y-1]) 
                    -(0.25)*(image[x-1][y+1]) - (0.5)* (image[x,y+1])
                    -(0.25)* (image[x+1, y+1]))
                    
                image2[x,y]= ((temp + 255)/510)*255
                Gy[x][y]=temp
                
        

        

    else: #RGB
        #Gx
        for x in range(height): #Blue 
            for y in range(width):
                if (x==0) and (y==0):
                    temp= (-(0.50)*(image[x+1,y, 0]) 
                    -(0.25)* (image[x+1, y+1, 0]))
                elif (x==0) and (y==(width-1)):
                    temp = (-(0.25)*(image[x+1,y-1, 0])
                    -(0.50)*(image[x+1,y, 0]))
                elif (y==0) and (x==(height-1)):
                    temp = ((0.50)*(image[x-1,y, 0]) + (0.25)*(image[x-1,y+1, 0]))
                
                elif x==0:
                    temp = (-(0.25)*(image[x+1,y-1, 0])
                    -(0.50)*(image[x+1,y, 0]) 
                    -(0.25)* (image[x+1, y+1, 0]))
                elif y==0:
                    temp = ((0.50)*(image[x-1,y, 0]) - (0.50)*(image[x+1,y, 0]) + (0.25)*(image[x-1,y+1, 0])
                    -(0.25)* (image[x+1, y+1, 0]))
                elif (x==(height-1)) and (y==(width-1)):
                    temp = ((0.25)*(image[x-1, y-1, 0]) +
                    (0.50)*(image[x-1,y, 0]))
                elif x==(height-1):
                    temp = ((0.25)*(image[x-1, y-1, 0]) +
                    (0.50)*(image[x-1,y, 0])  + (0.25)*(image[x-1,y+1, 0]))
                elif y==(width-1):
                    temp = ((0.25)*(image[x-1, y-1, 0]) - (0.25)*(image[x+1,y-1, 0]) +
                    (0.50)*(image[x-1,y, 0]) - (0.50)*(image[x+1,y, 0]))
                else:                    
                    temp = ((0.25)*(image[x-1, y-1, 0]) - (0.25)*(image[x+1,y-1, 0]) +
                    (0.50)*(image[x-1,y, 0]) - (0.50)*(image[x+1,y, 0]) + (0.25)*(image[x-1,y+1, 0])
                    -(0.25)* (image[x+1, y+1, 0]))
                Gxb[x][y]= temp
                image[x, y, 0]= ((temp + 255)/(510)) *255
                

        for x in range(height): #Green
            for y in range(width):
                if (x==0) and (y==0):
                    temp= (-(0.50)*(image[x+1,y, 1]) 
                    -(0.25)* (image[x+1, y+1, 1]))
                elif (x==0) and (y==(width-1)):
                    temp = (-(0.25)*(image[x+1,y-1, 1])
                    -(0.50)*(image[x+1,y, 1]))
                elif (y==0) and (x==(height-1)):
                    temp = ((0.50)*(image[x-1,y, 1]) + (0.25)*(image[x-1,y+1, 1]))
                
                elif x==0:
                    temp = (-(0.25)*(image[x+1,y-1, 1])
                    -(0.50)*(image[x+1,y, 1]) 
                    -(0.25)* (image[x+1, y+1, 1]))
                elif y==0:
                    temp = ((0.50)*(image[x-1,y, 1]) - (0.50)*(image[x+1,y, 1]) + (0.25)*(image[x-1,y+1, 1])
                    -(0.25)* (image[x+1, y+1, 1]))
                elif (x==(height-1)) and (y==(width-1)):
                    temp = ((0.25)*(image[x-1, y-1, 1]) +
                    (0.50)*(image[x-1,y, 1]))
                elif x==(height-1):
                    temp = ((0.25)*(image[x-1, y-1, 1]) +
                    (0.50)*(image[x-1,y, 1])  + (0.25)*(image[x-1, y+1, 1]))
                elif y==(width-1):
                    temp = ((0.25)*(image[x-1, y-1, 1]) - (0.25)*(image[x+1,y-1, 1]) +
                    (0.50)*(image[x-1,y, 1]) - (0.50)*(image[x+1,y, 1]))
                else:                    
                    temp = ((0.25)*(image[x-1, y-1, 1]) - (0.25)*(image[x+1,y-1, 1]) +
                    (0.50)*(image[x-1,y, 1]) - (0.50)*(image[x+1,y, 1]) + (0.25)*(image[x-1,y+1, 1])
                    -(0.25)* (image[x+1, y+1, 1]))
                    
                image[x, y, 1]= ((temp + 255)/(510)) *255
                Gxg[x][y]= temp
                
        for x in range(height): #Red 
            for y in range(width):
                if (x==0) and (y==0):
                    temp= (-(0.50)*(image[x+1,y, 2]) 
                    -(0.25)* (image[x+1, y+1, 2]))
                elif (x==0) and (y==(width-1)):
                    temp = (-(0.25)*(image[x+1,y-1, 2])
                    -(0.50)*(image[x+1,y, 2]))
                elif (y==0) and (x==(height-1)):
                    temp = ((0.50)*(image[x-1,y, 2]) + (0.25)*(image[x-1,y+1, 2]))
                
                elif x==0:
                    temp = (-(0.25)*(image[x+1,y-1, 2])
                    -(0.50)*(image[x+1,y, 2]) 
                    -(0.25)* (image[x+1, y+1, 2]))
                elif y==0:
                    temp = ((0.50)*(image[x-1,y, 2]) - (0.50)*(image[x+1,y, 2]) + (0.25)*(image[x-1,y+1, 2])
                    -(0.25)* (image[x+1, y+1, 2]))
                elif (x==(height-1)) and (y==(width-1)):
                    temp = ((0.25)*(image[x-1, y-1, 2]) +
                    (0.50)*(image[x-1,y, 2]))
                elif x==(height-1):
                    temp = ((0.25)*(image[x-1, y-1, 2]) +
                    (0.50)*(image[x-1,y, 2])  + (0.25)*(image[x-1, y+1, 2]))
                elif y==(width-1):
                    temp = ((0.25)*(image[x-1, y-1, 2]) - (0.25)*(image[x+1,y-1, 2]) +
                    (0.50)*(image[x-1,y, 2]) - (0.50)*(image[x+1,y, 2]))
                else:                    
                    temp = ((0.25)*(image[x-1, y-1, 2]) - (0.25)*(image[x+1,y-1, 2]) +
                    (0.50)*(image[x-1,y, 2]) - (0.50)*(image[x+1,y, 2]) + (0.25)*(image[x-1,y+1, 2])
                    -(0.25)* (image[x+1, y+1, 2]))
                    
                image[x, y, 2]= ((temp + 255)/(510)) *255
                Gxr[x][y]= temp


        #Gy
        for x in range(height): #Blue
            for y in range(width):
                if (x==0) and (y==0):
                    temp= (-(0.5)* (image2[x,y+1,0]) -(0.25)* (image2[x+1, y+1,0]))
                elif (x==0) and (y==(width-1)):
                    temp = ((0.50)* (image2[x,y-1,0]) + (0.25)*(image2[x+1,y-1,0]))
                elif (y==0) and (x==(height-1)):
                    temp = (-(0.25)*(image2[x-1,y+1,0]) - (0.5)* (image2[x,y+1,0])) 
                elif x==0:
                    temp = ( (0.50)* (image2[x,y-1,0]) + (0.25)*(image2[x+1,y-1,0]) 
                    - (0.5)* (image2[x,y+1,0])
                    -(0.25)* (image2[x+1, y+1,0]))
                elif y==0:
                    temp = ( -(0.25)*(image2[x-1,y+1,0]) - (0.5)* (image2[x,y+1,0])
                    -(0.25)* (image2[x+1, y+1,0]))
                elif (x==(height-1)) and (y==(width-1)):
                    temp = ((0.25)*(image2[x-1, y-1,0]) + (0.50)* (image2[x,y-1,0]))
                elif x==(height-1):
                    temp = ((0.25)*(image2[x-1, y-1,0]) + (0.50)* (image2[x,y-1,0]) 
                    -(0.25)*(image2[x-1,y+1,0]) - (0.5)* (image2[x,y+1,0]))
                elif y==(width-1):
                    temp = ((0.25)*(image2[x-1, y-1,0]) + (0.50)* (image2[x,y-1,0]) + (0.25)*(image2[x+1,y-1,0]) )
                else:                    
                    temp = ((0.25)*(image2[x-1, y-1,0]) + (0.50)* (image2[x,y-1,0]) + (0.25)*(image2[x+1,y-1,0]) 
                    -(0.25)*(image2[x-1,y+1,0]) - (0.5)* (image2[x,y+1,0])
                    -(0.25)* (image2[x+1, y+1,0]))
                    
                image2[x, y, 0]= ((temp + 255)/(510)) *255
                Gyb[x][y]= temp
                
        for x in range(height): #Green
            for y in range(width):
                if (x==0) and (y==0):
                    temp= (-(0.5)* (image2[x,y+1,1]) -(0.25)* (image2[x+1, y+1,1]))
                elif (x==0) and (y==(width-1)):
                    temp = ((0.50)* (image2[x,y-1,1]) + (0.25)*(image2[x+1,y-1,1]))
                elif (y==0) and (x==(height-1)):
                    temp = (-(0.25)*(image2[x-1,y+1,1]) - (0.5)* (image2[x,y+1,1])) 
                elif x==0:
                    temp = ( (0.50)* (image2[x,y-1,1]) + (0.25)*(image2[x+1,y-1,1]) 
                    - (0.5)* (image2[x,y+1,1])
                    -(0.25)* (image2[x+1, y+1,1]))
                elif y==0:
                    temp = ( -(0.25)*(image2[x-1,y+1,1]) - (0.5)* (image2[x,y+1,1])
                    -(0.25)* (image2[x+1, y+1,1]))
                elif (x==(height-1)) and (y==(width-1)):
                    temp = ((0.25)*(image2[x-1, y-1,1]) + (0.50)* (image2[x,y-1,1]))
                elif x==(height-1):
                    temp = ((0.25)*(image2[x-1, y-1,1]) + (0.50)* (image2[x,y-1,1]) 
                    -(0.25)*(image2[x-1,y+1,1]) - (0.5)* (image2[x,y+1,1]))
                elif y==(width-1):
                    temp = ((0.25)*(image2[x-1, y-1,1]) + (0.50)* (image2[x,y-1,1]) + (0.25)*(image2[x+1,y-1,1]) )
                else:                    
                    temp = ((0.25)*(image2[x-1, y-1,1]) + (0.50)* (image2[x,y-1,1]) + (0.25)*(image2[x+1,y-1,1]) 
                    -(0.25)*(image2[x-1,y+1,1]) - (0.5)* (image2[x,y+1,1])
                    -(0.25)* (image2[x+1, y+1,1]))
                
                image2[x, y, 1]= ((temp + 255)/(510)) *255
                Gyg[x][y]= temp
                
        for x in range(height): #Red
            for y in range(width):
                if (x==0) and (y==0):
                    temp= (-(0.5)* (image2[x,y+1,2]) -(0.25)* (image2[x+1, y+1,2]))
                elif (x==0) and (y==(width-1)):
                    temp = ((0.50)* (image2[x,y-1,2]) + (0.25)*(image2[x+1,y-1,2]))
                elif (y==0) and (x==(height-1)):
                    temp = (-(0.25)*(image2[x-1,y+1,2]) - (0.5)* (image2[x,y+1,2])) 
                elif x==0:
                    temp = ( (0.50)* (image2[x,y-1,2]) + (0.25)*(image2[x+1,y-1,2]) 
                    - (0.5)* (image2[x,y+1,2])
                    -(0.25)* (image2[x+1, y+1,2]))
                elif y==0:
                    temp = ( -(0.25)*(image2[x-1,y+1,2]) - (0.5)* (image2[x,y+1,2])
                    -(0.25)* (image2[x+1, y+1,2]))
                elif (x==(height-1)) and (y==(width-1)):
                    temp = ((0.25)*(image2[x-1, y-1,2]) + (0.50)* (image2[x,y-1,2]))
                elif x==(height-1):
                    temp = ((0.25)*(image2[x-1, y-1,2]) + (0.50)* (image2[x,y-1,2]) 
                    -(0.25)*(image2[x-1,y+1,2]) - (0.5)* (image2[x,y+1,2]))
                elif y==(width-1):
                    temp = ((0.25)*(image2[x-1, y-1,2]) + (0.50)* (image2[x,y-1,2]) + (0.25)*(image2[x+1,y-1,2]) )
                else:                    
                    temp = ((0.25)*(image2[x-1, y-1,2]) + (0.50)* (image2[x,y-1,2]) + (0.25)*(image2[x+1,y-1,2]) 
                    -(0.25)*(image2[x-1,y+1,2]) - (0.5)* (image2[x,y+1,2])
                    -(0.25)* (image2[x+1, y+1,2]))
                    
                image2[x, y, 2]= ((temp + 255)/(510)) *255
                Gyr[x][y]= temp
                



       

    #part b
    temp=0
    temp1=0
    temp2=0
    temp3=0
    if (gray==1): #GrayScale Image
        for x in range(height): 
            for y in range(width):
                temp = math.sqrt(math.pow(Gx[x][y],2) + math.pow(Gy[x][y],2))
                image3[x,y]= ((temp + 255)/(510)) *255
    else:   
        for x in range(height): 
             for y in range(width):
                 temp1 = math.sqrt(math.pow(Gxb[x][y],2) + math.pow(Gyb[x][y],2))
                 temp2 = math.sqrt(math.pow(Gxg[x][y],2) + math.pow(Gyg[x][y],2))
                 temp3= math.sqrt(math.pow(Gxr[x][y],2) + math.pow(Gyr[x][y],2))
                 image3[x, y, 0]= ((temp1 + 255)/(510)) *255
                 image3[x, y, 1]= ((temp2 + 255)/(510)) *255
                 image3[x, y, 2]= ((temp3 + 255)/(510)) *255
        

    #part c arrow quiver
    if(gray>=1):
        angle=0
        for x in range(10, height-10, 10): 
            for y in range(10, width-10, 10):
                #print(Gx[x][y][0])
                
                
                a=float(Gy[x][y])
                b=float(Gx[x][y])
                angle=math.atan2(a,b)
                cv2.arrowedLine(image4,(x,y), (x + int(5*math.cos(angle)), y+ int(5*math.sin(angle))),(0,0,0),1,8,0,0.1)
                
    cv2.imshow("Gx",image)
    cv2.imshow("Gy",image2)
    cv2.imshow("Sobel Magnitude",image3)
    cv2.imshow("Arrow Plot",image4)

        


    

        

if len(sys.argv)!=3:
    print("Please use command line format \"./SobelFilter.py input_image grayscale")
    quit()
print("hey")
image4=cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
if(int(sys.argv[2]) == 1):#Grayscale
    image = cv2.imread(sys.argv[1])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image2= cv2.imread(sys.argv[1])
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    image3=cv2.imread(sys.argv[1])
    image3= cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
else:
    image = cv2.imread(sys.argv[1])
    image2= cv2.imread(sys.argv[1])
    image3=cv2.imread(sys.argv[1])
print("ho")
A(image, image2,image3,int(sys.argv[2]), image4)
print("type")
