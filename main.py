import matplotlib.pyplot as plt
import os
from numpy import inf
from Pathfinder import find_path
from GridOCR import scanGrid
import subprocess

# from stitching import stitch

ImageJ_path = r"C:/Users/Christian/Desktop/Fiji.app"
inDir = "C:/Users/Christian/Pictures/Help2/"
outDir = "C:/Users/Christian/Pictures/Help2/"
outFile = "MyPic.jpg"
start = (19, 0)
stop = (0, 19)
choice = ""
overlap = "55"

# Old Image stitching
subprocess.run(f"{ImageJ_path}/ImageJ-win64.exe --ij2 --headless --console --run " +
               f"\"{ImageJ_path}/scripts/stitches.py\" " +
               f"\"inDir='{inDir}',outDir='{outDir + outFile}',overlap='{overlap}'\"", shell=True)
# Python Image stitching
# stitch(inDir, outDir+outFile)

grid = scanGrid(outDir + outFile)
shortest = (inf, '')
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

*_, minimum = find_path(name, grid, start, stop)
print(f"The choice {name} is the shortest with a cost of {int(minimum)}")
plt.show()
if os.path.exists(outDir + "TileConfiguration.registered.txt"):
    os.remove(outDir + "TileConfiguration.registered.txt")
if os.path.exists(outDir + "TileConfiguration.txt"):
    os.remove(outDir + "TileConfiguration.txt")
if os.path.exists(outDir + outFile):
    os.remove(outDir + outFile)
