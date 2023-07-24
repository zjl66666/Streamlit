import base64

import streamlit as st
from aip import AipImageProcess
st.title("Hello world")
st.title("图片风格转换🎨")

APP_ID='31014756'
API_KEY='4eLe0vI67g8KHPEXKlwjhmwt'
APP_SECRET='pjoLysTDGbP5QGbDjyt2kgqiZXzROjq2'
client=AipImageProcess(APP_ID,API_KEY,APP_SECRET)
options = {
    '卡通画风格': 'cartoon', '铅笔风格': 'pencil', '彩色铅笔画风格': 'color_pencil',
    '彩色糖块油画风格': 'warm', '神奈川冲浪里油画风格': 'wave', '薰衣草油画风格': 'lavender',
    '奇异油画风格': 'mononoke', '呐喊油画风格': 'scream', '哥特油画风格': 'gothic'
}

uploaded_file=st.file_uploader('选择需要加工的照片')
style = st.sidebar.selectbox('选择需要加工的风格',options.keys())
if uploaded_file:
    st.image(uploaded_file,caption='已选文件',use_column_width=True)
    img_data=uploaded_file.read()

    st.title('加工后的图像')
    # 如果有可选参数
    select = {}
    select['option'] = options[style]
    res = client.styleTrans(img_data, select)
    st.image(base64.b64decode(res['image']))
