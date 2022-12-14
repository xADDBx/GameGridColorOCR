from PIL import Image, ImageChops
import ColorOCR
import numpy as np


# Tries to remove black borders etc. before Color OCR
def trim(img):
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return img.crop(bbox)


# This is for the debug image in which every sampled point will have a large dot showing it's recognized color
def color(point, img, color):
    x, y = point
    for i in range(-2, 3):
        for j in range(-2, 3):
            from webcolors import hex_to_rgb as htr
            img.putpixel((x + i, y + j), htr(color))


# Assuming the grid is 20x20 with all those fields, this function basically goes through every cells and samples 2
# points; one at the upper left to classify elements, one a bit lower left of the center to recognize if it's a mountain
# The recognized Element/Mountain will then be saved in the Grid
def check_grid(x, y, img):
    # This was used to manually select sampled points; found that using percentage based pixels lead to more
    # consistent results
    # def click_event(event, x, y, flags, params):
    # x //= 10
    # y //= 10
    # if event == cv2.EVENT_LBUTTONDOWN:
    dx, dy = img.size
    dx = dx / 20
    dy = dy / 20
    all_colors = np.zeros([20, 20], dtype=np.dtype('U100'))
    for j in range(20):
        colors = []
        for i in range(20):
            tmp_x = int(x + i * dx)
            tmp_y = int(y + j * dy)
            tx = int(tmp_x + 0.01 * img.size[0])
            ty = int(tmp_y + 0.03 * img.size[1])
            c = ColorOCR.rgb_to_color(img.getpixel((tmp_x, tmp_y)))
            # Debugging I think
            # pts[img.getpixel((tmp_x, tmp_y))] = img.getpixel((tmp_x, tmp_y))
            t = ColorOCR.rgb_to_color(img.getpixel((tx, ty)))
            if t == 't':
                colors.append(t)
            else:
                colors.append(c)
            # Those two function calls are, as mentioned, to color the debug map
            color((tmp_x, tmp_y), img, list(ColorOCR.colors.keys())[list(ColorOCR.colors.values()).index(c)])
            color((tx, ty), img, list(ColorOCR.colors.keys())[list(ColorOCR.colors.values()).index(t)])
        all_colors[j] = colors

    img.show()
    return all_colors


def scanGrid(file):
    img = Image.open(file)
    img = trim(img)
    ''' Using self clicked point with zoom
    x_bord = img.size[0]//10
    y_bord = img.size[1]//10
    im = cv2.imread("C:/Users/Christian/Pictures/Fused.jpg")[0:x_bord, 0:y_bord]
    im = cv2.resize(im, None, fx=10, fy=10)
    cv2.imshow('image', im)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

    x_0 = img.size[0] // 180
    y_0 = img.size[1] // 180
    return check_grid(x_0, y_0, img)


# Basically debugging stuff
''' Used to calculate average color for better color recognition
pts = {}
scanGrid("C:/Users/Christian/Pictures/MyPic.jpg")
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')
sav = {'yellow': ((0, 0, 0), 0), 'red': ((0, 0, 0), 0), 'blue': ((0, 0, 0), 0), 'green': ((0, 0, 0), 0), 'orange': ((0, 0, 0), 0)}
for point in pts.values():
    col = rgb_to_color(pts[point])
    s, c = sav[col]
    s = (s[0] + pts[point][0], s[1] + pts[point][1], s[2] + pts[point][2])
    c += 1
    sav[col] = s, c
    ax.scatter(*point, c=col)
for key in sav.keys():
    s, c = sav[key]
    print(f"{key}: {int(s[0]/c)}, {int(s[1]/c)}, {int(s[2]/c)}")
plt.show()
'''
