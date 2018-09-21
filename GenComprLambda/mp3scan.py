#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 28, 2018 9:11:41 AM$"

import os, fnmatch
import id3reader_p3 as id3reader

def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, "*.{}".format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)

root = "/Users/tom/Music/iTunes/iTunes Music/"

for f in find_music(root, 'mp3'):
    id3r = id3reader.Reader(f)
    print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
        id3r.get_value('performer'),
        id3r.get_value('album'),
        id3r.get_value('track'),
        id3r.get_value('title')
    ))
