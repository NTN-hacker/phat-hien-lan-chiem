import cv2
import numpy as np

def cropImageRoi(image, roi):
    """
    crop image base on list cordinates was returned 
    from key roi into file setting
    """
    roi_cropped = image[
    int(roi[1]) : int(roi[1] + roi[3]), int(roi[0]) : int(roi[0] + roi[2])
]
    return roi_cropped

def roiFillPoly(image, lst):
    points = np.array(lst)
    temp_img = cv2.fillPoly(img= image, pts= [points], color= (0, 0 , 0))
    return temp_img

def processing(image):
    roi = []
    #crop image
    image_roi = cropImageRoi(image, roi)
    #resize image
    image_resize = cv2.resize(image_roi, (195, 185))
    #fill Poly the resized image
    temp = image_resize.copy()
    image_fill =  roiFillPoly(temp, roi)
    return image_fill

   