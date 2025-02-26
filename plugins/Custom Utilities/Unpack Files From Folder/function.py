import os
import shutil


def driver(items: list[str] = [], params: dict = {}):
    for folder in items:
        for file in os.listdir(folder):
            print("Unpacking: ", file)
            shutil.move(os.path.join(folder, file), os.path.join(os.path.dirname(folder), file))
            os.rmdir(folder)
