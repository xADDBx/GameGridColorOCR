import cv2


# Python stitching; not used anymore
def stitch(dirPath, outFile):
    images = []
    for i in range(1, 5):
        images.append(cv2.imread(dirPath + f"{i}.jpg"))
    stitcher = cv2.Stitcher_create()
    status, stitched = stitcher.stitch(images)
    cv2.imwrite(outFile, stitched)
