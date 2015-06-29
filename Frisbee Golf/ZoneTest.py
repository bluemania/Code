__author__ = 'nick.jenkins'


class Zone:
    def __init__(self):
        self.coordinate = ()
        self.picture = ""
        self.isgoal = False
        self.outofbound = False


# Creates the far away zone for point in polygon testing


# Creates zones
ZT = Zone()
ZT.coordinate = ((0, 0), (10, 10), (0, 10))
ZT.picture = 'Map\Goal.png'
ZT.isgoal = True
ZT.outofbounds = False

ZA1 = Zone()
ZA1.coordinate = ((5, 0), (10, 20), (-10, 20))
ZA1.picture = 'Map\A.jpg'
ZA1.isgoal = False
ZA1.outofbounds = False

ZA2 = Zone()
ZA2.coordinate = ((-10, 20), (-5, 0), (5, 0))
ZA2.picture = 'Map\A.jpg'
ZA2.isgoal = False
ZA2.outofbounds = False

ZB1 = Zone()
ZB1.coordinate = ((-20, 30), (-10, 20), (-5, 30))
ZB1.picture = 'Map\B.jpg'
ZB1.isgoal = False
ZB1.outofbounds = False

ZB2 = Zone()
ZB2.coordinate = ((-20, 30), (-10, 35), (-5, 30))
ZB2.picture = 'Map\B.jpg'
ZB2.isgoal = False
ZB2.outofbounds = False

ZC1 = Zone()
ZC1.coordinate = ((-10, 20), (-5, 30), (5, 30))
ZC1.picture = 'Map\C.jpg'
ZC1.isgoal = False
ZC1.outofbounds = False

ZC2 = Zone()
ZC2.coordinate = ((-5, 30), (5, 30), (10, 20))
ZC2.picture = 'Map\C.jpg'
ZC2.isgoal = False
ZC2.outofbounds = False

ZD1 = Zone()
ZD1.coordinate = ((10, 20), (5, 30), (20, 30))
ZD1.picture = 'Map\D.jpg'
ZD1.isgoal = False
ZD1.outofbounds = False

ZD2 = Zone()
ZD2.coordinate = ((5, 30), (20, 30), (10, 35))
ZD2.picture = 'Map\D.jpg'
ZD2.isgoal = False
ZD2.outofbounds = False

ZE = Zone()
ZE.coordinate = ((-5, 55), (-10, 45), (0, 40))
ZE.picture = 'Map\E.jpg'
ZE.isgoal = False
ZE.outofbounds = False

ZF = Zone()
ZF.coordinate = ((-10, 45), (-10, 35), (0, 40))
ZF.picture = 'Map\F.jpg'
ZF.isgoal = False
ZF.outofbounds = False

ZG = Zone()
ZG.coordinate = ((-10, 35), (-5, 30), (0, 40))
ZG.picture = 'Map\G.jpg'
ZG.isgoal = False
ZG.outofbounds = False

ZH = Zone()
ZH.coordinate = ((-5, 30), (5, 30), (0, 40))
ZH.picture = 'Map\H.jpg'
ZH.isgoal = False
ZH.outofbounds = False

ZI = Zone()
ZI.coordinate = ((5, 30), (10, 35), (0, 40))
ZI.picture = 'Map\I.jpg'
ZI.isgoal = False
ZI.outofbounds = False

ZJ = Zone()
ZJ.coordinate = ((10, 35), (10, 45), (0, 40))
ZJ.picture = 'Map\J.jpg'
ZJ.isgoal = False
ZJ.outofbounds = False

ZK = Zone()
ZK.coordinate = ((10, 45), (5, 55), (0, 40))
ZK.picture = 'Map\K.jpg'
ZK.isgoal = False
ZK.outofbounds = False

ZG1 = Zone()
ZG1.coordinate = ((-1, 39), (-1, 41), (1, 39))
ZG1.picture = 'Map\Goal.png'
ZG1.isgoal = True
ZG1.outofbounds = False

ZG2 = Zone()
ZG2.coordinate = ((-1, 41), (1, 41), (1, 39))
ZG2.picture = 'Map\Goal.png'
ZG2.isgoal = True
ZG2.outofbounds = False

zonelist = [ZA1, ZA2, ZB1, ZB2, ZC1, ZC2, ZD1, ZD2, ZE, ZF, ZG, ZH, ZI, ZJ, ZK, ZG1, ZG2]


def ccw(A, B, C):
    return ((C[1]-A[1]) * (B[0]-A[0])) > ((B[1]-A[1]) * (C[0]-A[0]))

def intersect(A, B, C, D):
        return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

# tests if the frisbee is within a given zone by returning True
def area_tester(the_frisbee_coordinate, zone_coord):
    Z_far_boundary = (5432.1, 123.45)
    pip_test = 0
    if intersect(the_frisbee_coordinate, Z_far_boundary, zone_coord[0], zone_coord[1]):
        pip_test = pip_test + 1
    if intersect(the_frisbee_coordinate, Z_far_boundary, zone_coord[0], zone_coord[2]):
        pip_test = pip_test + 1
    if intersect(the_frisbee_coordinate, Z_far_boundary, zone_coord[1], zone_coord[2]):
        pip_test = pip_test + 1
    if pip_test % 2 == 0:
        return False
    if pip_test % 2 == 1:
        return True


def throw_outcome(the_frisbee_coordinates, zonelist):
    check_zone_result = -1
    for zone in zonelist:
        if area_tester(the_frisbee_coordinate, zone.coordinate) and zone.isgoal:
            check_zone_result = 1
        elif area_tester(the_frisbee_coordinate, zone.coordinate) and check_zone_result != 1:
            wbo(zone.picture)
            check_zone_result = 0

    if check_zone_result==-1:
        print("Out of bounds")

    return check_zone_result


"""
redundant variables
"""

import webbrowser
# quick get picture
def wbo(picture_input):
    webbrowser.open(picture_input)
import random
import time

"""
testing
"""

# if frisbee coordinate is too accurate (i.e on a point, it will exist in multiple zones
the_frisbee_coordinate = (5.1, 30.1)
throw_outcome(the_frisbee_coordinate, zonelist)


for each in range(0,10):
    the_frisbee_coordinate = random.randrange(-20, 20), random.randrange(0, 55)
    print the_frisbee_coordinate
    throw_outcome(the_frisbee_coordinate, zonelist)
    time.sleep(2)



