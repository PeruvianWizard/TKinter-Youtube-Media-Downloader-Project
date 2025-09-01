# Copyright (C) 2025 PeruvianWizard.
# All Rights Reserved.
# It may be used however you want as long as it doesn't break a law.

import tkinter as tk
from tkinter import ttk
import media_manager

# Limit for recently downloaded media dictionary
RECENT_LIMIT = 10

# Dictionary to hold recently downloaded media.
# Restores from backup is there is any. Else, the function returns an empty dicitonary.
recently_downloaded = media_manager.restore_backup()

# Function for download button
def download_media():
    # This line tells the interpreter that the function will be using the global variable recently_downloaded
    global recently_downloaded
    url = None

    # Get the content from the combobox
    content = str(recent_cbox.get())
    
    # Attempt to get key if content is a previously downloaded song
    found_url = recently_downloaded.get(content)
    
    # Decided whether content from combobox is an url or the name of a previosuly downloaded song
    if media_manager.check_youtube_url(content):
        url = content
    elif found_url != None:
        url = found_url
    else:
        print("Name provided is not an url or recently downloaded media")  # Display this message to user as label or warning window
        return

    # Get title of song
    song_title = media_manager.media_title(url)
    print(f"Media Title: {song_title}")
    
    # Download in MP3 or MP4 format based on user choice
    if str(media_type.get()) == "MP4":
        media_manager.download_media(url)
    else:
        media_manager.download_media(url, only_audio=True)

    # Add the song title with its url to the beginning of the recently_donwloaded dictionary
    recently_downloaded = {**{song_title: url}, **recently_downloaded}

    # Pop the last element of the recently downloaded dictionary if it goes over the limit.
    if len(recently_downloaded) > RECENT_LIMIT:
        recently_downloaded.popitem()

    # Set the recent_cbox values equal to the recently_downloaded keys
    recent_cbox['values'] = list(recently_downloaded.keys())

    # Successful download label
    success = tk.Label(root, text="Media downloaded successfully!", fg="Red")
    success.grid(row=3, column=1)
    root.after(3000, success.destroy)

# Main Window
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("600x300")

# Youtube label
main_lb = ttk.Label(root, text="YouTube Downloader", font=("Arial", 20))
main_lb.grid(row=0, column=1, sticky=tk.NS, pady=30)

# Link label
link_lb = ttk.Label(root, text="Link: ", font=("Arial", 12))
link_lb.grid(row=1, column=0, sticky=tk.NS)

# Combobox where url will be entered or names will be selected
recent_cbox = ttk.Combobox(root, values=list(recently_downloaded.keys()))
recent_cbox.grid(row=1, column=1, sticky=tk.NSEW)
recent_cbox.focus()

# Combobox to choose type of media
media_type = ttk.Combobox(root, values=["MP3", "MP4"], state="readonly", width=4)
media_type.grid(row=1, column=2)
media_type.set("MP4")

# Download button
download_button = ttk.Button(root, text="Download", command=download_media, padding=(15,18))
download_button.grid(row=2, column=1, pady = 30)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

if __name__ == '__main__':
    root.mainloop()

    # Backup the recently_downloaded list from current session to be used in the next one.
    # Backup from previous session will get overwritten.
    if len(recently_downloaded) != 0:
        media_manager.download_backup(recently_downloaded)