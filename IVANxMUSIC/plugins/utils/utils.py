import logging
from urllib.parse import urlparse
import yt_dlp

# ✅ Logger helper
def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(levelname)s] %(name)s: %(message)s')
    handler.setFormatter(formatter)
    if not logger.hasHandlers():  # avoid duplicate logs
        logger.addHandler(handler)
    return logger

# ✅ Convert seconds to mm:ss
def seconds_to_min_sec(seconds: int) -> str:
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes}:{secs:02d}"

# ✅ Check if string is a URL
def is_url(string: str) -> bool:
    try:
        result = urlparse(string)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# ✅ Get audio info without downloading (using yt-dlp)
def get_audio_info(url: str):
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                'title': info.get('title'),
                'duration': info.get('duration'),
                'uploader': info.get('uploader'),
                'webpage_url': info.get('webpage_url')
            }
    except Exception as e:
        return {'error': str(e)}

# ✅ Format song info nicely
def format_song_info(title: str, duration: int):
    return f"🎶 **{title}**\n⏱ Duration: `{seconds_to_min_sec(duration)}`"

# ✅ Download audio (optional)
def download_audio(url: str, output_path: str = "downloads/") -> str:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}%(id)s.%(ext)s',
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)
