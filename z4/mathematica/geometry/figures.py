
def square_area(a):
    return a * a


def triangle_area(a, b, c):
    # calculate the Perimeter
    perimeter = a + b + c
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    # calculate the area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
