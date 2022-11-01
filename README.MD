To run this, you need to have a Python3 Interpreter (I'm unsure of which version is needed, but at least 3.6, just use the newest available Python 3 Version if it doesn't run on yours).

Depends on the following packages:
- OS
- numpy
- matplotlib
- subprocess
- webcolors
- scipy.spatial
- PIL (Pillow)

be sure to have them installed in your Python3 runtime.

How to run:

1) Install Fiji (a derivative of ImageJ)
2) Move stitches.py (NOT stitching.py) into the scripts subdirectory of the Fiji directory
3) Create the Screenshots and Crop + Name them as explained in the main.py
4) Adjust the path to the image files like explained in main.py
5) Adjust coordinates in the main.py to match start and end point
6) run main.py

For more Information read the comments in main.py (I suggest doing that).
There are some inaccuracies, especially with the ColorOCR, so there is some potential to improve that. Shouldn't be too hard either, instead adding more color to recognized tile key value pairs should be good enough.
