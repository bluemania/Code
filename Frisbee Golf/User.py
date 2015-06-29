from Utilities import *
import math


class User:
    def __init__(self):
        self.score = 0
        self.hole_score = 0
        self.position = [0.0, 0.0]
        self.player = None
        self.finished_hole = False
        self.name = ""

    def character_select(self):
        print("You have chosen " + self.player.name +
              ". He is " + str(self.player.age) + " years old and " +
              str(self.player.height) + " metres tall.")
        print("Here is a picture of him")
        print(self.player.name + 's special ability is ' + self.player.special)
        show_pic(self.player.picture)
        return

    def distance_to_goal(self, goal_coord):
        ax = ((goal_coord[0] - self.position[0]) ** 2)
        bx = ((goal_coord[1] - self.position[1]) ** 2)
        return math.sqrt(ax + bx)

    def prompt_and_throw(self, temp_goal_position, temp_wind):
        print(self.name + ", your character, " + self.player.name +
              " is aiming directly at the target, " +
              str(round(self.distance_to_goal(temp_goal_position), 2)) +
              "m away")
        horizontal_throw = -100.0
        vertical_throw = -100.0
        power_throw = -100.0
        while (horizontal_throw > 90) or (horizontal_throw < -90):
            user_input = raw_input("Change your horizontal direction? Use '-' for left:")
            horizontal_throw = float(user_input) if user_input is not None else -100
        while (vertical_throw > 90) or (vertical_throw < -90):
            vertical_throw = float(raw_input("Change your vertical direction? Currently aiming at the horizon: "))
        while (power_throw > 100) or (power_throw < 0):
            power_throw = float(raw_input("How hard do you want to throw your frisbee? Max of 100:"))

        total_throw = (self.player.strength * 0.06) * (power_throw * 0.06)

        horizontal_throw += self.look_to_target(temp_goal_position)

        g = 9.8
        vxo = total_throw * make_cos(vertical_throw)
        vyo = total_throw * make_sin(vertical_throw)
        time_rise = vyo / g
        h = self.player.height + vyo * time_rise - 0.5 * g * (time_rise ** 2)
        time_fall = math.sqrt(2 * h / g)
        time_flight = time_rise + time_fall
        total_range = vxo * time_flight

        # Returns the temporary throw coordinates before wind is applied
        pre_wind = [0.0, 0.0]
        pre_wind[0] = self.position[0] + total_range * make_sin(horizontal_throw)
        pre_wind[1] = self.position[1] + total_range * make_cos(horizontal_throw)

        # Returns the temporary throw coordinates before wind is applied
        post_throw = [0.0, 0.0]
        post_throw[0] = pre_wind[0] + time_flight * temp_wind.strength * make_sin(temp_wind.direction)
        post_throw[1] = pre_wind[1] + time_flight * temp_wind.strength * make_cos(temp_wind.direction)

        self.position = post_throw
        self.hole_score += 1
        return

    # makes the thrower look at the target first
    def look_to_target(self, goal_coordinates):
        return rad2deg(math.atan2(goal_coordinates[0] - self.position[0], goal_coordinates[1] - self.position[1]))

    def show_zone_picture(self):
        try:
            show_pic(TheGame.hole.get_current_zone(self.position).picture)
        except:
            print("Out of bounds")
