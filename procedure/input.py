from concurrent.futures import process
from parameter.setting import Parameter
from stack import NumpyStack
import subprocess
import cv2
import numpy as np

class Input(object):


    ROOT_IMAGE_BASE = 'parameter/base_image/'

   

    def init_stack(self, length):
        self.stack = NumpyStack(length)
        return self.stack

    def get_feature_image(self, camera_name):
        request = {'camera': None, 'base_img': None, 'type': 'CAM_DBP'}
        if camera_name == 'dbp_bt':
            request['camera']   = 'dbp_bt'
            request['base_img'] = self.get_background_image(camera_name= camera_name)
            request['type']     = 'CAM_DBP'
        return request

    def get_background_image(self, camera_name):
        return self.ROOT_IMAGE_BASE + camera_name + "_background.png"
    

