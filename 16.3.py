import pygame,sys
pygame.init()

dots = [[221,432], [225,331], [133,432], [141,310],
        [51, 230], [74, 217], [58, 153], [114,164],
        [123,135], [176,190], [159, 77], [193, 93],
        [230, 28], [267, 93], [301, 77], [284,190],
        [327,135], [336,164], [402,163], [386,217],
        [409,230], [319,310], [327,342], [233,311],
        [237,432]]

screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.lines(screen,[255,0,0],True,dots,2)
pygame.display.flip()
pygame.time.delay(30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
