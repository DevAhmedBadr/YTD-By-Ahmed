
from timeit import repeat

import yt_dlp
import os
import colorama

from colorama import Fore, Back, Style

def color_text(text, color):
    return f"{color}{text}{Style.RESET_ALL}"


while True:
    
    logo = r"""
    █   █ █████ ████     ████  █   █     ███  █   █ █   █ █████ ████        ███
     █ █    █   █   █    █   █  █ █     █   █ █   █ ██ ██ █     █   █    █ █   █
      █     █   █   █    ████    █      █████ █████ █ █ █ ████  █   █      █   █
      █     █   █   █    █   █   █      █   █ █   █ █   █ █     █   █    █ █   █
      █     █   ████     ████    █      █   █ █   █ █   █ █████ ████        ███
    """

    print(color_text(logo, Fore.RED))

    url = input(color_text("Enter the YouTube video URL: ", Fore.CYAN))
    url = url.strip()
    save_path = input(color_text("Enter the path to save the video (default is 'downloads'): ", Fore.CYAN))
    print(color_text("Available video qualities: \n1-Best\n2-720p\n3-480p\n4-Worst", Fore.YELLOW))
    choose_video_quality = input(color_text("Choose video quality 1/2/3/4: ", Fore.CYAN)).strip().lower()


    if not save_path:
        save_path = "downloads"


    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'format': 'bestvideo*+bestaudio/best'
    }


    if not url:
        print("No URL provided.")
        exit()






    if url.startswith("https://www.youtube.com/") or url.startswith("https://youtu.be/"):
        print(color_text("Valid YouTube URL.", Fore.GREEN))

        if choose_video_quality == "1":
            ydl_opts['format'] = 'bestvideo+bestaudio'
        elif choose_video_quality == "2":
            ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best[height<=720]'
        elif choose_video_quality == "3":
            ydl_opts['format'] = 'bestvideo[height<=480]+bestaudio/best[height<=480]'
        elif choose_video_quality == "4":
            ydl_opts['format'] = 'worstvideo+worstaudio/worst'
        else:
            print(color_text("Invalid video quality choice. Defaulting to best quality.", Fore.YELLOW))
            ydl_opts['format'] = 'bestvideo+bestaudio'

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(color_text("Download completed successfully.", Fore.GREEN))

        repeat_process = input(color_text("Do u wanna download another video? (Y/N)", Fore.CYAN)).strip().upper()
        if repeat_process == "N":
            print(Back.RED + color_text("Thank you for using YTD By Ahmed :)", Fore.CYAN))
            break
        elif repeat_process == "Y":
            os.system("cls")
                


    else:
        print(color_text("Invalid YouTube URL. Please provide a valid YouTube video link.", Fore.RED))
        exit()






