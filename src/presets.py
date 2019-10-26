class ConwayPatterns:
    def glider(point):
        x = point[0]
        y = point[1]
        return [(x, y), (x + 1, y), (x + 2, y), (x + 2, y + 1), (x + 1, y + 2)]

    def penta_decathalon(point):
        x = point[0]
        y = point[1]
        return [(x + 1, y + 0), (x + 2, y + 0), (x + 3, y + 0), (x + 0, y + 1), (x + 4, y + 1), (x + 0, y + 2),
                (x + 4, y + 2), (x + 1, y + 3), (x + 2, y + 3), (x + 3, y + 3), (x + 1, y + 8), (x + 2, y + 8),
                (x + 3, y + 8), (x + 0, y + 9), (x + 4, y + 9), (x + 0, y + 10), (x + 4, y + 10), (x + 1, y + 11),
                (x + 2, y + 11), (x + 3, y + 11)]

    def r_pentomino(point):
        x = point[0]
        y = point[1]
        return [(x + 1, y), (x, y + 1), (x + 1, y + 1), (x + 1, y + 2), (x + 2, y + 2)]
