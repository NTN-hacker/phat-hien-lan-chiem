import cv2
from cv2 import CAP_PROP_XI_IMAGE_DATA_BIT_DEPTH
import numpy as np
import imgcompare
from preprocessing import cropImageRoi
from parameter.setting import Parameter


class DifferenceFrame(object):
    def caculate_diff_frame(self, camera_id, camera_name, image1, image2, cordinate):
        """
        This function used to caculate difference degree between two frame
        """
        path_result = f"test\\{camera_name}\\test\\result.png"
        path_test = f"test\\{camera_name}\\test\\test.png"

        percentage = float(1)
        try: 
            result = cropImageRoi(cropImageRoi(image1, Parameter[camera_id]["roi"][0]), cordinate)
            test   = cropImageRoi(cropImageRoi(image2, Parameter[camera_id]["roi"][0]), cordinate)

            cv2.imwrite(path_result, result)
            cv2.imwrite(path_test, test)
            percentage = imgcompare.image_diff_percent(path_result, path_test)
        except Exception as e:
            print("Error open image", str(e))
            pass
        return percentage

       
name = "CAM_DBP" 
# name_slit = name.split("_")
print(name.split("_")[-1].lower())