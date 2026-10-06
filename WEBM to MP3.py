import os
import subprocess


def convert_folder_webm_to_mp3(folder_path):
    """
    Finds all .webm files in a folder and converts them to .mp3.
    Uses a local ffmpeg binary if present in the script's directory.
    """
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # Check if ffmpeg.exe is in the current directory
    # If it is, we use the local path. If not, we try the system default.
    ffmpeg_bin = "./ffmpeg.exe" if os.path.exists("ffmpeg.exe") else "ffmpeg"

    files = os.listdir(folder_path)
    webm_files = [f for f in files if f.lower().endswith('.webm')]

    if not webm_files:
        print("No .webm files found in the specified folder.")
        return

    print(f"Found {len(webm_files)} .webm file(s) to convert.\n")

    for index, file_name in enumerate(webm_files, start=1):
        input_path = os.path.join(folder_path, file_name)
        output_file_name = os.path.splitext(file_name)[0] + ".mp3"
        output_path = os.path.join(folder_path, output_file_name)

        print(f"[{index}/{len(webm_files)}] Converting: '{file_name}' -> '{output_file_name}'")

        command = [
            ffmpeg_bin,  # Uses local ffmpeg.exe if you pasted it here
            '-i', input_path,
            '-vn',
            '-ab', '192k',
            '-y',
            output_path
        ]

        try:
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            print(f"❌ Failed to convert: {file_name}")
        except FileNotFoundError:
            print("❌ FFmpeg was still not found. Please ensure 'ffmpeg.exe' is pasted in this folder.")
            return

    print("\n🎉 Conversion process complete!")


if __name__ == "__main__":
    # If the script is in the same folder as your webm songs, leave this as "."
    # Otherwise, provide the full path like: r"C:\Users\YourName\Music"
    TARGET_FOLDER_PATH = r"C:\Users\mayan\OneDrive\Documents\Coding\Projects\Python\Youtube Video Downloader\My_Downloaded_Video"

    convert_folder_webm_to_mp3(TARGET_FOLDER_PATH)