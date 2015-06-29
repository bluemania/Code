__author__ = 'nick.jenkins'

import math

"""
Free definitions throwing
"""

# Returns the sin/cos of input in degrees
def make_sin(x):
    return math.sin(float(x) / 57.2957795)


def rad2deg(x):
    return x * 57.2957795


def make_cos(x):
    return math.cos(float(x) / 57.2957795)


def ccw(a, b, c):
    return ((c[1] - a[1]) * (b[0] - a[0])) > ((b[1] - a[1]) * (c[0] - a[0]))


def intersect(a, b, c, d):
    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)


def show_pic(picture_input):
    pass
    # webbrowser.open(picture_input)
