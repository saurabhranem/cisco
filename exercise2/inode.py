import os
path = os.getcwd()

print("Directory entry name and their inode number")
with os.scandir(path) as itr:
    for entry in itr:
        print(entry.name, ":", entry.inode())

