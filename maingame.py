import pygame

pygame.init()

wn_size = (1440, 800)
win = pygame.display.set_mode(wn_size)
pygame.display.set_caption("Devil's Maze")

walkRight = [pygame.image.load('NinjaSprite/R1.png'),
             pygame.image.load('NinjaSprite/R2.png'),
             pygame.image.load('NinjaSprite/R3.png'),
             pygame.image.load('NinjaSprite/R4.png')]
walkLeft = [pygame.image.load('NinjaSprite/L1.png'),
            pygame.image.load('NinjaSprite/L2.png'),
            pygame.image.load('NinjaSprite/L3.png'),
            pygame.image.load('NinjaSprite/L4.png')]
walkUp = [pygame.image.load('NinjaSprite/F1.png'),
          pygame.image.load('NinjaSprite/F2.png'),
          pygame.image.load('NinjaSprite/F3.png'),
          pygame.image.load('NinjaSprite/F4.png')]
walkDown = [pygame.image.load('NinjaSprite/B1.png'),
            pygame.image.load('NinjaSprite/B2.png'),
            pygame.image.load('NinjaSprite/B3.png'),
            pygame.image.load('NinjaSprite/B4.png')]
jumpRight = pygame.image.load('NinjaSprite/RJ.png')
jumpLeft = pygame.image.load('NinjaSprite/LJ.png')
jumpUp = pygame.image.load('NinjaSprite/Back.png')
jumpDown = pygame.image.load('NinjaSprite/Standing.png')
bg = pygame.image.load('BGMazes/maze-(1).png')
char = pygame.image.load('NinjaSprite/Standing.png')
char_back = pygame.image.load('NinjaSprite/Back.png')
clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.LB = False

    def draw(self, win):
        if self.walkCount + 1 >= 8:
            self.walkCount = 0
        # Y COORDINATE MOVES
        if self.up:
            win.blit(walkUp[p1.walkCount // 2], (round(self.x), round(self.y)))
            self.walkCount += 1
        elif self.down:
            win.blit(walkDown[p1.walkCount // 2], (round(self.x), round(self.y)))
            self.walkCount += 1
        # X COORDINATE MOVES
        elif self.left:
            win.blit(walkLeft[p1.walkCount // 2], (round(self.x), round(self.y)))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[p1.walkCount // 2], (round(self.x), round(self.y)))
            self.walkCount += 1

        elif self.isJump:
            if self.up:
                win.blit(jumpUp[p1.walkCount // 2] (round(self.x), round(self.y)))
                self.walkCount += 1
            elif self.down:
                win.blit(jumpDown[p1.walkCount // 2] (round(self.x), round(self.y)))
                self.walkCount += 1
            elif self.left:
                win.blit(jumpLeft[p1.walkCount // 2] (round(self.x), round(self.y)))
                self.walkCount += 1
            elif self.right:
                win.blit(jumpRight[p1.walkCount // 2] (round(self.x), round(self.y)))
                self.walkCount += 1
            else:
                win.blit(char, (round(self.x), round(self.y)))

        # CHARACTER IDLE POSITION
        else:                                                             #**********
            if self.LB:
                win.blit(char_back, (round(self.x), round(self.y)))
                self.walkCount = 0

            else:
                win.blit(char, (round(self.x), round(self.y)))
                self.walkCount = 0

                                                                          #***********
def redrawGameWindow():
    win.blit(bg, (0, 0))
    p1.draw(win)
    pygame.display.update()


# MAINLOOP
p1 = player(58, 0, 64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # X COORDINATE ARROW PRESSES
    if keys[pygame.K_LEFT] and p1.x > p1.vel:
        p1.x -= p1.vel
        p1.left = True
        p1.right = False
        p1.up = False
        p1.down = False

    elif keys[pygame.K_RIGHT] and p1.x < 1440 - p1.width - p1.vel:
        p1.x += p1.vel
        p1.left = False
        p1.right = True
        p1.up = False
        p1.down = False

    # Y COORDINATE ARROW PRESSES
    elif keys[pygame.K_UP] and p1.y > p1.vel:
        p1.y -= p1.vel
        p1.up = True
        p1.down = False
        p1.left = False
        p1.right = False

        # ******
        # what i want to happen is when the up arrow key is released it will show
        # the players back. but i can't seem to figure out how to do that. currently it just goes back
        # to the players front facing position. the players backs connected to the char_back variable.
        # you can see above in asterisks idle positions that hold both the front and back facing variables.
        # what i thought could work is a while loop where it detects the up arrow key release
        # making LB (looking back) = True and then while true it would display the players back. once the walkCount
        # was greater than or = to 1 the loop would break. any help is greatly appreciated.


    elif keys[pygame.K_DOWN] and p1.y < 800 - p1.vel - p1.width:
        p1.y += p1.vel
        p1.up = False
        p1.left = False
        p1.right = False
        p1.down = True

    else:
        p1.up = False
        p1.down = False
        p1.left = False
        p1.right = False
        p1.walkCount = 0

    # JUMP MOVEMENT/ARROW PRESS

    if not p1.isJump:
        if keys[pygame.K_SPACE]:
            p1.isJump = True
            p1.walkCount = 0
    else:
        if p1.jumpCount >= -10:
            p1.y -= (p1.jumpCount * abs(p1.jumpCount)) * 0.1
            p1.jumpCount -= 1
        else:
            p1.jumpCount = 10
            p1.isJump = False

    redrawGameWindow()

pygame.quit()
