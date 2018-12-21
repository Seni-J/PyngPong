import pygame, sys
from pygame.locals import *


width = 800
height = width / 16 * 9
fps = 60
linethickness = 10

screen = pygame.display.set_mode((width, int(height)))

timer = pygame.time.Clock()

#Player's paddles
paddle_one = {'x': 0, 'y': 0, 'width': 50, 'height': 150}
paddle_two = {'x': 0, 'y': 0, 'width': 50, 'height': 150}

ball = {'x': 0, 'y': 0, 'width': 50, 'height': 150}

#Score
playerone_score = 0
AI_score = 0

#Colors
black = (0, 0, 0)
white = (255, 255, 255)

def drawArena():
    


#Run the game
def main():
    pygame.init()
    global DISPLAYSURF

    pygame.display.set_caption('Pyng Pong')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        timer.tick(fps)

if __name__ == '__main__':
    main()
