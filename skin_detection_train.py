import os  
from PIL import Image
import numpy as np
import csv
import pandas as pd


##src- path of image file
def open_image(src): 
    return Image.open(src,'r')


## this function reads image and get RGB data
def read_image(im):
    im = im.convert('RGB') ##converts single value to rgb
    return list(im.getdata()) ##listing all rgb into a list
  

def check_skin(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    if (r <= 150 and g <= 150 and b <= 150): return False
    return True

def train_data(pixels, pix_val_actual, pix_val_mask, skin, non_skin):
        
    for i in range(len(pix_val_actual)):
        
        r = pix_val_actual[i][0]
        g = pix_val_actual[i][1]
        b = pix_val_actual[i][2]

        if(check_skin(pix_val_mask[i])):
            skin[r][g][b] += 1 
      
        else:
            non_skin[r][g][b] += 1
       
    return pixels, skin, non_skin                  
 
def set_probability(pixel, skin, non_skin, probability):
    probability = list(skin / (non_skin + skin))
    return probability


def to_list(r,g,b,probability):
    a = []
    a.append(r)
    a.append(g)
    a.append(b)
    a.append(probability)
    return list(a)

def data(probability):  ## just a function to make list of rgb and prob
    arr = []
    progress = 0
    for r in range(256):
        for g in range(256):
            for b in range(256):
                arr.append(to_list(r,g,b,probability[r][g][b]))
                progress += 1
        
    return arr     


def create_csv(probability): ##this function creats csv 
    myFile = open('train.csv', 'w', newline = '')
    with myFile:  
        writer = csv.writer(myFile)
        writer.writerow(["Red", "Green", "Blue", "Probability"])
        writer.writerows(data(probability))
    print('Training Completed')


def main():

    pixels = np.zeros((256,256,256))
    skin = np.zeros((256,256,256)) 
    non_skin = np.zeros((256,256,256))    
    probability = np.zeros((256,256,256))

    files_actual = os.listdir('image') 
    files_mask = os.listdir('mask')
    # len(files_actual)
    for i in range(5): ##iterating through all images
       
        image_actual_path = 'image\\'
        imgae_mask_path = 'mask\\'

        pix_val_actual = read_image(open_image(image_actual_path+files_actual[i])) ## storing the pixels of actual picture..
        pix_val_mask = read_image(open_image(imgae_mask_path+files_mask[i])) ## storing the pixels of mask picture..
        
        print(image_actual_path+files_actual[i], imgae_mask_path+files_mask[i])
        
        pixels, skin, non_skin = train_data(pixels, pix_val_actual, pix_val_mask, skin, non_skin) ## this returns the skin value and non_skin value 
#        
    probability = set_probability(pixels, skin, non_skin, probability) ## this returns the probability
    create_csv(probability) ## creating CSV from that probabilty and rgb
    
if __name__ == "__main__":
    
    main()