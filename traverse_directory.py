import os
from os import listdir
from os.path import isfile, isdir, join
from collections import namedtuple

# Создаем именованный кортеж - запись в  results
MyInfo = namedtuple('info', 'name ext is_directory parent_directory')

class Traverse_directory:
    def __init__(self):
        self.results: MyInfo = []

    def run(self, parent_path):
        list_files = [f for f in listdir(parent_path) if isfile(join(parent_path, f))]
        list_dirs = [f for f in listdir(parent_path) if isdir(join(parent_path, f))]
        for f in list_files:
            localpath = os.path.join(parent_path, f)
            filename, ext = os.path.splitext(localpath)            
            self.results.append(MyInfo(filename, ext, False, parent_path))
        for d in list_dirs: 
            self.results.append(MyInfo(d, None, True, parent_path))
            self.run(join(parent_path, d))  