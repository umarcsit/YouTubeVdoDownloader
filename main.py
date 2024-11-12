from pytubefix import YouTube
from pytubefix.cli import on_progress
import re
import os
n=-1
while n<1:
    # url = "https://www.youtube.com/watch?v=OJEzV8cqJUI&t=17s"

    url=input("\n Please Enter URL: ")
    # Specify the folder to save the video
    save_path = "video"
    # Create the folder if it doesn't exist
    os.makedirs(save_path, exist_ok=True)

    yt = YouTube(url, on_progress_callback=on_progress)
    # print("Title:", yt.title)

    ys = yt.streams.get_highest_resolution()
    # Check if the video already exists in the "video" folder
    if not os.path.exists(os.path.join(save_path, ys.default_filename )):
        ys.download(output_path=save_path,skip_existing=True)
    

