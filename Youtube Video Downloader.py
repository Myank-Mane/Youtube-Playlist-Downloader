import os
import yt_dlp


def download_video_as_mp3(video_url, output_folder):
    """Downloads an individual YouTube video of any length as an MP3 file."""
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # yt-dlp configuration options
    ydl_opts = {
        # Select best audio quality
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        # Save template: Saves inside target folder with video title
        "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),
        # Ensures single video downloading even if a playlist parameter is in the URL
        "noplaylist": True,
        "ignoreerrors": True,
    }

    print(f"Starting download for: {video_url}")
    print(f"Saving file to: {output_folder}/\n")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    print("\nDownload completed!")


if __name__ == "__main__":
    # --- SETUP YOUR VARIABLES HERE ---

    # Replace this with your actual YouTube video URL
    TARGET_VIDEO_URL = "https://youtu.be/sBn2B9hnjw8?si=eDzSsucDiXTJ4Wmn"

    # The folder where you want to save the MP3 file
    TARGET_FOLDER = "My_Downloaded_Video"

    # Run the function
    download_video_as_mp3(TARGET_VIDEO_URL, TARGET_FOLDER)