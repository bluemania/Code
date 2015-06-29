
from Utilities import show_pic
from Wind import *

class Hole:
    def __init__(self):
        self.zones = []
        self.starting_position = (0.0, 0.0)
        self.goal_position = (0.0, 0.0)
        self.goal_zone = []
        self.name = ""
        self.number = 0
        self.par = 0
        self.wind = Wind()

    def is_in_goal(self, the_frisbee_coordinate):
        for zone in self.goal_zone:
            if zone.has_coord(the_frisbee_coordinate):
                return True
        return False

    def get_current_zone(self, the_frisbee_coordinate):
        for zone in self.zones:
            if zone.has_coord(the_frisbee_coordinate):
                return zone
        return None

    # gives tour of the hole, says wind, player says something
    def tour(self):
        print("Next hole is hole number " + str(self.number) + ", " + self.name + ". It is par " + str(self.par) + ".")
        raw_input("Press enter to see a tour of the hole: ")
        for zone in self.zones:
            show_pic(zone.picture)
            # time.sleep(0.6)
        show_pic(self.zones[0].picture)
        print(self.wind.to_string())