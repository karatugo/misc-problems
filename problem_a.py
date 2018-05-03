import sys

def get_result(a,b):
    m1 = 365
    m2 = 687
    M1, M2 = m2, m1

    def find_inverse(m, modulo):
        for x in range(1, modulo):
            if m*x % modulo == 1:
                return x



    M1_inverse = find_inverse(M1, m1)
    M2_inverse = find_inverse(M2, m2)

    y1 = (a * -1) % m1
    y2 = (b * -1) % m2

    res = y1 * M1 * M1_inverse + y2 * M2 * M2_inverse
    return res % (m1*m2)

n = 1
for line in sys.stdin:
    ab = line.split()
    a = int(ab[0])
    b = int(ab[1])
    result = get_result(a, b)
    print "Case {}: {}".format(n, result)
    n += 1
