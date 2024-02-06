#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """ triangle of size n

    return a list of lists on integers
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
