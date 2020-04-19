#resizing function
def resize(img,scale):
  print('Original Dimensions : ',img.shape)
  scale_percent = scale      # percent of original size
  width = int(img.shape[1] * scale_percent / 100)
  height = int(img.shape[0] * scale_percent / 100)
  dim = (width, height)
  # resize image
  resized = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)
  print('Resized Dimensions : ',resized.shape)
  return resized
#color lab print
def img_to_lab(img):
	return (cv2.cvtColor(img, cv2.COLOR_BGR2LAB))
#splitting lab image to channels
def channels(img):
	l,a,b=cv2.split(img)
	return l,a,b
#-----Applying CLAHE (Contrast Limited Adaptive Histogram Equalization) to L-channel-------------------------------------------
def contrast(l):
	clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
	cl = clahe.apply(l)
	return cl
#-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
def merge(cl,a,b):
	limg=cv2.merge((cl,a,b))
	return limg
#-----Converting image from LAB Color model to RGB model--------------------
def lab_to_img(img):
	return cv2.cvtColor(img,cv2.COLOR_LAB2BGR)

  