__author__ = 'nick.jenkins'

import math



# asks for throwing input
def thrower(starting_coordinates, goal_coordinates, player_strength, player_height, wind_direction, wind_speed, hori_throw, veri_throw, powi_throw):

    total_throw = 0.0
    powi_throw = float(powi_throw)
    total_throw = (player_strength*0.06) * (powi_throw*0.06)
    veri_throw = float(veri_throw)
    hori_throw = float(hori_throw)

    hori_throw = look_to_target(starting_coordinates,goal_coordinates) + hori_throw

    g = 9.8
    vxo = total_throw * make_cos(veri_throw)
    vyo = total_throw * make_sin(veri_throw)
    trise = vyo / g
    h = player_height + vyo * trise - 0.5 * g * (trise ** 2)
    tfall = math.sqrt(2 * h / g)
    tflight = trise + tfall
    total_range = vxo * tflight


    # Returns the temporary throw coordinates before wind is applied
    pre_wind_coordinates = [0.0, 0.0]
    pre_wind_coordinates[0] = starting_coordinates[0] + total_range * make_sin(hori_throw)
    pre_wind_coordinates[1] = starting_coordinates[1] + total_range * make_cos(hori_throw)

    # Returns the temporary throw coordinates before wind is applied
    post_wind_coordinates = [0.0, 0.0]
    post_wind_coordinates[0] = pre_wind_coordinates[0] + tflight * wind_speed * make_sin(wind_direction)
    post_wind_coordinates[1] = pre_wind_coordinates[1] + tflight * wind_speed * make_cos(wind_direction)
    new_coordinates = [0.0, 0.0]
    new_coordinates[0] = post_wind_coordinates[0]
    new_coordinates[1] = post_wind_coordinates[1]

    return new_coordinates


#makes the thrower look at the target first
def look_to_target(starting_coordinates, goal_coordinates):
    angle_t = rad2deg(math.atan2(goal_coordinates[0] - starting_coordinates[0], goal_coordinates[1] - starting_coordinates[1]))
    return angle_t

# Returns the sin/cos of input in degrees
def make_sin(x):
    return math.sin(float(x) / 57.2957795)


def rad2deg(x):
    return (x * 57.2957795)


def make_cos(x):
    return math.cos(float(x) / 57.2957795)



#starting_coordinates, goal_coorindates, player_strength, player_height, wind_direction, wind_speed, hori_throw, veri_throw, powi_throw):

print(thrower((0.0, 0.0), (0, 40.0), 100, 2, 0, 0, 0, 20, 100))