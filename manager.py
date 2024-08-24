""" Module for Controlling the Junctions and Exporting the Books """

import sys
import os
import json
import shutil
import glob

def delete_junctions(directory_: str):
    """ delete all custom subdir """
    delete_path = os.path.join(directory_, "*/")
    for dirs in glob.glob(delete_path):
        if "src" in dirs:
            continue
        try:
            os.unlink(dirs[:-1])
        except PermissionError:
            shutil.rmtree(dirs[:-1])

def reset_js(data_: dict, command_: str = "serve", js: str = "./src/data.js"):
    """ overwrite the JS data file """
    # perform deep copy here
    temp = {book_code_: val.copy() for book_code_, val in data_.items()}
    if command_ == "export":
        for book_code_ in temp:
            temp[book_code_]["path"] = "./" + book_code_
    with open(js, "w", encoding = "utf-8") as file:
        file.write("var data = " + json.dumps(temp, indent = 4) + ";")

def clear_setting(command_:str = "serve", input_dir: str = "./src/data.json",
                  setup_dir: str = "./") -> dict:
    """ clear the setup and return the data """
    with open(input_dir, "r", encoding = "utf-8") as file:
        data_ = json.load(file)
    reset_js(data_, command_)
    delete_junctions(setup_dir)
    return data_

def serve(book_dir: str, link_dir_: str = "./"):
    """ Soft copying all books by junctions and ready to serve """
    os.system(f"mklink /J \"{link_dir_}\" \"{book_dir}\"")

def export(book_dir: str, link_dir_: str):
    """ Hard copying all books and ready to export """
    shutil.copytree(book_dir, link_dir_)

if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1].lower() not in ["serve", "export", "clear"]:
        print("Correct usage: manager.py [serve / export / clear]")
        sys.exit()
    command = sys.argv[1].lower()
    data = clear_setting(command)
    if command == "clear":
        sys.exit()
    i = 0
    for book_code, vals in data.items():
        link_dir = os.path.join("./", book_code)
        if command == "serve":
            serve(vals["path"], link_dir)
        else:
            export(vals["path"], link_dir)
        if not os.path.exists(f"{book_code}/cover.png"):
            shutil.copy2("src/cover.png", f"{book_code}/cover.png")
        i += 1
        print(f"Created {i}/{len(data)} links for {book_code}", end = "\t\t\r")
    print()
