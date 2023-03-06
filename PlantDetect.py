import streamlit as st
from aip import AipImageClassify

st.title("Hello world")
st.title("植物识别")

APP_ID='27956980'
API_KEY='fvZQAoGvoMas0Kmvke0oycHV'
APP_SECRET='Q7MXuXHFcwFn2Fld60ECGX4SmA8Wn1Pg'
client=AipImageClassify(APP_ID,API_KEY,APP_SECRET)

uploaded_file=st.file_uploader('选择一张照片',type=['jpg','png'])
if uploaded_file:
    st.image(uploaded_file,caption='已选文件',use_column_width=True)
    bs=uploaded_file.read()

    res=client.plantDetect(bs)
    st.title('有可能的植物及其概率')
    res['result']
    st.title("该植物最有可能是")
    st.title(res['result'][0]['name'])