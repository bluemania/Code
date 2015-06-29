
from Game import *
from Zone import *
from Hole import *
from Utilities import *
from Course import *


"""
Create data to fill into the above classes
"""

def construct_game():

    # Creates zones
    Z1A1 = Zone()
    Z1A1.coordinate = ((5, 0), (10, 20), (-10, 20))
    Z1A1.picture = 'Map\A.jpg'
    Z1A1.is_goal = False

    Z1A2 = Zone()
    Z1A2.coordinate = ((-10, 20), (-5, 0), (5, 0))
    Z1A2.picture = 'Map\A.jpg'
    Z1A2.is_goal = False

    Z1B1 = Zone()
    Z1B1.coordinate = ((-20, 30), (-10, 20), (-5, 30))
    Z1B1.picture = 'Map\B.jpg'
    Z1B1.is_goal = False

    Z1B2 = Zone()
    Z1B2.coordinate = ((-20, 30), (-10, 35), (-5, 30))
    Z1B2.picture = 'Map\B.jpg'
    Z1B2.is_goal = False

    Z1C1 = Zone()
    Z1C1.coordinate = ((-10, 20), (-5, 30), (5, 30))
    Z1C1.picture = 'Map\C.jpg'
    Z1C1.is_goal = False

    Z1C2 = Zone()
    Z1C2.coordinate = ((-5, 30), (5, 30), (10, 20))
    Z1C2.picture = 'Map\C.jpg'
    Z1C2.is_goal = False

    Z1D1 = Zone()
    Z1D1.coordinate = ((10, 20), (5, 30), (20, 30))
    Z1D1.picture = 'Map\D.jpg'
    Z1D1.is_goal = False

    Z1D2 = Zone()
    Z1D2.coordinate = ((5, 30), (20, 30), (10, 35))
    Z1D2.picture = 'Map\D.jpg'
    Z1D2.is_goal = False

    Z1E = Zone()
    Z1E.coordinate = ((-5, 55), (-10, 45), (0, 40))
    Z1E.picture = 'Map\E.jpg'
    Z1E.is_goal = False

    Z1F = Zone()
    Z1F.coordinate = ((-10, 45), (-10, 35), (0, 40))
    Z1F.picture = 'Map\F.jpg'
    Z1F.is_goal = False

    Z1G = Zone()
    Z1G.coordinate = ((-10, 35), (-5, 30), (0, 40))
    Z1G.picture = 'Map\G.jpg'
    Z1G.is_goal = False

    Z1H = Zone()
    Z1H.coordinate = ((-5, 30), (5, 30), (0, 40))
    Z1H.picture = 'Map\H.jpg'
    Z1H.is_goal = False

    Z1I = Zone()
    Z1I.coordinate = ((5, 30), (10, 35), (0, 40))
    Z1I.picture = 'Map\I.jpg'
    Z1I.is_goal = False

    Z1J = Zone()
    Z1J.coordinate = ((10, 35), (10, 45), (0, 40))
    Z1J.picture = 'Map\J.jpg'
    Z1J.is_goal = False

    Z1K = Zone()
    Z1K.coordinate = ((10, 45), (5, 55), (0, 40))
    Z1K.picture = 'Map\K.jpg'
    Z1K.is_goal = False

    Z1G1 = Zone()
    Z1G1.coordinate = ((-1, 39), (-1, 41), (1, 39))
    Z1G1.picture = 'Map\Goal.png'
    Z1G1.is_goal = True

    Z1G2 = Zone()
    Z1G2.coordinate = ((-1, 41), (1, 41), (1, 39))
    Z1G2.picture = 'Map\Goal.png'
    Z1G2.is_goal = True

    Z2A1 = Zone()
    Z2A1.coordinate = ((5, 0), (10, 20), (-10, 20))
    Z2A1.picture = 'Map\A.jpg'
    Z2A1.is_goal = False

    Z2A2 = Zone()
    Z2A2.coordinate = ((-10, 20), (-5, 0), (5, 0))
    Z2A2.picture = 'Map\A.jpg'
    Z2A2.is_goal = False

    Z2B1 = Zone()
    Z2B1.coordinate = ((-20, 30), (-10, 20), (-5, 30))
    Z2B1.picture = 'Map\B.jpg'
    Z2B1.is_goal = False

    Z2B2 = Zone()
    Z2B2.coordinate = ((-20, 30), (-10, 35), (-5, 30))
    Z2B2.picture = 'Map\B.jpg'
    Z2B2.is_goal = False

    Z2C1 = Zone()
    Z2C1.coordinate = ((-10, 20), (-5, 30), (5, 30))
    Z2C1.picture = 'Map\C.jpg'
    Z2C1.is_goal = False

    Z2C2 = Zone()
    Z2C2.coordinate = ((-5, 30), (5, 30), (10, 20))
    Z2C2.picture = 'Map\C.jpg'
    Z2C2.is_goal = False

    Z2D1 = Zone()
    Z2D1.coordinate = ((10, 20), (5, 30), (20, 30))
    Z2D1.picture = 'Map\D.jpg'
    Z2D1.is_goal = False

    Z2D2 = Zone()
    Z2D2.coordinate = ((5, 30), (20, 30), (10, 35))
    Z2D2.picture = 'Map\D.jpg'
    Z2D2.is_goal = False

    Z2E = Zone()
    Z2E.coordinate = ((-5, 55), (-10, 45), (0, 40))
    Z2E.picture = 'Map\E.jpg'
    Z2E.is_goal = False

    Z2F = Zone()
    Z2F.coordinate = ((-10, 45), (-10, 35), (0, 40))
    Z2F.picture = 'Map\F.jpg'
    Z2F.is_goal = False

    Z2G = Zone()
    Z2G.coordinate = ((-10, 35), (-5, 30), (0, 40))
    Z2G.picture = 'Map\G.jpg'
    Z2G.is_goal = False

    Z2H = Zone()
    Z2H.coordinate = ((-5, 30), (5, 30), (0, 40))
    Z2H.picture = 'Map\H.jpg'
    Z2H.is_goal = False

    Z2I = Zone()
    Z2I.coordinate = ((5, 30), (10, 35), (0, 40))
    Z2I.picture = 'Map\I.jpg'
    Z2I.is_goal = False

    Z2J = Zone()
    Z2J.coordinate = ((10, 35), (10, 45), (0, 40))
    Z2J.picture = 'Map\J.jpg'
    Z2J.is_goal = False

    Z2K = Zone()
    Z2K.coordinate = ((10, 45), (5, 55), (0, 40))
    Z2K.picture = 'Map\K.jpg'
    Z2K.is_goal = False

    Z2G1 = Zone()
    Z2G1.coordinate = ((-1, 39), (-1, 41), (1, 39))
    Z2G1.picture = 'Map\Goal.png'
    Z2G1.is_goal = True

    Z2G2 = Zone()
    Z2G2.coordinate = ((-1, 41), (1, 41), (1, 39))
    Z2G2.picture = 'Map\Goal.png'
    Z2G2.is_goal = True


    Z3A1 = Zone()
    Z3A1.coordinate = ((5, 0), (10, 20), (-10, 20))
    Z3A1.picture = 'Map\A.jpg'
    Z3A1.is_goal = False

    Z3A2 = Zone()
    Z3A2.coordinate = ((-10, 20), (-5, 0), (5, 0))
    Z3A2.picture = 'Map\A.jpg'
    Z3A2.is_goal = False

    Z3B1 = Zone()
    Z3B1.coordinate = ((-20, 30), (-10, 20), (-5, 30))
    Z3B1.picture = 'Map\B.jpg'
    Z3B1.is_goal = False

    Z3B2 = Zone()
    Z3B2.coordinate = ((-20, 30), (-10, 35), (-5, 30))
    Z3B2.picture = 'Map\B.jpg'
    Z3B2.is_goal = False

    Z3C1 = Zone()
    Z3C1.coordinate = ((-10, 20), (-5, 30), (5, 30))
    Z3C1.picture = 'Map\C.jpg'
    Z3C1.is_goal = False

    Z3C2 = Zone()
    Z3C2.coordinate = ((-5, 30), (5, 30), (10, 20))
    Z3C2.picture = 'Map\C.jpg'
    Z3C2.is_goal = False

    Z3D1 = Zone()
    Z3D1.coordinate = ((10, 20), (5, 30), (20, 30))
    Z3D1.picture = 'Map\D.jpg'
    Z3D1.is_goal = False

    Z3D2 = Zone()
    Z3D2.coordinate = ((5, 30), (20, 30), (10, 35))
    Z3D2.picture = 'Map\D.jpg'
    Z3D2.is_goal = False

    Z3E = Zone()
    Z3E.coordinate = ((-5, 55), (-10, 45), (0, 40))
    Z3E.picture = 'Map\E.jpg'
    Z3E.is_goal = False

    Z3F = Zone()
    Z3F.coordinate = ((-10, 45), (-10, 35), (0, 40))
    Z3F.picture = 'Map\F.jpg'
    Z3F.is_goal = False

    Z3G = Zone()
    Z3G.coordinate = ((-10, 35), (-5, 30), (0, 40))
    Z3G.picture = 'Map\G.jpg'
    Z3G.is_goal = False

    Z3H = Zone()
    Z3H.coordinate = ((-5, 30), (5, 30), (0, 40))
    Z3H.picture = 'Map\H.jpg'
    Z3H.is_goal = False

    Z3I = Zone()
    Z3I.coordinate = ((5, 30), (10, 35), (0, 40))
    Z3I.picture = 'Map\I.jpg'
    Z3I.is_goal = False

    Z3J = Zone()
    Z3J.coordinate = ((10, 35), (10, 45), (0, 40))
    Z3J.picture = 'Map\J.jpg'
    Z3J.is_goal = False

    Z3K = Zone()
    Z3K.coordinate = ((10, 45), (5, 55), (0, 40))
    Z3K.picture = 'Map\K.jpg'
    Z3K.is_goal = False

    Z3G1 = Zone()
    Z3G1.coordinate = ((-1, 39), (-1, 41), (1, 39))
    Z3G1.picture = 'Map\Goal.png'
    Z3G1.is_goal = True

    Z3G2 = Zone()
    Z3G2.coordinate = ((-1, 41), (1, 41), (1, 39))
    Z3G2.picture = 'Map\Goal.png'
    Z3G2.is_goal = True

    """
    Constructs object hierarchy
    """
    # create users


    StKH1 = Hole()
    StKH1.name = "Cage to Cage hole (temp 1)"
    StKH1.zones = [Z1A1, Z1A2, Z1B1, Z1B2, Z1C1, Z1C2, Z1D1, Z1D2, Z1E, Z1F, Z1G, Z1H, Z1I, Z1J, Z1K]
    StKH1.goal_position = (0, 40)
    StKH1.goal_zone = [Z1G1, Z1G2]
    StKH1.starting_position = (0, 0)
    StKH1.par = 3
    StKH1.number = 1

    StKH2 = Hole()
    StKH2.name = "Cage to Cage hole"
    StKH2.zones = [Z2A1, Z2A2, Z2B1, Z2B2, Z2C1, Z2C2, Z2D1, Z2D2, Z2E, Z2F, Z2G, Z2H, Z2I, Z2J, Z2K]
    StKH2.goal_position = (0, 40)
    StKH2.goal_zone = [Z2G1, Z2G2]
    StKH2.starting_position = (0, 0)
    StKH2.par = 3
    StKH2.number = 2

    StKH3 = Hole()
    StKH3.name = "Cage to Cage hole (temp 3)"
    StKH3.zones = [Z3A1, Z3A2, Z3B1, Z3B2, Z3C1, Z3C2, Z3D1, Z3D2, Z3E, Z3F, Z3G, Z3H, Z3I, Z3J, Z3K]
    StKH3.goal_position = (0, 40)
    StKH3.goal_zone = [Z3G1, Z3G2]
    StKH3.starting_position = (0, 0)
    StKH3.par = 3
    StKH3.number = 3

    StK = Course()
    StK.name = "St Kilda Botanical Gardens"
    StK.holes = [StKH1, StKH2, StKH3]

    TheGame = Game()
    TheGame.course = StK
    TheGame.hole = StK.holes[0]

    return TheGame