import os  
from PIL import Image
import numpy as np
import csv
import pandas as pd
##src- path of image file
def openImage(src): 
    return Image.open(src,'r')
## this function reads image and get RGB data
def readImage(im):
    
    im = im.convert('RGB') ##converts single value to rgb
    return list(im.getdata()) ##listing all rgb into a list
  

def check_skin(rgb):
    if (rgb[0]<=100 and rgb[1]<=100 and rgb[2]<=100): return False
    return True

class skin_Non_skinValue(object):
    def __init__(self,pixel, skin, non_skin, arr_index):
        self.pixel = pixel
        self.skin = skin
        self.non_skin = non_skin
        self.arr_index = arr_index
        


def trainData(pixels, pix_val_actual, pix_val_mask, skin, non_skin):
        
    for i in range(len(pix_val_actual)):
        
         r = pix_val_actual[i][0]
         g = pix_val_actual[i][1]
         b = pix_val_actual[i][2]

         if(check_skin(pix_val_mask[i])):
            skin[r][g][b]+=1 
      
         else:
            non_skin[r][g][b]+=1
                
        
    return pixels, skin, non_skin                  
 
def setProbability(pixel, skin, non_skin, probability):
    probability = list(skin/(non_skin+skin))
    return probability

def testData(probability, pix_val_actual):
    treshold = 0.555555
    arr  = []
    for i in range(len(pix_val_actual)):
        r = pix_val_actual[i][0]
        g = pix_val_actual[i][1]
        b = pix_val_actual[i][2]
        if(probability[r][g][b]<treshold):
            arr.append([255,255,255])
        else:
            arr.append([0,0,0])
    return arr                   
def test(probability, path):
    
    im = openImage(path)
    temp = im.copy()
    createImage(temp, probability)

  
def whiteImage(width, height):
    return Image.new('RGB',(width,height),'white')
     

def createImage(im,probability): 
    
    width, height = im.size

    pix = im.load()

    
    for i in range(width):
        for j in range(height):
            r,g,b = im.getpixel((i,j))
            row_num = (r*256*256)+(g*256)+b
            if(probability['Probability'][row_num] <0.4):
                pix[i,j] = (0,0,0)
            else:
                pix[i,j] = (255,255,255)
                
#                        

    # Return new image
    saveImage(im)
    
def saveImage(image): ## saving image
    image.save('s1_mask1.jpg')




def toList(r,g,b,probability):
    a = []
    a.append(r)
    a.append(g)
    a.append(b)
    a.append(probability)
    return list(a)

def data(probability):  ## just a function to make list of rgb and prob
    arr = []
    for r in range(256):
        for g in range(256):
            for b in range(256):
                print(r,g,b)
                arr.append(toList(r,g,b,probability[r][g][b]))
    return arr     


def createCSV(probability): ##this function creats csv 
    myFile = open('train1.csv', 'w', newline = '')
    with myFile:  
        writer = csv.writer(myFile)
        writer.writerow(["Red", "Green", "Blue", "Probability"])
        writer.writerows(data(probability))
    print('done')


    
if __name__ == "__main__":
    
###>>>>>>>>>>>>>>>training phase<<<<<<<<<<<<<<<<<<<<<<

#    pixels = np.zeros((256,256,256))
#    skin = np.zeros((256,256,256)) 
#    non_skin = np.zeros((256,256,256))
#    
#    probability = np.zeros((256,256,256))

#    
#    ###########################--> reading image starts here.
#    ########### get all the files from that directory
#    files_actual = os.listdir('SkinDetector-master\data\image') 
#    files_mask = os.listdir('SkinDetector-master\data\mask')
#   ############
#   
#    for i in range(len(files_actual)): ##iterating throuh all images
#        print(i)

#        image_actual_path = 'SkinDetector-master\data\image\\'
#        imgae_mask_path = 'SkinDetector-master\data\mask\\'

#        pix_val_actual = readImage(openImage(image_actual_path+files_actual[i])) ## storing the pixels of actual picture..
#        pix_val_mask = readImage(openImage(imgae_mask_path+files_mask[i])) ## storing the pixels of mask picture..
#       
#        pixels, skin, non_skin = trainData(pixels, pix_val_actual, pix_val_mask, skin, non_skin) ## this returns the skin value and non_skin value 
#        
#    probability = setProbability(pixels, skin, non_skin, probability) ## this returns the probability
#    createCSV(probability) ## creating CSV from that probabilty and rgb

###>>>>>>>>>>>>>>>end<<<<<<<<<<<<<<<<<<<<<<

    probability = pd.read_csv('train.csv') # getting the rows from csv    
    print('Data collection completed') 
#    print(probability)       
    test(probability,'t2.jpg') # this tests the data
    
    print('Prediction is ready')
    
