'''
Task 2

1- Write a module (files.py) which is responsible for managing the file content.
2- Create a class (TextFile) with the methods below:

    - read(file_path)
    - write(content)
    - remove(file_path)
    - is_empty()
    - is_exists()
'''
from os import path


class TextFile:

    def __init__(self, filepath):

        if filepath is None or filepath == "":
            raise ValueError
        self.f_path = filepath

    def read(self):
        with open(self.f_path) as f:
            file_lines = f.readlines()
        return file_lines

'''
    def write(self, content):
        with open(self.filepath) as f:
            content = f.write()
        return "File written"

    def is_empty(self):
        pass

    def is_exists(self):
        if path.exists(self.filepath):
            return True
        return False
'''