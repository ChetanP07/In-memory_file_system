import os
import json
import re

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}

class FileSystem:
    def __init__(self):
        self.root = Directory('/')
        self.current_dir = self.root

    def mkdir(self, name):
        if name in self.current_dir.children:
            print(f"Directory {name} already exists.")
        else:
            self.current_dir.children[name] = Directory(name, self.current_dir)

    def cd(self, name):
        if name == '..':
            if self.current_dir.parent is not None:
                self.current_dir = self.current_dir.parent
        elif name == '/':
            self.current_dir = self.root
        elif name in self.current_dir.children:
            self.current_dir = self.current_dir.children[name]
        else:
            print(f"No such directory: {name}")

    def ls(self):
        for name in self.current_dir.children:
            print(name)

    def touch(self, name):
        if name in self.current_dir.children:
            print(f"File {name} already exists.")
        else:
            self.current_dir.children[name] = ""

    def cat(self, name):
        if name in self.current_dir.children:
            print(self.current_dir.children[name])
        else:
            print(f"No such file: {name}")

    def echo(self, text, name):
        if name in self.current_dir.children:
            self.current_dir.children[name] = text
        else:
            print(f"No such file: {name}")

    def mv(self, name, new_name):
        if name in self.current_dir.children:
            self.current_dir.children[new_name] = self.current_dir.children.pop(name)
        else:
            print(f"No such file or directory: {name}")

    def cp(self, name, new_name):
        if name in self.current_dir.children:
            self.current_dir.children[new_name] = self.current_dir.children[name]
        else:
            print(f"No such file or directory: {name}")

    def rm(self, name):
        if name in self.current_dir.children:
            del self.current_dir.children[name]
        else:
            print(f"No such file or directory: {name}")

    # def grep(self, pattern, name):
    #     if name in self.current_dir.children:
    #         matches = re.findall(pattern, self.current_dir.children[name])
    #         for match in matches:
    #             print(match)
    #     else:
    #         print(f"No such file: {name}")

    def grep(self, pattern, name):
        if name in self.current_dir.children:
            return re.findall(pattern, self.current_dir.children[name])
        else:
            print(f"No such file: {name}")
            return []


    def save_state(self, path):
        with open(path, 'w') as f:
            json.dump(self.root.children, f)

    def load_state(self, path):
        with open(path, 'r') as f:
            self.root.children = json.load(f)
