import random

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