from colorama import Back
import cv2 
import numpy as np
from preprocessing import cropImageRoi, processing, roiFillPoly
import parameter
from parameter.setting import *
from back_subtraction import BackSubtraction
from bouding_box import boudingBox

class DetectObject(object):
    def detect_Obj(self, image_f, image_b):
        fg_cropImageRoi = cropImageRoi(image_f, Parameter["587c79e9b807da0011e33d3d"]["roi"][0])
        bg_cropImageRoi = cropImageRoi(image_b, Parameter["587c79e9b807da0011e33d3d"]["roi"][1])
        bg_cropImageRoi = cv2.resize(bg_cropImageRoi, (195,185))
        fg_cropImageRoi = cv2.resize(fg_cropImageRoi, (195,185))

        bg_cropImageFill = roiFillPoly(bg_cropImageRoi, Parameter["587c79e9b807da0011e33d3d"]["lst_roi"]["1"])
        bg_cropImageFill = roiFillPoly(bg_cropImageFill , Parameter["587c79e9b807da0011e33d3d"]["lst_roi"]["2"])

        temp = fg_cropImageRoi.copy()
        fg_cropImageFill = roiFillPoly(temp, Parameter["587c79e9b807da0011e33d3d"]["lst_roi"]["1"])
        fg_cropImageFill = roiFillPoly(temp, Parameter["587c79e9b807da0011e33d3d"]["lst_roi"]["2"])

        mask = BackSubtraction().backSubtraction(bg_cropImageFill, fg_cropImageFill)
        fgMask = BackSubtraction().preprocessing_backsubtraction(mask)
        cv2.imwrite("test_brightness.png", fgMask)
        cordinate, fg = boudingBox( fg_cropImageRoi, fgMask= fgMask)
        return cordinate, fg


