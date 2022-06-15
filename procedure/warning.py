from time import time
import cv2
import numpy as np
import time
import subprocess
from object_detection import DetectObject
from input import Input
from diff_frame import DifferenceFrame
from parameter.setting import *
from distance_point import *
import streamlit as st

class WarningObject(object):

    LENGTH_ROOT_FAULT = 10


    def __init__(self, camera_id):
        self.stack = Input().init_stack(10)
        self.id = camera_id
        self.cordinate_threshold = [[10, 6, 112, 90]]

        while (self.stack.len < self.LENGTH_ROOT_FAULT):
            self.stack.stack = self.stack.put(self.get_url_save_image()) 
            print("Init data...")

    def get_url_save_image(self):
        url = f'''curl "http://giaothong.hochiminhcity.gov.vn:8007/Render/CameraHandler.ashx?id={self.id}"   -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"   -H "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ja;q=0.4"   -H "Cache-Control: no-cache"   -H "Connection: keep-alive"   -H "Cookie: GUEST_LANGUAGE_ID=vi_VN; _ga=GA1.3.1268639869.1637042764; ASP.NET_SessionId=whhmth0edrixbfoydshhg321; .VDMS=2CF9AF29877107034C56C9D51CBEAE47FD899DED662CFBB5CBCEC7A62F97DB60F5C8FE341A12F6AD3E69E32B9546499219D77B0A76197BD52BF5F71C799B7F95E1A68A7D5A94399BE5C38D66786A8983ECBD5FB32FC51D47CE7DCF103EE11B65EDACE38441D20196BAAA45CC40CC32998E1D7AE4; _frontend=\u0021nw6dooWn8pGIKqFmil1P2lbeEwNhYVww9WP2z4x6h9kTylkUspJirO5K6GJzkWZkAtNCeYsAB3gpIT8=; CurrentLanguage=vi; _gid=GA1.3.446387129.1652343216; _pk_ref.1.2f14=%5B%22%22%2C%22%22%2C1652343216%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.2f14=a912fbe1c12c6e6e.1652249178.2.1652343264.1652343216."   -H "Pragma: no-cache"   -H "Upgrade-Insecure-Requests: 1"   -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"   --compressed   --insecure '''
        process = subprocess.Popen(url , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        self.img = cv2.imdecode(np.fromstring(stdout, dtype=np.uint8), 1)
        return self.img

    def detect(self, img):
        flag = False
        cordinate, fg = DetectObject().detect_Obj(img, cv2.imread("procedure\parameter\\base_image\dbp_bt_background.png"))

        #Instert new image to stack
        self.stack.pop()
        self.stack.put(img)

        print(cordinate)
        percentages = []
        if (cordinate != 0):
            for i in range(self.stack.len - 2):
                diff_frame_ = DifferenceFrame().caculate_diff_frame(self.stack.pop(), self.stack.stack[i], cordinate)
                percentages = percentages + [diff_frame_]
            percentage = np.mean(percentages)
            print(percentage)
            print(percentages)

            if (percentage > Parameter[self.id]["threahold"]["percentage"]):
                pass
            else:        
                left_distance = (distance(getPoint(cordinate)[0], getPoint(self.cordinate_threshold[-1])[0]))
                right_distance = (distance(getPoint(cordinate)[1], getPoint(self.cordinate_threshold[-1])[1]))             
                if (left_distance > 2 and right_distance > 2):
                    self.cordinate_threshold = self.cordinate_threshold + [cordinate]
                    flag = True
                else:
                    pass
        return flag, fg

    # def request(self):
    #     i = 0
    #     cordinate_threshold = [[10, 6, 112, 90]]
    #     while True:
    #         if i < self.LENGTH_ROOT_FAULT: # nếu có ptu null thì thực hiện nạp thêm ảnh vào cuối stack trong hàm ktra nếu stack đã full thì xóa ptu số 0
    #             i += 1
    #             self.stack.stack = self.stack.put(self.get_url_save_image(self.url)) 
    #             print("Dang nap du Liệu ")
    #         else:
    #             cordinate, fg = DetectObject().detect_Obj(self.stack.pop(), cv2.imread("procedure\parameter\\base_image\dbp_bt_background.png"))
    #             print(cordinate)
    #             percentages = []
    #             if (cordinate != 0):
    #                 for i in range(self.stack.len - 2):
    #                     diff_frame_ = DifferenceFrame().caculate_diff_frame(self.stack.pop(), self.stack.stack[i], cordinate)
    #                     percentages = percentages + [diff_frame_]
    #                 percentage = np.mean(percentages)
    #                 print(percentage)
    #                 print(percentages)

    #                 if (percentage > Parameter[self.id]["threahold"]["percentage"]):
    #                     print("Không cảnh báo")
    #                 else:        
    #                     left_distance = (distance(getPoint(cordinate)[0], getPoint(cordinate_threshold[-1])[0]))
    #                     right_distance = (distance(getPoint(cordinate)[1], getPoint(cordinate_threshold[-1])[1]))             
    #                     if (left_distance > 2 and right_distance > 2):
    #                         cordinate_threshold = cordinate_threshold + [cordinate]
    #                         # print("Cảnh báo")
    #                         # cv2.imshow("Object have signed", fg)
    #                         # cv2.waitKey(0)
    #                         # cv2.destroyAllWindows()  
                            
    #                     else:
    #                         pass
    #             i = 9

    #         time.sleep(Parameter[self.id]["time-update"])


