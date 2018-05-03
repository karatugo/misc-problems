import sys

# https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain
def get_convex_hull(vertices):
# It does so by first sorting the points lexicographically (first by x-coordinate, and in case of a tie, by y-coordinate), and then constructing upper and lower hulls of the points in O(n) time.
# An upper hull is the part of the convex hull, which is visible from the above. It runs from its rightmost point to the leftmost point in counterclockwise order. Lower hull is the remaining part of the convex hull.
    def cross_product(o, a, b):
        x = a[0]
        y = a[1]

        p = o[0]
        q = o[1]

        w = b[0]
        z = b[1]

        return (x - p) * (z - q) - (y - q) * (w - p)

    vertices = sorted(set(vertices))
    if len(vertices) <= 1:
        return vertices

    lower_hull = []
    for v in vertices:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], v) <= 0:
            lower_hull.pop()
        lower_hull.append(v)

    upper_hull = []
    for v in reversed(vertices):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], v) <= 0:
            upper_hull.pop()
        upper_hull.append(v)

    return lower_hull[:-1] + upper_hull[:-1]

def adjacent_vertices(vertices):
    # match the vertex with the next one
    # e.g.
    # vertices :
    # [(6, 39), (11, 19), (18, 13), (31, 3), (31, 17), (28, 25)]
    #
    # vertices[1:] + [vertices[0]]:
    # [(11, 19), (18, 13), (31, 3), (31, 17), (28, 25), (6, 39)]
    #
    # zipped:
    # [((6, 39), (11, 19)), ((11, 19), (18, 13)), ((18, 13), (31, 3)), ((31, 3), (31, 17)), ((31, 17), (28, 25)), ((28, 25), (6, 39))]
    return zip(vertices, vertices[1:] + [vertices[0]])


# https://stackoverflow.com/questions/451426/how-do-i-calculate-the-area-of-a-2d-polygon
def area(vertices):
    areas_of_paralelograms = (a*d - c*b for ((a, b), (c, d)) in adjacent_vertices(vertices))
    # we divide by 2 because area of each paralelogram is summed twice
    return abs(sum(areas_of_paralelograms)) / 2.0

def get_inputs(inputs):
    vertices = []
    for line in inputs[1:]:
        xy = line.split()
        vertices.append((int(xy[0]), int(xy[1])))

    print area(get_convex_hull(vertices))

# inputs = ["5","0 0", "10 10", "0 10", "10 0","5 5",
# "10","6 39","28 25", "28 13", "31 3", "11 19", "31 17", "26 19","18 13","30 11","25 20",
# "0"
# ]

inputs = sys.stdin.readlines()
number_of_vertices = int(inputs[0])
n = 0
while number_of_vertices > 0:
    get_inputs(inputs[n : number_of_vertices + n + 1])
    n += number_of_vertices + 1
    number_of_vertices = int(inputs[n])
