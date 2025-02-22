# thumbnail_downloader.py
import yt_dlp
import os
import requests

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

def download_thumbnails():
    for idx, url in enumerate(video_urls, 1):
        output_template = os.path.join(output_dir, f'chocolate{idx}Thumbnail.jpg')
        
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True
        }
        
        try:
            # First get video info to extract the video ID
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"\nGetting info for thumbnail {idx}...")
                info = ydl.extract_info(url, download=False)
                video_id = info['id']
                
                # Try to download maxresdefault first
                thumbnail_url = f'https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg'
                response = requests.get(thumbnail_url)
                
                # If maxresdefault is not available, fall back to hqdefault
                if response.status_code != 200:
                    thumbnail_url = f'https://i.ytimg.com/vi/{video_id}/hqdefault.jpg'
                    response = requests.get(thumbnail_url)
                
                # Save the thumbnail
                if response.status_code == 200:
                    with open(output_template, 'wb') as f:
                        f.write(response.content)
                    print(f"Successfully downloaded high quality chocolate{idx}Thumbnail.jpg")
                else:
                    print(f"Failed to download thumbnail {idx}")
                    
        except Exception as e:
            print(f"Error downloading thumbnail {idx}: {str(e)}")

if __name__ == "__main__":
    download_thumbnails()
