import yt_dlp

try:
    url = input("Enter the YouTube URL: ")
    
    ydl_opts = {
        'outtmpl': '/Users/rimen/OneDrive/Desktop/Users/rimen/Desktop/%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print("Download complete.")

except Exception as e:
    print("An error occurred:", str(e))
