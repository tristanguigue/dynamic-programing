# number of possible paths from (x1, y1) to (x2, y2) moving right or down
# Input: (0, 0, 1, 1)
# Output : 2


def count_paths(x1, y1, x2, y2):
    # invalid path
    if x1 > x2 or y1 > y2:
        return 0

    # we've arrived to destination, add 1 for each leaf
    if x1 == x2 and y1 == y2:
        return 1

    # move right and down
    return count_paths(x1 + 1, y1, x2, y2) + count_paths(x1, y1 + 1, x2, y2)

print count_paths(0, 0, 1, 1)
