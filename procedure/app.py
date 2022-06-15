from datetime import datetime
from charset_normalizer import detect
import streamlit as st
from warning import WarningObject
from parameter.setting import *
import time

st.header("Detect object signwalk encroachment")

id = '587c79e9b807da0011e33d3d'

wb = WarningObject(id)
#st.image("test\CAM_DBP\\test\\result.png", caption= "Camera at Dien Bien Phu street, Binh Thanh", width= 385)

# Phat video camera
st.header("Camera 001")

video_holder = st.empty()
warning_holder = st.empty()
while True:
    img = wb.get_url_save_image()
    video_holder.image(img)

    # Phat hien lan chiem
    flag, fg = wb.detect(img)

    if (flag == True):
        warning_holder.image(fg, "Object Signwalk Encroachment")
        st.balloons()
        time_violate = datetime.now()
        st.write(f"Thời gian ghi nhận: {time_violate}")
    else:
        pass

    time.sleep(Parameter[id]["time-update"])

