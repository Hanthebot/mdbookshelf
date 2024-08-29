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
        if "src" in dirs or "covers" in dirs:
            continue
        try:
            os.unlink(dirs[:-1])
        except PermissionError:
            shutil.rmtree(dirs[:-1])
    for dirs in glob.glob(os.path.join(directory_, "covers/*.png")):
        os.remove(dirs)

def reset_js(data_: dict, command_: str = "serve", js: str = "./src/data.js"):
    """ overwrite the JS data file """
    # perform deep copy here
    temp = data_.copy()
    temp["books"] = {book_code_: val.copy() for book_code_, val in data_["books"].items()}
    if command_ == "export":
        for book_code_ in temp["books"]:
            temp["books"][book_code_]["path"] = "./" + book_code_
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

def serve(book_dir: str, book_code_: str):
    """ Soft copying all books by junctions and ready to serve """
    link_dir_ = os.path.join("./", book_code_)
    cover_path_ = os.path.join(book_dir, "../cover.png")
    os.system(f"mklink /J \"{link_dir_}\" \"{book_dir}\"")
    shutil.copy(cover_path_, f"covers/{book_code_}.png")

def export(book_dir: str, book_code_: str):
    """ Hard copying all books and ready to export """
    link_dir_ = os.path.join("./", book_code_)
    cover_path_ = os.path.join(book_dir, "../cover.png")
    shutil.copytree(book_dir, link_dir_)
    shutil.copy(cover_path_, f"covers/{book_code_}.png")

if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1].lower() not in ["serve", "export", "clear"]:
        print("Correct usage: manager.py [serve / export / clear]")
        sys.exit()
    command = sys.argv[1].lower()
    data = clear_setting(command)
    if command == "clear":
        sys.exit()
    i = 0
    for book_code, vals in data["books"].items():
        cover_dir = os.path.join(vals["path"], "../cover.png")
        if not os.path.exists(cover_dir):
            shutil.copy2("src/cover.png", cover_dir)
        link_dir = os.path.join("./", book_code)
        if command == "serve":
            serve(vals["path"], book_code)
        else:
            export(vals["path"], book_code)
        # if the book is not in dir/cover.png, create one
        # copy it to covers/book_code.png
        i += 1
        print(f"Created {i}/{len(data)} links for {book_code}", end = "\t\t\r")
    print()
