# video_downloader.py
import yt_dlp
import os

# List of video URLs
video_urls = [
    "https://youtu.be/EM6jBiC9ZYY",
    "https://youtu.be/W9WDF0hH4ME",
    "https://youtu.be/BGpgEXS3kbA",
    "https://youtu.be/Zk88E4xM5NU",
    "https://youtu.be/h-_4LSy3WCo",
    "https://youtu.be/riaTG4hc4fk",
    "https://youtu.be/PNKWdTiw_BI"
]

# Output directory
output_dir = "/home/sandarva3/Videos/chocolates"

# Create directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

def download_videos():
    for idx, url in enumerate(video_urls, 1):
        output_template = os.path.join(output_dir, f'chocolate{idx}.mp4')
        
        ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            'merge_output_format': 'mp4',
            'outtmpl': output_template,
            'quiet': False,
            'no_warnings': False
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"\nDownloading video {idx}...")
                ydl.download([url])
                print(f"Successfully downloaded chocolate{idx}.mp4")
        except Exception as e:
            print(f"Error downloading video {idx}: {str(e)}")

if __name__ == "__main__":
    download_videos()
