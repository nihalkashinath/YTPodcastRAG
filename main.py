import os
from embedchain import App

YTpodcast_bot = App()

YTpodcast_bot.add("https://www.youtube.com/watch?v=yqfKsoDLff8")
YTpodcast_bot.query("What is the summary of the video?")

