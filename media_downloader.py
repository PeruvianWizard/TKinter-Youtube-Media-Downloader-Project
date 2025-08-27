# Copyright (C) 2025 PeruvianWizard.
# All Rights Reserved.
# It may be used however you want as long as it doesn't break a law.

from pytubefix import YouTube
from pytubefix.cli import on_progress
import subprocess
import os

def download_media(url, only_video=False, only_audio=False):
    yt = YouTube(url, on_progress_callback=on_progress)

    if only_video:
        print("Downloading video...")
        ys = yt.streams.get_highest_resolution(False)
        ys.download(filename=yt.title+'.mp4')
    elif only_audio:
        print("Downloading audio...")
        ys = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        ys.download(filename=yt.title +'.mp3', output_path=os.path.expanduser("~")+"/Downloads")
    else:
        print("Downloading video with audio...")
        video_path = os.path.abspath(yt.title+'.mp4')
        audio_path = os.path.abspath(yt.title+'.mp3')
        output_path = os.path.join(os.path.expanduser("~"), "Downloads", yt.title + '.mp4')
        ys = yt.streams.get_highest_resolution(False)
        ys.download(filename=yt.title+'.mp4')
        ys = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        ys.download(filename=yt.title+'.mp3')

        subprocess.run([
            'ffmpeg', 
            '-i', video_path,
            '-i', audio_path,
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-strict', 'experimental',
            output_path
        ])

        os.remove(video_path)
        os.remove(audio_path)
