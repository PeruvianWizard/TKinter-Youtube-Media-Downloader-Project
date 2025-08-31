# Youtube Media Downloader Project

This a project solely coded in python, and it is meant to be used to experiment 
with modules, libraries (e.g. pytubefix, tkinter), and common coding practices.
The software has only been tested on Windows 11, so the installation instructions
are for Windows 11.

## Installation

To get this project to work, you will need ffmpeg, an open-source software that 
offers tools to manipulate multimedia, such as, videos, audios, streams, etc.
Moreover, you'll need to install the python library, pytubefix, to your virtual 
environment. The pytubefix library is used to download the videos/audios from 
Youtube.

### Installing pytubefix

1. Open terminal in virtual environment
2. Execute command, pip install pytubefix

### Installing ffmpeg

1. Go to https://ffmpeg.org/download.html
2. Select Windows and then click on Windows builds by BtbN
3. On the github website, click on "ffmpeg-master-lastest-win64-gpl-shared.zip"
4. Extract the .zip file anywhere you want to
5. Add the path of the bin file (the one inside the ffmpeg folder) to the PATH
   environment variable (Start->Search "Edit the system environment variables"
   ->Environment Variables...)
7. Open the command prompt and execute "ffmpeg -version" to make sure it was
   installed correctly
