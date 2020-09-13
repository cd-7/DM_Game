import pygame
import random

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
bg = pygame.image.load('BGMazes/maze-(1).png')
char = pygame.image.load('NinjaSprite/Standing.png')
char_back = pygame.image.load('NinjaSprite/Back.png')
clock = pygame.time.Clock()


class player (object):
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


    def draw(self, win):
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
    if keys[pygame.K_LEFT] and p1.x > p1.vel + 35:
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
    else:
        if p1.jumpCount >= -10:
            p1.y -= (p1.jumpCount * abs(p1.jumpCount)) * 0.1
            p1.jumpCount -= 1
        else:
            p1.jumpCount = 10
            p1.isJump = False

    redrawGameWindow()

pygame.quit()
