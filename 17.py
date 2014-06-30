#coding=utf-8
import pygame,sys
pygame.init()
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)
screen = pygame.display.set_mode([640,480])
background = pygame.Surface(screen.get_size())
background.fill([255,255,255])
clock = pygame.time.Clock()

#-----------------创建Ball类及move方法
class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed ,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        if self.rect.left <= screen.get_rect().left or self.rect.right >= screen.get_rect().right:
            self.speed[0] = - self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos
#------------------建立球的实例 文件位置 速度 位置
my_ball = Ball('beach_ball.png',[10,0], [20,20])
held_down = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #当鼠标按下时即为pygame.MOUSEBUTTONDOWN held_down为真
        elif event.type == pygame.MOUSEBUTTONDOWN:
            held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held_down = False
        elif event.type == pygame.MOUSEMOTION:
        #如果held_down为真 啧重新绘制球体位置
            if held_down:
                my_ball.rect.center = event.pos
        #elif event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_UP:
        #        my_ball.rect.top =my_ball.rect.top -10
        #    elif event.key == pygame.K_DOWN:
        #        my_ball.rect.top = my_ball.rect.top +10
    #这是时钟
    clock.tick(30)
    #-------完全重绘界面
    screen.blit(background, (0,0))
    my_ball.move()
    screen.blit(my_ball.image,my_ball.rect)
    pygame.display.flip()