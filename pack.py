#!/usr/bin/python3
import sys
import os
import zipfile
import fnmatch


def is_included(path, exclude_patterns):
    for p in exclude_patterns:
        if fnmatch.fnmatch(path, p):
            return False
    return True

def scan(path, exclude_patterns):
    entries = []
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and is_included(entry.path, exclude_patterns):
                if entry.is_file():
                    entries.append(entry.path)
                    print(entry.path)
                if entry.is_dir():
                    entries = entries + scan(entry.path, exclude_patterns)
    return entries


def zip_files(zipfile_name, arc_prepend, files):
    f = zipfile.ZipFile(zipfile_name, 'w', zipfile.ZIP_DEFLATED)  
    for file in files:
        f.write(file, os.path.join(arc_prepend, file))
    f.close()

exclude_patterns = sys.argv[1].split()

print(f"exclude: {exclude_patterns}")

files = scan(".", exclude_patterns)
zip_files("/tmp/my.zip", "", files)



