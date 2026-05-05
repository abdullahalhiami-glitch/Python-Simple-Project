import yt_dlp

def download_video(url):
    # إعدادات بسيطة لتحميل أفضل جودة متوفرة
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s' # حفظ الملف باسمه الأصلي
    }
    
    print("جاري التحميل، يرجى الانتظار...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("تم تحميل الفيديو بنجاح!")
    except Exception as e:
        print(f"حدث خطأ أثناء التحميل: {e}")

# تجربة البرنامج
video_url = input("أدخل رابط فيديو يوتيوب: ")
download_video(video_url)

#https://youtube.com/shorts/zaBDyEfhrnk?si=QPXb5JxWHDjbENdx