import tkinter
import customtkinter
from pytube import YouTube
from PIL import Image, ImageTk
import requests
import os

appVersion = "Version 1.0"

appIcon = "assets\YouTube_Logo.ico"

customtkinter.set_appearance_mode("system")

customtkinter.set_default_color_theme("assets\YouTube Video Downloader CustomTkinter theme.json")

app = customtkinter.CTk()

app.geometry("480x480")

app.iconbitmap(bitmap=appIcon)

app.title("YouTube Video Downloader")

app.resizable(width=False, height=False)


enterLabel = customtkinter.CTkLabel(master=app, width=500, text="Enter YouTube Link")
enterLabel.pack()

urlVar = tkinter.StringVar()
link = customtkinter.CTkEntry(master=app, width=400, height=50, textvariable=urlVar)
link.pack()

def downloader():
    try:
        tubeLink = link.get()
        tubeObject = YouTube(tubeLink, on_progress_callback=progress)
  
        video = tubeObject.streams.get_highest_resolution()
        finishLabel.configure(text="")
        video.download()
    except:
        finishLabel.configure(text="Download failed!")


def progress(stream, chunk, bytes_left):
    tSize = stream.filesize
    bytes_downloaded = tSize - bytes_left
    percentage = bytes_downloaded / tSize * 100
    per = str(int(percentage))
    percentageUI.configure(text=per + '%')
    percentageUI.update()

    progressBar.set(float(percentage) / 100)

    if per == "100":
        finishLabel.configure(text="Download Complete!")


percentageUI = customtkinter.CTkLabel(master=app, text="0%")
percentageUI.pack()

progressBar = customtkinter.CTkProgressBar(master=app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

finishLabel = customtkinter.CTkLabel(master=app, text="")
finishLabel.pack()

downloadButton = customtkinter.CTkButton(master=app, text="Download", command=downloader)
downloadButton.pack()

def quality_format_ComboBox_Callback(choice):
    return


quality_format_ComboBox = customtkinter.CTkComboBox(master=app, values=["Test 1", "Test 2"], command=quality_format_ComboBox_Callback)
quality_format_ComboBox.pack()

# can't for the life of me figure out how to force the window into focus.
# same issue that's causing the focusing issue seems to be causing the icon to not appear on the about window.
# Possible fix: https://stackoverflow.com/questions/76687351/customtkinter-entry-not-getting-focus
def about():
    about = customtkinter.CTkToplevel()
    about.geometry("280x280")
    about.iconbitmap(bitmap=appIcon)
    about.title("About")
    about.focus_force()
    aboutTitleLabel = customtkinter.CTkLabel(master=about, text="YouTube Video Downloader")
    aboutTitleLabel.pack()
    appVersionLabel = customtkinter.CTkLabel(master=about, text=appVersion)
    appVersionLabel.pack()
    developerLabel = customtkinter.CTkLabel(master=about, text="Developer: magnetProgramming")
    developerLabel.pack()

aboutButton = customtkinter.CTkButton(master=app, text="About", command=about)
aboutButton.pack(padx=10, pady=10)





app.mainloop()