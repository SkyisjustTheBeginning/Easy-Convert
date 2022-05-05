import cv2
import random
import numpy as np
import os
def conversion(SIZE,path):
     image_data = []
     for img in os.listdir(path):
         try:
              img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
              newarray = cv2.resize(img_array,(SIZE,SIZE))
              image_data.append([newarray])
         except:
              pass
     random.shuffle(image_data)
     image_data = np.array(image_data)
     return image_data
     
        
size = int(input("Size of image :   "))
path = str(input("Path to Folder :    "))

data = conversion(size,path)
print(data)

