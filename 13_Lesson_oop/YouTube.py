import yt_dlp
import logging
from typing import Optional

# Configure logging (professional alternative to print)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def validate_url(url: str) -> bool:
    """
    Basic validation for YouTube URL.
    """
    return "youtube.com" in url or "youtu.be" in url


def build_options(output_path: str = ".", audio_only: bool = False) -> dict:
    """
    Build yt-dlp configuration options.
    """
    if audio_only:
        return {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        return {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4'
        }


def download_video(url: str, output_path: str = ".", audio_only: bool = False) -> Optional[str]:
    """
    Download video or audio from YouTube.
    
    Args:
        url (str): Video URL
        output_path (str): Folder to save file
        audio_only (bool): If True, download audio only

    Returns:
        Optional[str]: File path if successful, None otherwise
    """
    if not validate_url(url):
        logging.error("Invalid YouTube URL.")
        return None

    options = build_options(output_path, audio_only)

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            logging.info("Starting download...")
            result = ydl.extract_info(url, download=True)

            filename = ydl.prepare_filename(result)
            logging.info(f"Download completed: {filename}")

            return filename

    except yt_dlp.utils.DownloadError as e:
        logging.error(f"Download failed: {e}")

    except Exception as e:
        logging.exception("Unexpected error occurred")

    return None


def main():
    """
    Entry point of the program.
    """
    url = input("Enter YouTube URL: ").strip()
    mode = input("Download audio only? (y/n): ").strip().lower()

    audio_only = mode == 'y'

    result = download_video(url, output_path="downloads", audio_only=audio_only)

    if result:
        logging.info("Process finished successfully.")
    else:
        logging.warning("Process failed.")


if __name__ == "__main__":
    main()