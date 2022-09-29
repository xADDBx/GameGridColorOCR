from scipy.spatial import KDTree
import webcolors


def rgb_to_color(rgb_tuple):
    # colors = {'#8d7741': 'yellow', '#825148': 'orange', '#407450': 'green', '#41698a': 'blue', '#a95c61': 'red', '#426a38': 't'}
    colors = {'#8d7741': 'y', '#825148': 'o', '#407450': 'g', '#41698a': 'b', '#a95c61': 'r',
              '#426a38': 't', '#033e4e': 'cyan'}
    names = []
    rgb_values = []
    for color_hex, color_name in colors.items():
        names.append(color_name)
        rgb_values.append(webcolors.hex_to_rgb(color_hex))

    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index]
