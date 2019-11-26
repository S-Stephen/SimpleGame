import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

#screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode(size=size)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = [0, 0, 255]


#ball = pygame.image.load("intro_ball.gif")
#ballrect = ball.get_rect()
#
# TODO fix draw a circle:
# pygame.draw.circle(screen,200,(0,0),14,14)


    # this line is used to clear the window and set background color (later background will be a portion of a location on a map)
screen.fill(WHITE)

    # draw circle
    # first row of circles
pygame.draw.circle(screen, BLACK, [80, 80], 80, 1)

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
#
#    ballrect = ballrect.move(speed)
#    if ballrect.left < 0 or ballrect.right > width:
#        speed[0] = -speed[0]
#    if ballrect.top < 0 or ballrect.bottom > height:
#        speed[1] = -speed[1]
#
    screen.fill(black)
#    screen.blit(ball, ballrect)
#    pygame.display.flip()
