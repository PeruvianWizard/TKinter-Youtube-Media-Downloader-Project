# Copyright (C) 2025 PeruvianWizard.
# All Rights Reserved.
# It may be used however you want as long as it doesn't break a law.

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import media_downloader

# Function for download button
def download_media():
    url = str(link_entry.get())
    
    if str(media_type.get()) == "MP4":
        media_downloader.download_media(url)
    else:
        media_downloader.download_media(url, only_audio=True)
    tk.Label(root, text="Video/Audio downloaded successfully!", fg="Red").grid(row=3, column=1)

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("600x300")

# Font and Label
font = tkFont.Font(family="Arial", size=20)
main_lb = tk.Label(root, text="YouTube Downloader", font=font)
main_lb.grid(row=0, column=1, sticky=tk.NSEW, pady=30)

# Another Label
link_lb = tk.Label(root, text="Link: ")
link_lb.grid(row=1, column=0)

# Entry
link_entry = tk.Entry(root)
link_entry.grid(row=1, column=1, sticky=tk.NSEW)
link_entry.focus()

# Combobox
media_type = ttk.Combobox(root, values=["MP3", "MP4"], state="readonly", width=4)
media_type.grid(row=1, column=2)

# Button
b1 = tk.Button(root, text="Download", command=download_media, height=2, width=15)
b1.grid(row=2, column=1, pady = 30)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

if __name__ == '__main__':
    root.mainloop()