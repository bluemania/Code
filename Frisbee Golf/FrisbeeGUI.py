import pygame

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Nick's Frisbee Golf Challenge")
screen.fill(white)
clock = pygame.time.Clock()
done = False



def intro(user_input):
    img = pygame.image.load("Map\Intro.jpg")
    screen.blit(img, (0, 0))
    font = pygame.font.SysFont(None, 70)
    intro_text = font.render("Nick's Frisbee Golf Challenge", True, red)
    screen.blit(intro_text, (50, 400))
    if user_input == "Space":
        Screens.remove(Screens[0])

def character_select(user_input):
    img = pygame.image.load("Map\A.jpg")
    screen.blit(img, (0, 0))
    intro_text = font.render("todo, will display character select", True, red)
    screen.blit(intro_text, (50, 400))
    if user_input == "Space":
        Screens.remove(Screens[0])

def course_tour(user_input):
    img = pygame.image.load("Map\A.jpg")
    screen.blit(img, (0, 0))
    intro_text = font.render("Tour of the course", True, red)
    screen.blit(intro_text, (50, 400))
    if user_input == "Space":
        Screens.remove(Screens[0])


def hole_tour(): pass
def hole(): pass

Screens = [intro, character_select, course_tour, hole_tour, hole]
print(Screens)

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

    Screens[0](key_pressed)



    # action on the screen




    #
    pygame.display.flip()
    clock.tick(10)

pygame.quit()

