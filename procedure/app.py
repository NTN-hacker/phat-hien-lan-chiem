from datetime import datetime
from charset_normalizer import detect
import streamlit as st
from warning import WarningObject
from parameter.setting import *
import time


st.write("Hello")
id = ''

st.header("Detect object signwalk encroachment")

option = st.selectbox("How to check camera?", ("CAM_DBP", "CAM_VL_NTT", "CAM_TOKY", "CAM_SG"))

if (option == 'CAM_DBP'):
    id = '587c79e9b807da0011e33d3d'
elif (option == 'CAM_TOKY'):
    id = '589ad89eb3bf7600110283ac'
elif (option == 'CAM_VL_NTT'):
    id = '5ad06a0d98d8fc001102e27'
elif (option == 'CAM_SG'):
    id = '5f000ab3942cda00169ee00b'
else:
    st.warning("Not optional! Error")

if (id != ''):
    wb = WarningObject(id)
    #st.image("test\CAM_DBP\\test\\result.png", caption= "Camera at Dien Bien Phu street, Binh Thanh", width= 385)

    # Phat video camera
    st.header(f"Camera {id}")

    video_holder = st.empty()
    warning_holder = st.empty()
    overview_holder = st.empty()
    st.write(id)
    while True:
        img = wb.get_url_save_image()
        video_holder.image(img)

        # detect signwalk encroachment
        flag, fg, img = wb.detect(img)

        if (flag == True):
            warning_holder.image(fg, "Object Signwalk Encroachment")
            overview_holder.image(img, "Image overview have to contain object signmalk encroachment")
            st.balloons()
            time_violate = datetime.now()
            st.write(f"Thời gian ghi nhận: {time_violate}")
        else:
            pass

        time.sleep(Parameter[id]["time-update"])

