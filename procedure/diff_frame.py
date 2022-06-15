import cv2
import numpy as np
import imgcompare
from preprocessing import cropImageRoi
from parameter.setting import Parameter


class DifferenceFrame(object):
    def caculate_diff_frame(self, image1, image2, cordinate):
        """
        This function used to caculate difference degree between two frame
        """
        percentage = float(1)
        result = cropImageRoi(cropImageRoi(image1, Parameter["587c79e9b807da0011e33d3d"]["roi"][0]), cordinate)
        test   = cropImageRoi(cropImageRoi(image2, Parameter["587c79e9b807da0011e33d3d"]["roi"][0]), cordinate)

        cv2.imwrite("test\CAM_DBP\\test\\result.png", result)
        cv2.imwrite("test\CAM_DBP\\test\\test.png", test)

        percentage = imgcompare.image_diff_percent("test\CAM_DBP\\test\\result.png", "test\CAM_DBP\\test\\test.png")
        
        return percentage
