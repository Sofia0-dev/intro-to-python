import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }
    ],
}


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
  ydl.download(['https://www.youtube.com/watch?v=QbS9QW0IHzU&list=RDQbS9QW0IHzU&start_radio=1'])


#ffmpeg windows
#justpaste.it/iq3it
#windows
#winget install --id Gyan.FFmpeg -e
#'ffmpeg_location' : r'C:\ffmpeg\bin',


