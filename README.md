## OCR using tesseract and opencv

All functions are not not comnined so to choose the best combination for the specific image example which thresholding or wheather to contrast the image or how to resize the image.


Best function found by experimenting is transforming image into its color channels then increase contrast or the black and white channel remove noise and then merge then back and then apply tesseract.

Binarization of image using thresholding is suggest many places but it leads to a lot of noise and important pixels might get removed from characters of letters.

### functions implemented 

- Resizing
- converting image to lab print
- spliting the channels of the image
- increasing contrast of the image
- merge the increased contrast black and white image to form new image
- regex to find required information in the extracted text.


### functions yet to be implemented

- ROI and bounding box of image
- better regex
- training tesseract on the font format of aadhar
- extaracting using Area of interest only.