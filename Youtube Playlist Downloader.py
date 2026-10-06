import os
import yt_dlp


def download_playlist_as_mp3(playlist_url, output_folder):
    """
    Downloads all videos from a YouTube playlist and converts them to MP3.
    """
    # Create the output folder if it doesn't already exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created directory: {output_folder}")

    # Configuration options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Choose the best audio format available
        'extract_audio': True,  # Only extract audio
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Output path and filename
        'ignoreerrors': True,  # Skip videos that cause errors (e.g., deleted videos)
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convert to mp3
            'preferredquality': '192',  # Set quality to 192 kbps
        }],
    }

    print(f"Fetching playlist: {playlist_url}")

    # Execute the download
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print("\nAll available songs have been successfully downloaded!")
    except Exception as e:
        print(f"\nAn error occurred during the download process: {e}")


if __name__ == "__main__":
    # --- SETUP YOUR VARIABLES HERE ---

    # Replace this with your actual YouTube playlist URL
    TARGET_PLAYLIST_URL = 'https://youtube.com/playlist?list=PLtV8HCyrxUzl978fv2CejMNKj8gdxvKAi&si=hUpm8YqTpKT4T8Ke'

    # The folder where you want to save the MP3 files
    TARGET_FOLDER = 'My_Downloaded_Playlist'

    # Run the function
    download_playlist_as_mp3(TARGET_PLAYLIST_URL, TARGET_FOLDER)