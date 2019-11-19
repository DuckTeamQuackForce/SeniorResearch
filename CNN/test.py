# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import os 
import cv2
import pickle
from tqdm import tqdm

DATADIR = "C:\\Users\\sawye\\OneDrive - Eastern Connecticut State University\\Senior Research\\Training_set"

CATEGORIES = ["Mudkip","Eevee", "Pikachu"]

img_size = 150

training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path): 
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                img_array = cv2.resize(img_array, (img_size, img_size))
                training_data.append([img_array, class_num])
                plt.imshow(img_array, cmap=plt.cm.binary)
                plt.xlabel(class_num)
                plt.show()
            except Exception as e:
                print(e)
            break
    
create_training_data()


