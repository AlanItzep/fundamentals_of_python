# Automation of Repetitive Tasks (File Renaming)

import os

def build_new_name(index, digits, extension):
    number_str = str(index)
    while len(number_str) < digits:
        number_str = "0" + number_str
    return "img" + number_str + extension

def rename_file(folder, original_name, new_name):
    old_path = os.path.join(folder, original_name)
    new_path = os.path.join(folder, new_name)
    try:
        os.rename(old_path, new_path)
        print("Renamed:", original_name, "->", new_name)
    except:
        print("Failed to rename:", original_name)

def rename_images(digits=3):
    folder = "."
    files = os.listdir(folder)

    index = 1
    i = 0
    total = len(files)

    while i < total:
        filename = str(files[i])
        extension = ""
        name_length = len(filename)

        if name_length >= 4:
            ext_part = filename[-4:]
            if ext_part == ".jpg" or ext_part == ".png":
                extension = ext_part

        if extension != "":
            newname = build_new_name(index, digits, extension)
            rename_file(folder, filename, newname)
            index = index + 1

        i = i + 1

rename_images()
