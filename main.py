import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('超寝不足：3時間')

#st.write('プログレスパー')
'Start!'

latest_iteration=st.empty()
bar = st.progress(0)

for i in range(1,100):
    latest_iteration.text(f'Now Loading {i + 1}')
    bar.progress(i)
    load_time = 5 / i
    time.sleep(load_time)
st.write('Finish Loading!')

# 画像表示
st.write('Display Image:')
img = Image.open('jetson_nano_2gb.jpg')
if st.checkbox('show Image'):
    st.image(img,caption='Jetson Nano 2GB',use_column_width=True)


st.sidebar.write('Interactive Wdgets')

# ボタン押したら表示
left_colum,right_colum = st.columns(2)
button = left_colum.button('display right')
if button:
    right_colum.write('right colum_here')

# クリックしたら表示する
expander = st.expander('cellphon')
expander.write('call back cellphon')

expander1 = st.expander('cellphon2')
expander1.write('call back cellphon2')

expander2 = st.expander('cellphon3')
expander2.write('call back cellphon3')

# 入力
hobby = st.sidebar.text_input('tell me your hobby')
# 特定範囲の数値入力
fine = st.sidebar.slider('how are you?',0,100,50)

hobby,'!? me too!'
'condition:',fine

num = st.selectbox(
    'あなたが好きな数字',
    list(range(1,11))
)    
'you like ',num,'!'

# データフレームの表示
st.write('DataFrame')

df = pd.DataFrame(
  np.random.rand(10,2),
  columns=['a','b']
)

st.table(df.style.highlight_max(axis=0)) #表で表示
#st.line_chart(df) #線グラフで表示
#st.area_chart(df) #塗りつぶし線グラフで表示
#st.bar_chart(df) #棒グラフで表示
#st.map(df)