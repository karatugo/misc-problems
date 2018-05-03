import sys
import math
import itertools
import copy

class Guide:
    def __init__(self, v, x, y):
        self.v = v
        self.x = x
        self.y = y


class Senior:
    def __init__(self, p, q, w, a):
        self.p = p
        self.q = q
        self.w = w
        self.a = a


def get_catch_time(senior, guide, return_times, _):
    alpha = guide.v**2 - senior.w**2
    gamma = (senior.p - guide.x) ** 2 + (senior.q - guide.y) ** 2
    beta = 2 * (senior.p - guide.x) * senior.w * math.cos(senior.a) + 2 * (senior.q - guide.y) * senior.w * math.sin(senior.a)
    t = (beta + math.sqrt(beta ** 2 + 4 * alpha * gamma)) / (2 * alpha)

    p = senior.p + senior.w * math.cos(senior.a) * t
    q = senior.q + senior.w * math.sin(senior.a) * t

    guide.x = p
    guide.y = q

    d = math.sqrt(p**2 + q**2)

    return_times.append(t + _ + d/senior.w)
    return t


def catch_them_all(v, seniors_, shortest_time):
    t = 0
    guide = Guide(v, 0, 0)
    return_times = []
    seniors = copy.deepcopy(seniors_)

    for senior in seniors:
        senior.p = senior.p + senior.w * math.cos(senior.a) * t
        senior.q = senior.q + senior.w * math.sin(senior.a) * t
        t += get_catch_time(senior, guide, return_times, t)
        if t > shortest_time:
            return sys.float_info.max

    total_time = t
    for time in return_times:
        if time > total_time:
            total_time = time

    return total_time


def get_result(v, seniors):
    permutations = itertools.permutations(seniors, len(seniors))
    shortest_time = sys.float_info.max
    for p in permutations:
        time = catch_them_all(v, p, shortest_time)
        if time < shortest_time:
            shortest_time = time

    return shortest_time


def get_inputs(inputs):
    v = float(inputs[1])
    seniors = []
    for line in inputs[2:]:
        pqwa = line.split()
        seniors.append(Senior(float(pqwa[0]), float(pqwa[1]), float(pqwa[2]), float(pqwa[3])))

    print int(round(get_result(v, seniors),0))


n = 0
inputs = sys.stdin.readlines()
number_of_seniors = int(inputs[0])

while number_of_seniors > 0:
    get_inputs(inputs[n : number_of_seniors + n + 2])
    n += number_of_seniors + 2
    number_of_seniors = int(inputs[n])
