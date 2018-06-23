from PIL import Image
import pandas as pd


def open_image(src): 
    return Image.open(src,'r')

                   
def test(probability, path):
    
    im = open_image(path)
    temp = im.copy()
    create_image(temp, probability)


def create_image(im,probability): 
    
    width, height = im.size

    pix = im.load()
  
    for i in range(width):
        for j in range(height):
            r,g,b = im.getpixel((i,j))
            row_num = (r*256*256) + (g*256) + b #calculating the serial row number 
            if(probability['Probability'][row_num] <0.555555):
                pix[i,j] = (0,0,0)
            else:
                pix[i,j] = (255,255,255)
                
    saveImage(im)
    
def saveImage(image): ## saving image
    image.save('test/result.jpg')

def main():

    print("Reading CSV...")
    probability = pd.read_csv('train1.csv') # getting the rows from csv    
    print('Data collection completed') 
    
    path = 'test/1.jpg'
    test(probability, path) # this tests the data
    print("Image created")


if __name__ == "__main__":
    main()

