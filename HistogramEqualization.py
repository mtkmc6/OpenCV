import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import sys


def A1(image):
    height, width = image.shape[:2]
    if len(image.shape)==2: #GrayScale Image
        grayFrequency = []
        grayFrequency = [0 for i in range(256)]
        
        for x in range(height):
            for y in range(width):
                grayFrequency[image[x,y]]=grayFrequency[image[x,y]]+1
                
        intensity=[]
        intensity = [i for i in range(256)]
        
        plt.bar(intensity,grayFrequency,color = "gray")
        plt.show()
        
    else:   #RGB Image
        redFrequency = []
        redFrequency = [0 for i in range(256)]
        blueFrequency = []
        blueFrequency = [0 for i in range(256)]
        greenFrequency = []
        greenFrequency = [0 for i in range(256)]
        intensity=[]
        intensity = [i for i in range(256)]
        
        for x in range(height):
            for y in range(width):
                blueFrequency[image[x,y,0]]=blueFrequency[image[x,y,0]]+1
                greenFrequency[image[x,y,1]]=greenFrequency[image[x,y,1]]+1
                redFrequency[image[x,y,2]]=redFrequency[image[x,y,2]]+1
        
        plt.bar(intensity,redFrequency, color = "red")
        plt.bar(intensity,greenFrequency,color="green")
        plt.bar(intensity,blueFrequency,color="blue")
        plt.show()

def A2(image, bins):
    height, width = image.shape[:2]
    if len(image.shape)==2:
        Frequency = []
        Frequency = [0 for i in range(bins)]
        
        for x in range(height):
            for y in range(width):
                Frequency[int(image[x,y]/(256/bins))]=Frequency[int(image[x,y]/(256/bins))]+1
        intensity=[]
        intensity = [i for i in range(bins)]
        plt.bar(intensity,Frequency,color = "gray")
        plt.show()
        
    else:
        redFrequency = []
        redFrequency = [0 for i in range(bins)]
        blueFrequency = []
        blueFrequency = [0 for i in range(bins)]
        greenFrequency = []
        greenFrequency = [0 for i in range(bins)]
        intensity=[]
        intensity = [i for i in range(bins)]
        
        for x in range(height):
            for y in range(width):
                blueFrequency[int(image[x,y,0]/(256/bins))]=blueFrequency[int(image[x,y,0]/(256/bins))]+1
                greenFrequency[int(image[x,y,1]/(256/bins))]=greenFrequency[int(image[x,y,1]/(256/bins))]+1
                redFrequency[int(image[x,y,2]/(256/bins))]=redFrequency[int(image[x,y,2]/(256/bins))]+1
       
        plt.bar(intensity,redFrequency, color = "red")
        plt.bar(intensity,greenFrequency,color="green")
        plt.bar(intensity,blueFrequency,color="blue")
        plt.show()

def A3(image):
    image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = image2.shape[:2]
    
    for x in range(height):
        for y in range(width):
            
            if image2[x,y]== 1:
                image2[x,y]=0
            else:
                image2[x,y]=100*(math.log(image2[x,y],10))
                
    Frequency = []
    Frequency = [0 for i in range(256)]
    
    for x in range(height):
        for y in range(width):
            Frequency[image2[x,y]]=Frequency[image2[x,y]]+1
            
    intensity=[]
    intensity = [i for i in range(256)]
    cv2.imshow("Log",image2)
    plt.bar(intensity,Frequency,color = "gray")
    plt.show()

def B(image):
    image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original",image2)
    height, width = image2.shape[:2]
    Frequency = []
    Frequency = [0 for i in range(256)]
    
    for x in range(height):
        for y in range(width):
            Frequency[image2[x,y]]=Frequency[image2[x,y]]+1
            
    equalOuptut=Frequency
    
    for x in range(len(Frequency)):
        equalOuptut[x]=Frequency[x]/(height*width)
    for x in range(1,len(equalOuptut)): #Start at second element
        equalOuptut[x]=equalOuptut[x]+equalOuptut[x-1]
    for x in range(len(equalOuptut)):
        equalOuptut[x]=equalOuptut[x]*255
    for x in range(len(equalOuptut)):
        equalOuptut[x]=int(equalOuptut[x])
        
    image3 = np.uint8(np.zeros(image2.shape))
    for x in range(height):
        for y in range(width):
            image3[x,y]=np.uint8(equalOuptut[image2[x,y]])
            
    
    Frequency = [0 for i in range(256)]
    for x in range(height):
        for y in range(width):
            Frequency[image3[x,y]]=Frequency[image3[x,y]]+1
    intensity=[]
    intensity = [i for i in range(256)]
    cv2.imshow("Equalized Image",image3)
    plt.bar(intensity,Frequency,color = "gray")
    plt.show()

if len(sys.argv)!=3:
    print("Please use command line format \"./HistogramEqualization.py input_image Bins")
    quit()
image = cv2.imread(sys.argv[1])
Bins = int(sys.argv[2])
A1(image)
A2(image,Bins)
A3(image)
B(image)
