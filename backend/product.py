from PIL import Image
import os
import easyocr
import cv2
from matplotlib import pyplot as plt
from spellchecker import SpellChecker
import numpy as np
import re

class Product:
    #" instance variables:
    # list - words extracted from image 
    # set - hidden sugars
    # set - carcinogens
    # ... potentially more 
    # "

    words = []

    #constructor
    def __init__(self, image):
        #instance variable of type Image called image
        self.image = image
        reader = easyocr.Reader(['en'])
        self.ingredients = ' '.join(reader.readtext(self.image, paragraph="True", detail = 0))
        self.processIngreds()
        

    def processIngreds(self):
        words = re.split(r'[,\'\":(){}.\[\]\=_\;\\]', self.ingredients)
        misread = []
        spell = SpellChecker()

        for i in range(len(words)):
            words[i] = words[i].strip()
            words[i] = ' '.join(words[i].split())

        while ("" in words):
            words.remove("")

        for i in range(len(words)):
            if " " in words[i]:
                wordsSet = words[i].split()
                for j in range(len(wordsSet)):
                    temp = wordsSet[j]
                    if temp != spell.correction(temp):
                        temp = spell.correction(temp)
                        if (temp is None):
                            temp = wordsSet[j]
                    wordsSet[j] = temp
                words[i] = " ".join(wordsSet)


        words[len(words)-1] = words[len(words)-1].replace("and ", "")
        words[0] = words[0].replace("ingredients", "")
        words[0] = words[0].replace("Ingredients", "")
        words[0] = words[0].replace("INGREDIENTS", "")

        while ("" in words):
            words.remove("")

        self.words = words


    def hiddenSugars(self):
        hiddenSugars = ["aspartame", "sucralose", "acesulfame potassium", "saccharin", "neotame", "sorbitol", "xylitol", "erythritol", "maltitol", "maltodextrin"]
        sugarsSimilar = []
        
        hiddenSugars_lower = [sugar.lower() for sugar in hiddenSugars]
        words_lower = [word.lower() for word in self.words]

        for word in words_lower:
            for sugar in hiddenSugars_lower:
                if sugar in word:
                    sugarsSimilar.append(sugar)

        return sugarsSimilar

    
    def carcinogens(self, words):
        carcinogens = ["butylated hydroxyanisole", "potassium bromate", "acrymalide", "sodium nitrate", "sodium nitrite", "propylene oxide", "yellow 6", "yellow #6", "red 6", "red #6"]
        carcSimilar = []

        carcinogens_lower = [carc.lower() for carc in carcinogens]
        words_lower = [word.lower() for word in self.words]

        for word in words_lower:
            for carc in carcinogens_lower:
                if carc in word:
                    carcSimilar.append(carc)

        return carcSimilar
    
    def getSugars(self):
        result = self.hiddenSugars()
        return result
    
    def getCarcs(self):
        return self.carcinogens(self.words)


    