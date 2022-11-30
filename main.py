import shutil
import uuid

import matplotlib.pyplot as plt
import os
from numpy import inf
from Pathfinder import find_path
from GridOCR import scanGrid
import subprocess

# from stitching import stitch

# Path to Fiji ImageJ installation. Beware that you need the stitches.py script in the scrips subdirectory of Fiji
ImageJ_path = "Fiji.app"
# Directory with the 4 pictures
# 1.PNG is upper left
# 2.PNG is upper right
# 3.PNG is lower left
# 4.PNG is lower right
# Example images are included which should show how the final images have to be cropped
inDir = "Help/"
# Where the resulting path image is saved
outDir = "Help/"
# Name of resulting Image
outFile = "MyPic.jpg"
# Coordinates of Start and Stop,
# (0, 0), (0, 1), ..., (0, y)
# (1, 0), ...
# ...
# (x, 0), (x, 1), ..., (x, y)
start = (0, 0)
stop = (19, 19)
# If you only want to check one element; leave this empty normally
choice = ""
# This is an approximate of the overlap that your images have. The number seems to produce accurate
# stiched images. Should, for whatever reason, the shown stitched image be a mess, try changing this
overlap = "55"

# ImageJ stitching
subprocess.run(f"{os.path.abspath(ImageJ_path)}/ImageJ-win64.exe --ij2 --headless --console --run " +
               f"\"{ImageJ_path}/scripts/stitches.py\" " +
               f"\"inDir='{inDir}',outDir='{outDir + outFile}',overlap='{overlap}'\"", shell=True)
# Python Image stitching, disabled as I had more consistent results with ImageJ
# stitch(inDir, outDir+outFile)

# This does OCR on the stitched image to get grid in which we can search for a path
grid = scanGrid(outDir + outFile)
shortest = (inf, '')

# Basically searches for the shortest path assuming each element once
# The element with the shortest path will be saved in the name variable
if choice == "":
    for choice in ['e', 'wa', 'f', 'g', 'wo']:
        *_, length = find_path(choice, grid, start, stop)
        plt.close(_[0])
        plt.close(_[1])
        toComp, _ = shortest
        if length < toComp:
            shortest = (length, choice)
    _, name = shortest
else:
    name = choice

# Redoing the shortest path to recover it's length; don't know why I'm not carrying over, but not worth
# optimizing since calculating the path is pretty fast compared to stitching and ocr
*_, minimum = find_path(name, grid, start, stop)
print(f"The choice {name} is the shortest with a cost of {int(minimum)}")
plt.show()
# Deleting some files created from the image stitching
if os.path.exists(outDir + "TileConfiguration.registered.txt"):
    os.remove(outDir + "TileConfiguration.registered.txt")
if os.path.exists(outDir + "TileConfiguration.txt"):
    os.remove(outDir + "TileConfiguration.txt")

uniqueName = str(uuid.uuid4())
os.mkdir(outDir + uniqueName)
file_names = [file for file in os.listdir(outDir) if os.path.isfile(os.path.join(outDir, file))]

for file_name in file_names:
    shutil.move(os.path.join(outDir, file_name), outDir + uniqueName)
