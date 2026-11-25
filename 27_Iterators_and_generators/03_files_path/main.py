# TODO здесь писать код
import os
def walk_tree(path):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            yield root, files
direct = os.path.abspath('/Games')
def gen_files_path(find):
    for root, files in walk_tree(direct):
        print(os.path.normpath(root))
        if os.path.samefile(str(root),str(find)):
            print("Folder is finded")
            break
        for file in files:
            print(os.path.join(root,file))
find = os.path.join(direct,'Jump Force/Engine')
gen_files_path(find)