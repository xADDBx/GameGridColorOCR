import numpy as np
import matplotlib.pyplot as plt


def find_path(choice, mapping, start, stop):
    fig, ax = plt.subplots(figsize=(10, 10))
    min_val, max_val = 0, 20
    grid = mapping.copy()

    if choice == 'e':
        costs = {'b': 0, 'r': 1, 'y': 1, 'g': 2, 'o': 1, 't': 200}
    elif choice == 'wa':
        costs = {'b': 1, 'r': 0, 'y': 1, 'g': 1, 'o': 2, 't': 200}
    elif choice == 'f':
        costs = {'b': 2, 'r': 1, 'y': 0, 'g': 1, 'o': 1, 't': 200}
    elif choice == 'g':
        costs = {'b': 1, 'r': 2, 'y': 1, 'g': 0, 'o': 1, 't': 200}
    elif choice == 'wo':
        costs = {'b': 1, 'r': 1, 'y': 2, 'g': 1, 'o': 0, 't': 200}
    else:
        costs = {}

    for i in range(20):
        for j in range(20):
            grid[i][j] = costs[grid[i][j]]

    grid = grid.astype(int)

    current_cmap = plt.cm.get_cmap("Blues").copy()
    current_cmap.set_bad(color='red')
    ax.matshow(grid, cmap=plt.cm.Blues, vmin=0, vmax=4)

    # Initialize auxiliary arrays
    distmap = np.ones((max_val, max_val), dtype=int) * np.Infinity
    distmap[start[0], start[1]] = 0
    originmap = np.ones((max_val, max_val), dtype='2i') * np.nan
    visited = np.zeros((max_val, max_val), dtype=bool)
    finished = False
    x, y = start
    count = 0

    # Loop Dijkstra until reaching the target cell
    while not finished:
        # move to x+1,y
        if x < max(start[0], stop[0]):
            if distmap[x + 1, y] > grid[x + 1, y] + distmap[x, y] and not visited[x + 1, y]:
                distmap[x + 1, y] = grid[x + 1, y] + distmap[x, y]
                originmap[x + 1, y] = (x, y)
        # move to x-1,y
        if x > min(start[0], stop[0]):
            if distmap[x - 1, y] > grid[x - 1, y] + distmap[x, y] and not visited[x - 1, y]:
                distmap[x - 1, y] = grid[x - 1, y] + distmap[x, y]
                originmap[x - 1, y] = (x, y)
        # move to x,y+1
        if y < max(start[1], stop[1]):
            if distmap[x, y + 1] > grid[x, y + 1] + distmap[x, y] and not visited[x, y + 1]:
                distmap[x, y + 1] = grid[x, y + 1] + distmap[x, y]
                originmap[x, y + 1] = (x, y)
        # move to x,y-1
        if y > min(start[1], stop[1]):
            if distmap[x, y - 1] > grid[x, y - 1] + distmap[x, y] and not visited[x, y - 1]:
                distmap[x, y - 1] = grid[x, y - 1] + distmap[x, y]
                originmap[x, y - 1] = (x, y)

        visited[x, y] = True
        dismaptemp = distmap
        dismaptemp[np.where(visited)] = np.Infinity
        # now we find the shortest path so far
        minpost = np.unravel_index(np.argmin(dismaptemp), np.shape(dismaptemp))
        x, y = minpost[0], minpost[1]
        if x == stop[0] and y == stop[1]:
            finished = True
        count = count + 1

    # Start backtracking to plot the path
    mattemp = grid.astype(float)
    x, y = stop
    path = []
    mattemp[int(x), int(y)] = np.nan
    cond1 = cond2 = True
    while cond1 or cond2:
        path.append([int(x), int(y)])
        x, y = originmap[int(x), int(y)]
        mattemp[int(x), int(y)] = np.nan
        if start[0] < stop[0]:
            cond1 = x > start[0]
        else:
            cond1 = x < start[0]
        if start[1] < stop[1]:
            cond2 = y > start[1]
        else:
            cond2 = y < start[1]

    path.append([int(x), int(y)])

    # Output and visualization of the path
    current_cmap = plt.cm.get_cmap("Blues").copy()
    current_cmap.set_bad(color='red')
    fig2, ax = plt.subplots(figsize=(8, 8))
    ax.matshow(mattemp, cmap=current_cmap, vmin=0, vmax=20)
    for i in range(max_val):
        for j in range(max_val):
            c = grid[j, i]
            ax.text(i, j, str(c), va='center', ha='center')

    return fig, fig2, distmap[stop[0], stop[1]]
