from Utilities import *

class Zone:
    def __init__(self):
        self.coordinate = ()
        self.picture = ""
        self.is_goal = False
        self.outofbound = False

    def has_coord(self, coord):
        z_far_boundary = (5432.1, 123.45)
        pip_test = 0
        if intersect(coord, z_far_boundary, self.coordinate[0], self.coordinate[1]):
            pip_test += 1
        if intersect(coord, z_far_boundary, self.coordinate[0], self.coordinate[2]):
            pip_test += 1
        if intersect(coord, z_far_boundary, self.coordinate[1], self.coordinate[2]):
            pip_test += 1
        if pip_test % 2 == 0:
            return False
        if pip_test % 2 == 1:
            return True
