from User import *
from Player import *



class Game:
    def __init__(self):
        self.users = []
        self.course = None
        self.hole = None
        self.turn_queue = []
        self.hole_completed = False
        self.players = []
        self.initialise_characters()

    def report_results(self, goal_coordinates):
        # prints results for each player
        for report_user_result in self.users:
            print(report_user_result.name + " has played " + str(report_user_result.hole_score) + " shots and has " +
                  str(round(report_user_result.distance_to_goal(goal_coordinates), 2)) +
                  "m left. " + str(round(report_user_result.position[0], 2)) + ", " +
                  str(round(report_user_result.position[1], 2)))

    def setup_next_hole(self, temp_next_hole):
        # set up the hole and tour
        self.turn_queue = list(self.users)
        self.hole = temp_next_hole
        self.hole.tour()
        for next_user in self.users:
            next_user.position = self.hole.starting_position
            next_user.hole_score = 0
            next_user.finished_hole = False

    def setup_players(self):
        # ask how many players
        player_count = int(raw_input("How many players?: "))
        for count in range(player_count):
            temp_user_assign = User()
            temp_user_assign.name = "Player " + str(count+1)
            self.users.append(temp_user_assign)

    def setup_characters(self):

        choose_character = "("
        for Player in self.players:
            choose_character += str(Player.name) + "/"
        choose_character += "): "

        for next_player in range(len(self.users)):
            while self.users[next_player].player is None:
                player_name = raw_input(self.users[next_player].name + ", first, choose your character" + choose_character)
                for Player in self.players:
                    if Player.name == player_name:
                        self.users[next_player].player = Player
            self.users[next_player].character_select()

    def initialise_characters(self):

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

        self.players = [Nick, Todd, Chris, Brad]
        
    # method names should be verbs describing doing
    def play(self):
                # loops through each hole in the course
        for each_hole in self.course.holes:
        
            # set up the hole and tour
            self.setup_next_hole(each_hole)
        
            # runs until the turn_queue is empty
            while self.turn_queue:
        
                # sorts the turn_queue according to least distance, or, lowest throw count
                self.turn_queue.sort(key=lambda x: (x.distance_to_goal(self.hole.goal_position), x.score), reverse=True)
        
                user = self.turn_queue[0]
        
                # prompts input, calculates result
                user.prompt_and_throw(self.hole.goal_position, self.hole.wind)
                user.show_zone_picture()
        
                if self.hole.is_in_goal(user.position):
                    print("Hole finished! You made it in " + str(user.hole_score) + " shots.")
                    self.turn_queue.remove(user)
                elif user.distance_to_goal(self.hole.goal_position) < user.player.height:
                    user.hole_score += 1
                    print("Close to hole, Gimme awarded! You made it in " + str(user.hole_score) + " shots.")
                    self.turn_queue.remove(user)
                elif user.hole_score > self.hole.par + 2:
                    print("Ok that's enough, you made three over par, " + str(user.hole_score) + " shots.")
                    self.turn_queue.remove(user)

                self.report_results(self.hole.goal_position)
        
            # self.finished_hole()
            print("All players finished hole!")
        
            for each_score in self.users:
                each_score.score = each_score.score + each_score.hole_score
            sorted(self.users, key=lambda x: x.score)
            for each in self.users:
                print(each.name)
                print(str(each.score))
            # Arrrrg!!! This has dropped my players from the list!!
            # print("Course leader is: " + self.users[0].name + " after " + str(self.hole.number) + " holes.")
            # self.turn_queue = self.users
        
        # add winner
        print("And they have won the game!")

