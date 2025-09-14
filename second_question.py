def get_line(x1, y1, x2, y2):

    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return points


def count_unique_cells(points_list):

    unique_points = set()
    for points in points_list:
        unique_points.update(points)
    return len(unique_points)


def main():
    # Input: List of points
    points = [] # put your input here

    all_paths = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        path = get_line(x1, y1, x2, y2)
        all_paths.append(path)

    # Count the unique cells
    result = count_unique_cells(all_paths)

    # Output the result
    print(result)


if __name__ == "__main__":
    main()
