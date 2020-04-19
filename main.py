import numpy as np
!pip install pytesseract
! apt install tesseract-ocr
! apt install libtesseract-dev
! pip install Pillow
! pip install pytesseract
import pytesseract
from PIL import ImageEnhance, ImageFilter, Image
import cv2
from pytesseract import Output
import re
import functions

custom_config = r'-l eng --oem 3 --psm 3'

#read image
img=cv2.imread('image.jpg')
#resizing image
img=resize(img,200)

#lab print
img=img_to_lab(img)

#converting image into channels
l,a,b=channels(img)

#increasing contrast
cl=contrast(l)

#merge back the channels
img=merge(cl,a,b)

#from lab image to original image
img=lab_to_img(img)

#detect text from new image
txt=pytesseract.image_to_string(img,config=custom_config)


#applying regex on the detected txt.
name=re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', img_string)
aadhar= re.fullmatch("^\d{4}\s\d{4}\s\d{4}$", img_string)
year=re.findall('^(19|20)\d{2}$',img_string)
