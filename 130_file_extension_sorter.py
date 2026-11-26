"""
Project 130: File Extension Sorter (Directory Organizer)
Concepts: os module, path manipulation, dictionary grouping, file organization logic.
"""
import os
import shutil

CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh"]
}

def simulate_categorization(filenames):
    organized = {cat: [] for cat in CATEGORIES}
    organized["Other"] = []

    for name in filenames:
        ext = os.path.splitext(name)[1].lower()
        matched = False
        for cat, ext_list in CATEGORIES.items():
            if ext in ext_list:
                organized[cat].append(name)
                matched = True
                break
        if not matched:
            organized["Other"].append(name)

    return organized

def main():
    print("=== FILE EXTENSION ORGANIZER SIMULATOR ===")
    sample_files = [
        "report.pdf", "vacation.jpg", "music_track.mp3", "data.csv",
        "archive.zip", "test_script.py", "presentation.pptx", "avatar.png",
        "notes.txt", "unknown_blob.xyz"
    ]

    print("Sample batch of files to organize:")
    print(", ".join(sample_files))

    results = simulate_categorization(sample_files)
    print("\n--- Sorter Results by Folder ---")
    for cat, files in results.items():
        if files:
            print(f"[FOLDER] [{cat}/]:")
            for f in files:
                print(f"   └── {f}")

if __name__ == "__main__":
    main()
