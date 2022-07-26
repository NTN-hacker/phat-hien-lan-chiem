from ast import Yield
from operator import index
import numpy as np
from math import *
from parameter.setting import *
import cv2
import matplotlib.pyplot as plt
import preprocessing

def get_iou(point_1, point_2):

    x_left_top = max(point_1[0], point_2[0]) 
    y_left_top = max(point_1[1], point_2[1])  
    x_right_bottom = min(point_1[2], point_2[2]) 
    y_right_bottom = min(point_1[3], point_2[3]) 

    if (x_left_top > x_right_bottom) or (y_left_top > y_right_bottom):
        return 0

    compute_iou = (x_right_bottom - x_left_top)*(y_right_bottom - y_left_top)

    #caculate area of each bounding boxes
    compute_bouding_1 = (point_1[0] - point_1[2])*(point_1[1] - point_1[3])
    compute_bouding_2 = (point_2[0] - point_2[2])*(point_2[1] - point_2[3])

    iou = compute_iou/float(compute_bouding_1 + compute_bouding_2 - compute_iou)

    # assert iou >= 0.0
    # assert iou <= 1.0
    return iou




