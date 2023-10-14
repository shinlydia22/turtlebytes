import os
import easyocr
import cv2
# from matplotlib import pyplot as plt
import numpy as np
import torch
# print(torch.cuda.is_available())
reader = easyocr.Reader(['en'])
result = reader.readtext(r"C:\Users\wwzb2\Downloads\water_list.jpg", paragraph=False)
result[0:10]