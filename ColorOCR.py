from scipy.spatial import KDTree
import webcolors


# y = yellow, o = orange (so brown basically), g = green, b = blue, r = red, t = mountain green, cyan is spawn?
colors = {'#8d7741': 'y', '#825148': 'o', '#407450': 'g', '#41698a': 'b', '#a95c61': 'r',
          '#426a38': 't'} # , '#033e4e': 'cyan'}
# This looks at a sampled pixel color and returns the value that is the nearest to the given color codes in the dict
# Basically it chooses the key that is closest to the sampled color and returns its value
# This has the highest need for optimization. Too few sampled colors leads to some points being classified as the wrong
# color, which is bad
def rgb_to_color(rgb_tuple):
    # I thing I used this for debugging:
    # colors = {'#8d7741': 'yellow', '#825148': 'orange', '#407450': 'green',
    # '#41698a': 'blue', '#a95c61': 'red', '#426a38': 't'}

    names = []
    rgb_values = []
    for color_hex, color_name in colors.items():
        names.append(color_name)
        rgb_values.append(webcolors.hex_to_rgb(color_hex))

    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index]
