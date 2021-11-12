import shutil
from pathlib import Path
import os


class OrganizeFiles:

    def __init__(self):
        self.extentions = None

    def create_folders(self, path):
        self.extentions = set()
        for root, dirs, files in os.walk(path):
            for file in files:
                extention = str(file).split('.')[-1]
                self.extentions.add(extention)
                try:
                    os.mkdir(path + extention)
                except FileExistsError:
                    continue

    def move_files(self, path):
        for root, dirs, files in os.walk(top=path):
            for file in files:
                extention = str(file).split('.')[-1]
                full_path = os.path.join(root, file)
                destiny_path = os.path.join(path + extention)
                if root == path:
                    try:
                        shutil.move(full_path, destiny_path)
                    except:
                        continue


BASE_DIR_DOWNLOAD = str(Path(__file__).parent.parent.parent.parent) + str(os.sep) + 'Downloads' + str(os.sep)
file_obj = OrganizeFiles()
file_obj.create_folders(BASE_DIR_DOWNLOAD)
file_obj.move_files(BASE_DIR_DOWNLOAD)
