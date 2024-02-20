import os
import streamlit as st
from embedchain import App

st.title("YouTube Podcast Bot!")
st.subheader("Share a YouTube Podcast link and ask the bot questions about it")

YTpodcast_bot = App()

YTpodcast_bot.add("https://www.youtube.com/watch?v=yqfKsoDLff8")
response = YTpodcast_bot.query("What is the summary of the video?")
st.write(response)
