#!/usr/bin/python

import StringIO
import zipfile
import sys
import os

if len(sys.argv) != 2:
    print "Usage: extension_extractor.py TARGET_DIR_PATH"
    exit(1)

path = sys.argv[1]
if not os.path.isdir(path):
    print "Error: Your target path is not a directory"
    exit(2)
    # TODO: make it also work on single files (eg. signle zip file)

extensions = set()
os.chdir(path)

for filename in os.listdir('.'):
    if filename.lower().endswith('/'):
        continue
    elif filename.lower().endswith('.zip'):
        with open(filename, "rb") as zip_file:
            try:
                unzipped = zipfile.ZipFile(zip_file)
                for item_name in unzipped.namelist():
                    if not item_name.endswith('/'):
                        file_name, file_extension = os.path.splitext(item_name)
                        # file_name = item_name.split('/')[-1]
                        # print file_name
                        extensions.add(file_extension)
            except zipfile.BadZipfile:
                pass  # corrupt zip file
    else:
        file_name, file_extension = os.path.splitext(filename)
        extensions.add(file_extension)

for extension in sorted(extensions):
    print extension
