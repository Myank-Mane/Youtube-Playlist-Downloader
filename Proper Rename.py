import os
import re


def clean_and_rename_mp3s(folder_path, capitalization_style="sentence"):
    """
    Renames all MP3 files in a folder with numbering (e.g., "01. Song name"),
    clean text, and formatting.
    """
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # Get all files and filter for .mp3
    files = os.listdir(folder_path)
    mp3_files = [f for f in files if f.lower().endswith('.mp3')]

    if not mp3_files:
        print("No .mp3 files found in the folder to rename.")
        return

    # Sort files alphabetically so the numbering follows a logical order
    mp3_files.sort()

    print(f"Found {len(mp3_files)} MP3 file(s) to clean and rename.\n")

    # Determine padding for numbers (e.g., '01', '02')
    padding = len(str(len(mp3_files)))
    if padding < 2:
        padding = 2

    for index, file_name in enumerate(mp3_files, start=1):
        # Extract the song name without the extension
        song_title, ext = os.path.splitext(file_name)

        # 1. Remove symbols and special characters (Keep only letters, numbers, and spaces)
        clean_title = re.sub(re.compile(r'[^a-zA-Z0-9\s]'), ' ', song_title)

        # Collapse multiple spaces into a single space and strip edges
        clean_title = ' '.join(clean_title.split())

        # 2. Handle Capitalization
        if capitalization_style == "title":
            clean_title = clean_title.title()
        else:
            clean_title = clean_title.capitalize()

        # 3. Add the sequential numbering prefix with a DOT and a SPACE (e.g., "01. ")
        number_prefix = f"{str(index).zfill(padding)}. "
        new_file_name = f"{number_prefix}{clean_title}{ext}"

        # Setup full paths
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        try:
            os.rename(old_path, new_path)
            print(f"✅ Renamed: '{file_name}' \n        -> '{new_file_name}'")
        except Exception as e:
            print(f"❌ Could not rename '{file_name}': {e}")

    print("\n🎉 All audio files have been neatly organized and renamed!")


if __name__ == "__main__":
    TARGET_FOLDER_PATH = r"C:\Users\mayan\OneDrive\Documents\Songs\Hindi Old Songs"
    STYLE = "sentence"  # Options: "sentence" or "title"

    clean_and_rename_mp3s(TARGET_FOLDER_PATH, capitalization_style=STYLE)