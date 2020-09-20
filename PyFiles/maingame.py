import pygame
pygame.init()


WH = 800
WW = 1440
HWH = WH / 2
HWW = WW / 2
wn_size = (1440, 800)
win = pygame.display.set_mode(wn_size)
pygame.display.set_caption("Devil's Maze")

walkRight = [pygame.image.load('Images/NinjaSprite/R1.png'),
             pygame.image.load('Images/NinjaSprite/R2.png'),
             pygame.image.load('Images/NinjaSprite/R3.png'),
             pygame.image.load('Images/NinjaSprite/R4.png')]
walkLeft = [pygame.image.load('Images/NinjaSprite/L1.png'),
            pygame.image.load('Images/NinjaSprite/L2.png'),
            pygame.image.load('Images/NinjaSprite/L3.png'),
            pygame.image.load('Images/NinjaSprite/L4.png')]
walkUp = [pygame.image.load('Images/NinjaSprite/U1.png'),
          pygame.image.load('Images/NinjaSprite/U2.png'),
          pygame.image.load('Images/NinjaSprite/U3.png'),
          pygame.image.load('Images/NinjaSprite/U4.png')]
walkDown = [pygame.image.load('Images/NinjaSprite/D1.png'),
            pygame.image.load('Images/NinjaSprite/D2.png'),
            pygame.image.load('Images/NinjaSprite/D3.png'),
            pygame.image.load('Images/NinjaSprite/D4.png')]
jumpRight = pygame.image.load('Images/NinjaSprite/RJ.png')
jumpLeft = pygame.image.load('Images/NinjaSprite/LJ.png')
jumpUp = pygame.image.load('Images/NinjaSprite/UJ.png')
jumpUp2 = pygame.image.load('Images/NinjaSprite/UJ_2.png')
jumpDown = pygame.image.load('Images/NinjaSprite/DJ.png')
bg = pygame.image.load('Images/BGMazes/bg.png')
char = pygame.image.load('Images/NinjaSprite/Standing.png')
char_back = pygame.image.load('Images/NinjaSprite/Back.png')
clock = pygame.time.Clock()
wall_img = pygame.image.load('Images/BGMazes/wall.png')
walls = []
bg_x = 0
bg_y = 0


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
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
    if keys[pygame.K_LEFT] and p1.x > p1.vel + 27:
        p1.x += - p1.vel
        if p1.x > 0 and bg_x != 0 and p1.x <= HWW:
            p1.x = HWW
            bg_x += p1.vel
        p1.left = True
        p1.right = False
        p1.up = False
        p1.down = False

    elif keys[pygame.K_RIGHT] and p1.x < 1380:
        p1.x += p1.vel
        if bg_x >= -355:
            if p1.x >= HWW:
                p1.x = HWW
                bg_x -= p1.vel


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

    elif keys[pygame.K_DOWN] and p1.y < 650:
        p1.y += p1.vel
        if p1.y >= HWH and bg_y >= -240:
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