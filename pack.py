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
            if is_included(entry.path, exclude_patterns):
                if entry.is_file():
                    entries.append(entry.path)
                if entry.is_dir():
                    entries = entries + scan(entry.path, exclude_patterns)
    return entries


def zip_files(zipfile_name, arc_prepend, files):
    f = zipfile.ZipFile(zipfile_name, 'w', zipfile.ZIP_DEFLATED)  
    for file in files:
        f.write(file, os.path.join(arc_prepend, file))
    f.close()

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} filename exclude-patterns")
    sys.exit(1)

filename = sys.argv[1]
exclude_patterns = sys.argv[2].split()
exclude_patterns.append('*/.git*')

print(f"exclude-patterns: {exclude_patterns}")

files = scan(".", exclude_patterns)

print(f"Files in {filename}:")
print("\n".join(files))
zip_files(filename, "", files)



