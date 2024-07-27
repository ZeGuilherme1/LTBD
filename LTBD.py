import yt_dlp
import os
import re

ascii_title = """


                    ██      ████████ ██████  ██████  
                    ██         ██    ██   ██ ██   ██ 
                    ██         ██    ██████  ██   ██ 
                    ██         ██    ██   ██ ██   ██ 
                    ███████    ██    ██████  ██████  
                                 
            Welcome to LibreTube Downloader, a Python study application.
"""

print(ascii_title)

def is_valid_url(url):
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'                                     
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    return youtube_regex.match(url) is not None

def get_valid_url():
    while True:
        url = input("Enter a YouTube video URL: ")
        if is_valid_url(url):
            return url
        else:
            print("Invalid URL! Please enter a valid YouTube URL.")

url = get_valid_url()

def list_formats(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])
        
        print("Available Formats:")
        for i, f in enumerate(formats):
            print(f"{i}: {f['format']} - {f['ext']}")
        return formats

formats = list_formats(url)

format_choice = int(input("> Enter the video format selecting the number option ([4] For example): "))

output_dir = input("Enter the directory to save ([/home/user/folder] For example): ")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

ydl_opts = {
    'format': formats[format_choice]['format_id'], 
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print(" > Successful Download!")
