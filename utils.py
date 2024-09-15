import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras import backend as K

plt.style.use("dark_background")

def plot_from_image_path(rows,cols,list_image_path,list_mask_path):
    fig=plt.figure(figsize=(12,12))
    for i in range(1,rows*cols+1):
        fig.add_subplot(rows,cols)
        img_path=list_image_path[i]
        mask_path=list_mask_path[i]
        image= cv2.imread(img_path)
        image=cv2.cvt.Color(image,cv2.COLOR_BGR2RGB)
        mask=cv2.imread(mask_path)
        plt.imshow(image)
        plt.imshow(mask)
    plt.show()


