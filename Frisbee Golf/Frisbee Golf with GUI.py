"""
Import dependencies
"""

import time
import webbrowser
import random
import math
import pygame

"""
Set classes
"""


class Game:
    def __init__(self):
        self.users = []
        self.course = None
        self.hole = None
        self.turn_queue = []
        self.hole_completed = False
        self.player_setup_state = False
        self.character_setup_state = False

    def report_results(self, goal_coordinates):
        # prints results for each player
        for report_user_result in self.users:
            print(report_user_result.name + " has played " + str(report_user_result.hole_score) + " shots and has " +
                  str(round(report_user_result.distance_to_goal(goal_coordinates), 2)) +
                  "m left. " + str(round(report_user_result.position[0], 2)) + ", " +
                  str(round(report_user_result.position[1], 2)))

    def setup_next_hole(self, temp_next_hole):
        # set up the hole and tour
        self.hole = temp_next_hole
        self.hole.tour()
        for next_user in self.users:
            next_user.position = self.hole.starting_position
            next_user.hole_score = 0
            next_user.finished_hole = False

    def setup_players(self, user_input):
        # ask how many players
        while not self.player_setup_state:
            player_count = int(raw_input("How many players?: "))
            for count in range(player_count):
                temp_user_assign = User()
                temp_user_assign.name = "Player " + str(count+1)
                TheGame.users.append(temp_user_assign)
            # player one shoots first
            TheGame.turn_queue = TheGame.users
            self.player_setup_state = True
        #if user_input == "Space":
            game_state.remove(game_state[0])

    def setup_characters(self, user_input):
        while not self.character_setup_state:
            choose_character = "("
            for Player in Players:
                choose_character += str(Player.name) + "/"
            choose_character += "): "

            for next_player in range(len(self.users)):
                while self.users[next_player].player is None:
                    player_name = raw_input(self.users[next_player].name + ", first, choose your character" + choose_character)
                    for Player in Players:
                        if Player.name == player_name:
                            self.users[next_player].player = Player
                self.users[next_player].character_select()
            self.character_setup_state = True
            #if user_input == "Space":
            game_state.remove(game_state[0])

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
            horizontal_throw = float(raw_input("Change your horizontal direction? Use '-' for left:"))
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

    def throw_result(self):
        # determine if current turn_queue is in hole, if they are, show score and pop from queue
        if TheGame.hole.is_in_goal(self.position):
            print("Hole finished! You made it in " + str(self.hole_score) + " shots.")
            TheGame.turn_queue.remove(self)
        elif self.distance_to_goal(TheGame.hole.goal_position) < self.player.height:
            self.hole_score += 1
            print("Close to hole, Gimme awarded! You made it in " + str(self.hole_score) + " shots.")
            TheGame.turn_queue.remove(self)
        elif self.hole_score > TheGame.hole.par + 2:
            print("Ok that's enough, you made three over par, " + str(self.hole_score) + " shots.")
            TheGame.turn_queue.remove(self)

    def show_zone_picture(self):
        try:
            show_pic(TheGame.hole.get_current_zone(self.position).picture)
        except:
            print("Out of bounds")


class Player:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.strength = 0.0
        self.height = 0.0
        self.picture = ""
        self.luck = 0.0
        self.temperament = 0.0
        self.special = ""
        self.saying = ""
        self.right_handed = True


class Course:
    def __init__(self):
        self.name = ""
        self.holes = []
        self.wind = Wind()


class Wind:
    def __init__(self):
        self.direction = 0.0
        self.strength = 0.0
        self.randomise()

    def randomise(self):
        self.direction = (random.randint(0, 360))
        self.strength = random.randint(0, 5)

    # add subtle random

    # describes which direction the wind is coming from
    def to_string(self):
        y = 0
        wind_text = ""

        if self.direction >= 337.5:
            wind_text = "North"
        else:
            y = (self.direction - 22.5) / 45

        if y < 0:
            wind_text = "North"
        elif y < 1:
            wind_text = "North-East"
        elif y < 2:
            wind_text = "East"
        elif y < 3:
            wind_text = "South-East"
        elif y < 4:
            wind_text = "South"
        elif y < 5:
            wind_text = "South-West"
        elif y < 6:
            wind_text = "West"
        elif y < 7:
            wind_text = "North-West"

        y = 22.5
        if self.direction < y and self.direction < (y + 45):
            wind_text = "North-East"

        return "Wind on the course is heading to the " + wind_text + ", with an approximate wind speed of " \
               + str(round(self.strength)) + "km/h"


