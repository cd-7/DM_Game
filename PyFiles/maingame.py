import pygame
pygame.init()
###########################################################
#START MENU:


###########################################################
#MAZE:

WH = 800
WW = 1440
HWH = WH / 2
HWW = WW / 2
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
walkUp = [pygame.image.load('NinjaSprite/U1.png'),
          pygame.image.load('NinjaSprite/U2.png'),
          pygame.image.load('NinjaSprite/U3.png'),
          pygame.image.load('NinjaSprite/U4.png')]

walkDown = [pygame.image.load('NinjaSprite/D1.png'),
            pygame.image.load('NinjaSprite/D2.png'),
            pygame.image.load('NinjaSprite/D3.png'),
            pygame.image.load('NinjaSprite/D4.png')]
jumpRight = pygame.image.load('NinjaSprite/RJ.png')
jumpLeft = pygame.image.load('NinjaSprite/LJ.png')
jumpUp = pygame.image.load('NinjaSprite/UJ.png')
jumpUp2 = pygame.image.load('NinjaSprite/UJ_2.png')
jumpDown = pygame.image.load('NinjaSprite/DJ.png')
bg = pygame.image.load('BGMazes/bg.png')
char = pygame.image.load('NinjaSprite/Standing.png')
char_back = pygame.image.load('NinjaSprite/Back.png')
clock = pygame.time.Clock()
wall_img = pygame.image.load('BGMazes/wall.png')
walls = []
bgWidth, bgHeight = bg.get_rect().size
stageWidth = bgWidth
stage_x = 0
stage_y = 0
startScrolling_x = HWW
bg_x = 0
bg_y = 0



class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.back = 0
        self.hitbox = (self.x + 16, self.y + 28, 32, 35)

    def movement(self, win):
        if self.walkCount + 1 >= 8:
            self.walkCount = 0
        if self.walkCount >= 1:
            self.back = 0

        # Y COORDINATE MOVES
        if self.up and not self.isJump:
            win.blit(walkUp[self.walkCount // 2], (round(self.x), round(self.y)))
            self.walkCount += 1
            self.back += 1
        elif self.down and not self.isJump:
            win.blit(walkDown[self.walkCount // 2], (round(self.x), round(self.y)))
            self.walkCount += 1

        # X COORDINATE MOVES
        elif self.left and not self.isJump:
            win.blit(walkLeft[self.walkCount // 2], (round(self.x), round(self.y)))
            self.walkCount += 1
        elif self.right and not self.isJump:
            win.blit(walkRight[self.walkCount // 2], (round(self.x), round(self.y)))
            self.walkCount += 1

        # IDLE POSITIONS
        else:
            if not self.isJump:
                if self.back >= 1:
                    win.blit(char_back, (round(self.x), round(self.y)))
                else:
                    win.blit(char, (round(self.x), round(self.y)))
        self.hitbox = (self.x + 16, self.y + 28, 32, 35)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        # JUMPING
        if self.isJump:
            if self.up:
                win.blit(jumpUp, (round(self.x), round(self.y)))
                self.back += 1
            elif self.down:
                win.blit(jumpDown, (round(self.x), round(self.y)))
                self.back = 0
            elif self.left:
                win.blit(jumpLeft, (round(self.x), round(self.y)))
                self.back = 0
            elif self.right:
                win.blit(jumpRight, (round(self.x), round(self.y)))
                self.back = 0
            else:
                if self.back >= 1:
                    win.blit(char_back, (round(self.x), round(self.y)))
                else:
                    win.blit(char, (round(self.x), round(self.y)))
                    self.back = 0


def redrawGameWindow():

    p1.movement(win)
    pygame.display.update()

# MAINLOOP
spawn_x = 49
spawn_y = 80
p1 = player(spawn_x, spawn_y, 64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    player_x = p1.x

    # X COORDINATE ARROW PRESSES
    if keys[pygame.K_LEFT] and p1.x > p1.vel + 35:
        p1.x += - p1.vel
        if p1.x > 0 and bg_x != 0:
            p1.x = HWW
            bg_x += p1.vel
        p1.left = True
        p1.right = False
        p1.up = False
        p1.down = False

    elif keys[pygame.K_RIGHT] and p1.x < 1440 - p1.width:
        p1.x += p1.vel
        if p1.x >= HWW:
            p1.x = HWW
            if stage_x >= 5:
                bg_x = 100
                stage_x = 5
                p1.x = p1.x
            else:
                bg_x -= p1.vel
                stage_x -= p1.vel
        p1.left = False
        p1.right = True
        p1.up = False
        p1.down = False

    # Y COORDINATE ARROW PRESSES
    elif keys[pygame.K_UP] and p1.y > p1.vel:
        p1.y -= p1.vel
        if bg_y < 0:
            p1.y = HWH
            bg_y += p1.vel
        p1.up = True
        p1.down = False
        p1.left = False
        p1.right = False

    elif keys[pygame.K_DOWN] and p1.y < 800 - p1.vel - p1.width:
        p1.y += p1.vel
        if p1.y >= HWH:
            p1.y = HWH
            bg_y -= p1.vel
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
    else:
        if p1.jumpCount >= -10:
            p1.y -= (p1.jumpCount * abs(p1.jumpCount)) * 0.1
            p1.jumpCount -= 1
        else:
            p1.jumpCount = 10
            p1.isJump = False

    win.blit(bg, (bg_x, bg_y))

    redrawGameWindow()

pygame.quit()
