# Snail Sort

# Given an n x n array, return the array elements arranged
# from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]

# Important to use reversed rather than .reverse to return the list/iterator.

def path(array):
    route = list.copy(array[0])
    n = len(array)
    for i in range(1, n - 1):
        route += [array[i][-1]]
    route += reversed(array[-1])
    for i in reversed(range(1, n - 1)):
        route += [array[i][0]]
    return route


def snail(snail_map):
    if len(snail_map) == 2:
        return snail_map[0] + list(reversed(snail_map[1]))
    if len(snail_map) == 1:
        return snail_map[0]
    else:
        current_route = path(snail_map)
        new_snail_map = snail_map[1 : -1]
        for i in range(len(new_snail_map)):
            new_snail_map[i].pop(-1)
        for i in range(len(new_snail_map)):
            new_snail_map[i].pop(0)

        return current_route + snail(new_snail_map)