class Hole:
    def __init__(self):
        self.zones = []
        self.starting_position = (0.0, 0.0)
        self.goal_position = (0.0, 0.0)
        self.goal_zone = []
        self.name = ""
        self.number = 0
        self.par = 0

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
        print(StK.wind.to_string())


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


"""
Create data to fill into the above classes
"""

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)

# Populate data into some classes
Brad = Player()
Brad.name = "Brad"
Brad.age = 30
Brad.strength = 100
Brad.height = 1.8
Brad.picture = 'Art\Brad.png'
Brad.luck = 95
Brad.temperament = 105
Brad.special = 'listening to 90s music'
Brad.saying = 'radical!'
Brad.right_handed = False

Chris = Player()
Chris.name = "Chris"
Chris.age = 29
Chris.strength = 85
Chris.height = 1.7
Chris.picture = 'Art\Chris.png'
Chris.luck = 110
Chris.temperament = 110
Chris.special = 'the BainesTree'
Chris.saying = '...................'
Chris.right_handed = False

Nick = Player()
Nick.name = "Nick"
Nick.age = 30
Nick.strength = 95
Nick.height = 2.0
Nick.picture = 'Art\Nick.png'
Nick.luck = 95
Nick.temperament = 95
Nick.special = 'inventing new shit'
Nick.saying = 'yeeeeeeeha!'

Todd = Player()
Todd.name = "Todd"
Todd.age = 29
Todd.strength = 90
Todd.height = 1.8
Todd.picture = 'Art\Todd.png'
Todd.luck = 95
Todd.temperament = 100
Todd.special = 'occassionally playing'
Todd.saying = 'its time to kick ass as chew gum, and im all out of gum!'


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
    img = pygame.image.load(picture_input)
    screen.blit(img, (0, 0))

def intro(user_input):
    show_pic("Map\Intro.jpg")
    font = pygame.font.SysFont(None, 70)
    intro_text = font.render("Nick's Frisbee Golf Challenge", True, red)
    screen.blit(intro_text, (50, 400))
    if user_input == "Space":
        game_state.remove(game_state[0])

"""
Constructs object hierarchy
"""
# create users
Players = [Brad, Chris, Todd, Nick]

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


"""
Game start
"""

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Nick's Frisbee Golf Challenge")
screen.fill(white)
clock = pygame.time.Clock()
done = False

game_state = [intro, TheGame.setup_players, TheGame.setup_characters]


# total game loop
while not done:

    key_pressed = "None"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                key_pressed = "Space"
            elif event.key == pygame.K_UP:
                key_pressed = "Up"
            elif event.key == pygame.K_DOWN:
                key_pressed = "Down"
            elif event.key == pygame.K_LEFT:
                key_pressed = "Left"
            elif event.key == pygame.K_RIGHT:
                key_pressed = "Right"

    # set screen to nothing
    screen.fill(white)

    # initial game setup
    game_state[0](key_pressed)

    if 1 == 0:
        # loops through each hole in the course
        for each_hole in TheGame.course.holes:

            # set up the hole and tour
            TheGame.setup_next_hole(each_hole)

            # runs until the turn_queue is empty
            while TheGame.turn_queue:

                # prompts input, calculates result
                TheGame.turn_queue[0].prompt_and_throw(TheGame.hole.goal_position, TheGame.course.wind)
                TheGame.turn_queue[0].show_zone_picture()
                TheGame.turn_queue[0].throw_result()
                TheGame.report_results(TheGame.hole.goal_position)

                # sorts the turn_queue according to least distance, or, lowest throw count
                TheGame.turn_queue.sort(key=lambda x: (x.distance_to_goal(TheGame.hole.goal_position), x.score), reverse=True)

            # TheGame.finished_hole()
            print("All players finished hole!")

            for each_score in TheGame.users:
                each_score.score = each_score.score + each_score.hole_score
            sorted(TheGame.users, key=lambda x: x.score)
            for each in TheGame.users:
                print(each.name)
                print(str(each.score))
            # Arrrrg!!! This has dropped my players from the list!!
            # print("Course leader is: " + TheGame.users[0].name + " after " + str(TheGame.hole.number) + " holes.")
            # TheGame.turn_queue = TheGame.users

        # add winner
        print("And they have won the game!")

    pygame.display.flip()
    clock.tick(10)

pygame.quit()