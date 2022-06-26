import cv2
import numpy as np
import datetime

def boudingBox(fg_cropImageRoi, fgMask):
    fg = fg_cropImageRoi.copy()
    cordinate = 0
    #You can choose type connectivity with value about from 4 to 8
    connectivity = 4
    output = cv2.connectedComponentsWithStats(fgMask, connectivity, cv2.CV_32S)
    (numLabels, labels, stats, centroids) = output
    for i in  range(0, numLabels):
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        area = stats[i, cv2.CC_STAT_AREA]
        if (area > 400) and (w > 30) and (h > 30) and (w < fg.shape[0]) and (h < fg.shape[1]): # and (x != 0) and (y != 0):
            cv2.rectangle(fg, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cordinate = [x, y, x + w, y + h]
    
    # cv2.imshow('Roi Image 2' , fg)
    time = datetime.datetime.now()
    cv2.imwrite("test/CAM_DBP/result/" + str(str(time).replace(" ","_").replace(":","-").split(".")[0]) + ".png", fg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return cordinate, fg