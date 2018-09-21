#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 28, 2018 7:51:11 AM$"

import sys
if sys.stdout.encoding == 'US-ASCII':
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import os

root = "/Users/tom/Music/iTunes/iTunes Music/"

#for path, directories, files in os.walk(root, topdown=True):
#    print(path)
#    for d in directories:
#        print("\t{}".format(d))
#    for f in files:
#        fullpath = path + "/" + f
#        print("\t\t{}".format(fullpath))

def find_files_by_extension(extension, dir_root='/'):
    ext_len = len(extension)
    up_ext = extension.upper()
    for path, _, files in os.walk(dir_root, topdown=True):
        for file in files:
            if file[-ext_len:].upper() == up_ext:
                yield "/".join([path, file])
                
for file in find_files_by_extension(extension='.mp3', dir_root=root):
    print(file)