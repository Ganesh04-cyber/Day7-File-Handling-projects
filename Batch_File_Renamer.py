import os

folder_path = "files"
files = os.listdir(folder_path)

count = 1
for filename in files:
    if filename.endswith(".txt"):
        old_path = os.path.join(folder_path, filename)
        new_name = f"renamed_{count}.txt"
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        count += 1

print("Renamed all text files.")
