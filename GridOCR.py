from PIL import Image, ImageChops
from ColorOCR import rgb_to_color
import numpy as np


def trim(img):
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return img.crop(bbox)


def color(point, img, color):
    x, y = point
    for i in range(-2, 3):
        for j in range(-2, 3):
            from webcolors import hex_to_rgb as htr
            img.putpixel((x + i, y + j), htr(color))


def check_grid(x, y, img):
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
            c = rgb_to_color(img.getpixel((tmp_x, tmp_y)))
            # pts[img.getpixel((tmp_x, tmp_y))] = img.getpixel((tmp_x, tmp_y))
            t = rgb_to_color(img.getpixel((tx, ty)))
            if t == 't':
                colors.append(t)
            else:
                colors.append(c)
            colorst = {'#8d7741': 'y', '#825148': 'o', '#407450': 'g', '#41698a': 'b', '#a95c61': 'r', '#426a38': 't', '#033e4e': 'cyan'}
            color((tmp_x, tmp_y), img, list(colorst.keys())[list(colorst.values()).index(c)])
            color((tx, ty), img, list(colorst.keys())[list(colorst.values()).index(t)])
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