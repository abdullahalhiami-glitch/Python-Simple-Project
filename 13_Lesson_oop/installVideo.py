import yt_dlp

def download_video(url):
    # Simple settings for downloading the best quality of the video
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s' # Save the file or video with its original name
    }
    
    print("Please wait while downloading your video....")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video Was Downloaded Successfully.")
    except Exception as e:
        print(f"Couldn't download the video and the error is: {e}")

# Trying the program
video_url = input("Enter the YouTub Link Here To Download The Video: ")
download_video(video_url)

#https://youtube.com/shorts/zaBDyEfhrnk?si=QPXb5JxWHDjbENdx