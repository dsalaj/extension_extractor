import StringIO
import zipfile
import sys
import os

if len(sys.argv) != 2:
    exit(1)

extensions = set()
path = sys.argv[1]
for filename in os.listdir(path):
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

for extension in extensions:
    print extension
