# Copyright (C) 2025 PeruvianWizard.
# All Rights Reserved.
# It may be used however you want as long as it doesn't break a law.

from pytubefix import YouTube
from pytubefix.cli import on_progress
from urllib.parse import urlparse
import subprocess
import os
import _pickle

# function to back up dictionary into text file
def download_backup(dic):
    try:
        with open("media_urls.txt", "wb") as urls_save:
            _pickle.dump(dic, urls_save)
            print("BACKUP_CREATION_SUCCESS: Backup created successfully.")
    except Exception:
        print("BACKUP_CREATION_FAILURE: Backup could not be created.")

# function to restore backup from text file
def restore_backup():
    dic = {}
    try:
        with open("media_urls.txt", "rb") as urls_open:
            dic = _pickle.load(urls_open)
            print("BACKUP_RESTORATION_SUCCESS: Backup restored successfully.")
            return dic
    except Exception:
        print("BACKUP_RESTORATION_FAILURE: There is no backup to restore.")
        return {}

# Checks if provided text is a valid URL. Returns true if URL is valid or false if otherwise
def check_youtube_url(possible_url):
    try:
        is_url = urlparse(possible_url)
        if all([is_url.scheme, is_url.netloc]):
            if 'youtu.be' in possible_url or 'youtube.com' in possible_url:
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False

# Returns youtube video title of provided url
def media_title(url):
    yt = YouTube(url)
    return yt.title

# Downloads media given url into Downloads folder
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
