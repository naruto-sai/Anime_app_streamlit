import streamlit as st
import pandas as pd
import os
from matplotlib import image
import plotly.express as px

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# absolute path of directory_of_interest
dir_of_interest = os.path.join(FILE_DIR,"resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "all.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data.csv")

st.title("Anime data-DashBoard")
st.image(image=image.imread(IMAGE_PATH))

df=pd.read_csv(DATA_PATH)
st.dataframe(df.iloc[:,1:])

col1, col2 = st.columns(2)

fig_1 = px.histogram(df.score)
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df.members)
col2.plotly_chart(fig_2, use_container_width=True)

fig=px.bar(df.members)
st.plotly_chart(fig)

index=df.ranked.sort_values(ascending=True)[:21].index
values=[df.title[i] for i in index[::2] ]
url=[df.img_url[i] for i in index[::2] ]

choice=st.selectbox('Choose Anime',options=['..','Top 10 anime by rank', 'One Piece', 'Naruto'])
if(choice=='Top 10 anime by rank'):
    st.header('** Top 10 Best Anime by Rank**')
    j=0
    col3,col4=st.columns(2)
    for i in range(len(values)//2):

        col3.image(url[j],caption=values[j], use_column_width=True)

        col4.image(url[j+1],caption=values[j+1], use_column_width=True)
        j+=2
elif(choice=='One Piece'):
    drop=st.selectbox('Choose One',options=['Image','Binks_Sake','OP AMV'])
    if(drop=='Image'):
        IMAGE_PATH = os.path.join(dir_of_interest, "images", "OnePiece_1.jpg")
        st.image(image.imread(IMAGE_PATH))
    elif(drop=='Binks_Sake'):
        V_PATH = os.path.join(dir_of_interest,'videos', "Binks_Sake.mp4")
        st.video(open(V_PATH, 'rb').read())
    elif(drop=='OP AMV'):
        V_PATH = os.path.join(dir_of_interest,'videos', "One_Piece_OST.mp4")
        st.video(open(V_PATH, 'rb').read())
elif(choice=='Naruto'):
    drop=st.selectbox('Choose One',options=['Image','Pain','Itachi Sama', 'Jiraya Sensei'])
    if(drop=='Image'):
        IMAGE_PATH = os.path.join(dir_of_interest, "images", "uchiha_itachi.jpg")
        st.image(image.imread(IMAGE_PATH))
    elif(drop=='Pain'):
        V_PATH = os.path.join(dir_of_interest,'videos', "Pain's_Theme_Song.mp4")
        st.video(open(V_PATH, 'rb').read())
    elif(drop=='Itachi Sama'):
        V_PATH = os.path.join(dir_of_interest,'videos', "Itachi_AMV.mp4")
        st.video(open(V_PATH, 'rb').read())
    elif(drop=='Jiraya Sensei'):
        V_PATH = os.path.join(dir_of_interest,'videos', "Jiraya_The_Gallant.mp4")
        st.video(open(V_PATH, 'rb').read())
    
