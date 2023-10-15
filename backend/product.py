from PIL import Image
import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import re

class Product:
    #" instance variables:
    # list - words extracted from image 
    # set - hidden sugars
    # set - carcinogens
    # ... potentially more 
    # "

    #constructor (for testing):
    def __init__(self):
        self.yay = 1

    #real constructor
    def __init__(self, image):
        #instance variable of type Image called image
        self.image = image
        reader = easyocr.Reader(['en'])
        self.ingredients = ' '.join(reader.readtext('./ingredients.jpg', paragraph="True", detail = 0))
        

    def processIngreds(self):
        words = re.split(r'[,()\[\]_\;\\]', self.ingredients)
        for i in range(len(words)):
            words[i] = words[i].strip()
        words.remove("")
        words[len(words)-1] = words[len(words)-1].replace("and ", "")

    #" methods:
    # constructor
    # sugars - makes set w/ hidden sugars in the product
    # carcinogens - same as sugar
    # getSugars, getCarcinogens, getName
    # 
    # "