from PIL import ImageFont, ImageDraw, Image  
import cv2  
import numpy as np  
import os
import csv

f = open("names.txt","r")
names_list = f.read().split("\n")
#print(names_list)

f1 = open("coords.txt","r")
coordinates = f1.read().split("\n")

flag=True

for i in range(len(names_list)):


    name_to_print = names_list[i]
    date_to_print = "30/08/2020"   #Change this date as per requirement

    # Load image in OpenCV  
    image = cv2.imread("template2.jpg")  

    # Convert the image to RGB (OpenCV uses BGR)  
    cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)  

    # Pass the image to PIL  
    pil_im = Image.fromarray(cv2_im_rgb)  

    draw = ImageDraw.Draw(pil_im)  
    # use a truetype font  
    font = ImageFont.truetype("./fonts/MLSJN.TTF", 60)      #You can change fonts size from list,given bottom
    font1 = ImageFont.truetype("./fonts/OLDENGL.TTF", 60)   

    # Draw the text 
    '''draw.text((int(coordinates[0]), int(coordinates[1])), name_to_print, font=font , fill='red')
    draw.text((int(coordinates[2]), int(coordinates[3])), date_to_print , font=font1, fill='blue')'''

    draw.text((439,331),name_to_print,font=font,fill='Black') 
    draw.text((752,590),date_to_print,font=font,fill='Black')
    
    # Get back the image to OpenCV  
    cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)  
    
    if flag:
        cv2.imshow('Certificate', cv2_im_processed) #Shows sample image
        flag=False
    path = ''
    cv2.imwrite('./output/'+name_to_print+'.png',cv2_im_processed)
    #os.startfile('output.png')
    cv2.waitKey(0)  

    cv2.destroyAllWindows()
    

'''
Other vareity of FONTS (Make sure you give proper path)

MLSJN.TTF
Lato-Black.ttf
MATURASC.TTF
OLDENGL.TTF
VIVALDII.TTF
copperplate gothic font.ttf


'''

'''
coordinates originally given in coords.txt file

198
228
53
337


'''




