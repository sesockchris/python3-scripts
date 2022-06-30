import os
from os import rename, listdir

directory = input("Directory containing files to rename: ")
to_be_named = os.listdir(path = directory)

for i in range(0, len(to_be_named)):
    os.rename(to_be_named[i], str(i + 1))

