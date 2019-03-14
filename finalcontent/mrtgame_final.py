import pygame
import random
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

sound = pygame.mixer.Sound("mrtsong.wav")
pygame.mixer.Sound.play(sound)


win = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("First Game")
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load(
    'R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load(
    'L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]


walkRightE = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load(
   'R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]
walkLeftE = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load(
   'L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]
charE = pygame.image.load('standingE.png')

bg = pygame.image.load('trainToBushan.png')
char = pygame.image.load('standing.png')
ss = pygame.image.load("start.png")

clock = pygame.time.Clock()


smallfont = pygame.font.SysFont("copperplate", 35)
medfont = pygame.font.SysFont("copperplate", 50)
largefont = pygame.font.SysFont("copperplate", 80)


def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        # win.fill(green)

        redrawStart()
        message_to_screen("Welcome on Board!",
                            red,
                            -300,
                            "large")
        message_to_screen("The objective of the game is to find a seat",
                            black,
                            -250)
        message_to_screen("Press S to play or Q to quit",
                            black,
                            180)

        pygame.display.update()
        clock.tick(15)


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
       if self.walkCount + 1 >= 27:
           self.walkCount = 0

       if self.left:
           win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
           self.walkCount += 1
       elif self.right:
           win.blit(walkRight[self.walkCount//3], (self.x, self.y))
           self.walkCount += 1
       else:
           win.blit(char, (self.x, self.y))

           self.hitbox = (self.x + 17, self.y + 11, 29, 52)

class enemy(object):

   def __init__(self, x, y, width, height, endx, endy, queue):
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.endx = endx
       self.endy = endy
       self.queue = queue
       self.path = [self.endx, self.endy]
       self.left = False
       self.right = True
       self.ended = False
       self.walkCount = 0
       self.vel = 5
       self.hitbox = (self.x + 17, self.y + 2, 31, 57)
       self.desig = False

   def move(self):

       if not self.desig:
           moveToDesignated(self)

       else:
           randMove(self)

   def draw(self, win):

       if not self.ended:
           self.move()

       if self.ended:
           win.blit(charE, (self.x, self.y))
           self.walkCount = 0

       if self.walkCount + 1 >= 27:
           self.walkCount = 0
       if self.left:
           win.blit(walkLeftE[self.walkCount//3], (self.x, self.y))
           self.walkCount += 1
       elif self.right:
           win.blit(walkRightE[self.walkCount//3], (self.x, self.y))
           self.walkCount += 1
       else:
           win.blit(charE, (self.x, self.y))
           self.walkCount = 0

       self.hitbox = (self.x + 17, self.y + 2, 31, 57)
           #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)




def moveToDesignated(self):
   if self.queue == "L1":
       #print("L1")
       while self.x < 150:
           self.x += self.vel
           self.left = False
           self.right = True
       while self.y > 200:
           self.y -= self.vel
       self.desig = True

   elif self.queue == "R1":
       #print("R1")
       while self.x > 180:
           self.x -= self.vel
           self.left = True
           self.right = False

       while self.y > 200:
           self.y -= self.vel
       self.desig = True

   elif self.queue == "L2":
       while self.x < 750:
           self.x += self.vel
           self.left = False
           self.right = True
       while self.y > 200:
           self.y -= self.vel
       self.desig = True

   elif self.queue == "R2":
       while self.x > 750:
           self.x -= self.vel
           self.left = True
           self.right = False
       while self.y > 200:
           self.y -= self.vel
       self.desig = True

# counter = 0

def randMove(self):
   # if self.path[0] -20 < self.x < self.path[0] + 20 and self.path[1] - 20 < self.y < self.path[1] + 20:
   #     self.x += 0
   #     self.y += 0
   #     self.ended = True
   #     print("self.ended is true!")
   # else:
    if self.x + self.vel < self.path[0]:
        self.x += self.vel
        self.left = False
        self.right = True
    elif self.x - self.vel > self.path[0]:
        self.x -= self.vel
        self.left = True
        self.right = False
    elif self.y - self.vel > self.path[1]:
        self.y -= self.vel
    elif self.y + self.vel < self.path[1] - 30:
        self.y += self.vel
    else:
        self.x += 0
        self.y += 0
        self.vel = 0
        self.left = False
        self.right = False
        self.ended = True
        mrt.counter += 1
        # counter = counter + 1

def enemyBarriers(self):
    if (self.y == 70 or self.y == 700) or (self.x == 0 or self.x == 1000) or (0 < self.y < 140 and self.x == 120) or (0 < self.y < 140 and self.x == 260) or (0 < self.y < 140 and self.x == 740) or (0 < self.y < 140 and self.x == 880) or (230 < self.y < 350 and self.x == 120) or (230 < self.y < 350 and self.x == 260) or (230 < self.y < 350 and self.x == 740) or (230 < self.y < 350 and self.x == 880) or (0 < self.y < 140 and self.x == 70) or (0 < self.y < 140 and self.x == 210) or (0 < self.y < 140 and self.x == 690) or (0 < self.y < 140 and self.x == 820) or (230 < self.y < 350 and self.x == 70) or (230 < self.y < 350 and self.x == 210) or (230 < self.y < 350 and self.x == 690) or (230 < self.y < 350 and self.x == 820) or (self.y == 140 and (70 < self.x < 120 or 210 < self.x < 260 or 690 < self.x < 740 or 820 < self.x < 880)) or (self.y == 300 and (0 < self.x < 110 or 210 < self.x < 720 or 830 < self.x < 1000)) or (self.y == 230 and (70 < self.x < 120 or 210 < self.x < 260 or 690 < self.x < 740 or 820 < self.x < 880)) or (self.y == 300 and (0 < self.x < 110 or 210 < self.x < 720 or 830 < self.x < 1000)):
        self.vel = self.vel * -1

# what to do when there is a barrier to the left


def leftBarrier(self):
    if (0 < self.y < 140 and self.x == 120) or (0 < self.y < 140 and self.x == 260) or (0 < self.y < 140 and self.x == 740) or (0 < self.y < 140 and self.x == 880) or (230 < self.y < 350 and self.x == 120) or (230 < self.y < 350 and self.x == 260) or (230 < self.y < 350 and self.x == 740) or (230 < self.y < 350 and self.x == 880):
        self.x -= 0
    else:
        self.x -= self.vel
        self.left = True
        self.right = False

# what to do when there is a barrier to the right


def rightBarrier(self):
    if (0 < self.y < 140 and self.x == 70) or (0 < self.y < 140 and self.x == 210) or (0 < self.y < 140 and self.x == 690) or (0 < self.y < 140 and self.x == 820) or (230 < self.y < 350 and self.x == 70) or (230 < self.y < 350 and self.x == 210) or (230 < self.y < 350 and self.x == 690) or (230 < self.y < 350 and self.x == 820):
        self.x -= 0
    else:
        self.x += self.vel
        self.left = False
        self.right = True


# what to do when there is a barrier at the  top
def upBarrier(self):
    if (self.y == 140 and (70 < self.x < 120 or 210 < self.x < 260 or 690 < self.x < 740 or 820 < self.x < 880)) or (self.y == 350 and (0 < self.x < 110 or 210 < self.x < 720 or 830 < self.x < 1000)):
        self.y -= 0
    else:
        self.y -= self.vel

# what to do when there is a barrier at the bottom


def downBarrier(self):
    if (self.y == 230 and (70 < self.x < 120 or 210 < self.x < 260 or 690 < self.x < 740 or 820 < self.x < 880)) or (self.y == 300 and (0 < self.x < 110 or 210 < self.x < 720 or 830 < self.x < 1000)):
        self.y += 0
    else:
        self.y += self.vel


# isJump = False
# jumpCount = 10
left = False
right = False
walkCount = 0
red = (250, 0, 0)
screen = pygame.display.set_mode()
# winner = False

def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    for i in range(0, 24):
        goblinList[i].draw(win)

    pygame.display.update()

def redrawStart():
    win.blit(ss, (0,0))

    pygame.display.update

class train(object):
    def __init__(self):
        self.counter = 0

mrt = train()

class chair(object):
    def __init__(self, a, b, name):
        self.vacancy = True
        self.a = a
        self.b = b
        self.name = name

def text_objects(text,color,size):
    if size == "small":
        textsurface = smallfont.render(text, True, color)
    elif size == "medium":
        textsurface = medfont.render(text, True, color)
    elif size == "large":
        textsurface = largefont.render(text, True, color)


    return textsurface, textsurface.get_rect()

def message_to_screen(msg,color, y_displace=0, size = "small"):
    textsurf, textrect = text_objects(msg,color,size)
    textrect.center = (1000/2), (700/2) + y_displace
    win.blit(textsurf, textrect)

# man = player(450, 500, 64, 64)



# mainloop

man = player(450, 400, 64, 64)
goblinList = [enemy(100, 600, 64, 64, -5, 60, "L1"),
enemy(600, 600, 64, 64, 55, 60, "L2"),
enemy(300, 600, 64, 64, 266, 60, "R1"),
enemy(800, 600, 64, 64, 320, 60, "R2"),
enemy(100, 600, 64, 64, 382, 60, "L1"),
enemy(600, 600, 64, 64, 435, 60, "L2"),
enemy(300, 600, 64, 64, 502, 60, "R1"),
enemy(800, 600, 64, 64, 550, 60, "R2"),
enemy(100, 600, 64, 64, 620, 60, "L1"),
enemy(600, 600, 64, 64, 670, 60, "L2"),
enemy(300, 600, 64, 64, 880, 60, "R1"),
enemy(800, 600, 64, 64, 940, 60, "R2"),
enemy(100, 600, 64, 64, -5, 320, "L1"),
enemy(600, 600, 64, 64, 55, 320, "L2"),
enemy(300, 600, 64, 64, 266, 320, "R1"),
enemy(800, 600, 64, 64, 320, 320, "R2"),
enemy(100, 600, 64, 64, 382, 320, "L1"),
enemy(600, 600, 64, 64, 435, 320, "L2"),
enemy(300, 600, 64, 64, 502, 320, "R1"),
enemy(800, 600, 64, 64, 550, 320, "R2"),
enemy(100, 600, 64, 64, 620, 320, "L1"),
enemy(600, 600, 64, 64, 670, 320, "L2"),
enemy(300, 600, 64, 64, 880, 320, "R1"),
enemy(800, 600, 64, 64, 940, 320, "R2")]

def gameLoop():
    run = True
    while run:
        clock.tick(27)
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False
        keys = pygame.key.get_pressed()
        if mrt.counter >= 24:
            win.fill(white)
            message_to_screen("Oh No You Suck!!", red, -50, size = "large")
            message_to_screen("Try again!", black, 0, size = "medium")
            pygame.display.update()
            time.sleep(2)
            break

        # 2 seats upper left
        e = -5
        f = 60
        for i in range (2):
            chair(e, f, i)
            seat = chair(e, f, i)

            for i in range(0, 24):
                if ((e < goblinList[i].x + 20 < e + 50) and (f - 50 < goblinList[i].y - 10 < f + 10)):  # get a seat
                    seat.vacancy = False

            if ((e < man.x + 20 < e + 50) and (f - 50 < man.y - 10 < f + 10)):  # get a seat
                print(seat.name)
                seat.vacancy = False
                man.vel = 0
                run = False
                while run == False:
                    win.fill(white)
                    message_to_screen("Congrats You Won!!", red, -50, size = "large")
                    message_to_screen("Thanks for Playing!", black, 0, size = "medium")
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                run = False
                                pygame.quit()
                                quit()
                            if event.key == pygame.K_s:
                                run = True
                                gameLoop()
                break
            e += 60

        # long seats in upper row
        c = 270
        d = 60
        for i in range (9, 17):
            chair(c, d, i)
            seat = chair(c, d, i)

            for i in range(0, 24):
                if ((e < goblinList[i].x + 20 < e + 50) and (f - 50 < goblinList[i].y - 10 < f + 10)):  # get a seat
                    seat.vacancy = False

            if ((c < man.x + 20 < c + 50) and (d - 50 < man.y - 10 < d + 10)):  # get a seat
                print(seat.name)
                seat.vacancy = False
                man.vel = 0
                run = False
                while run == False:
                    win.fill(white)
                    message_to_screen("Congrats You Won!!", red, -50, size = "large")
                    message_to_screen("Thanks for Playing!", black, 0, size = "medium")
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                run = False
                                pygame.quit()
                                quit()
                            if event.key == pygame.K_s:
                                run = True
                                gameLoop()
                break
            c += 60

        # 2 seats upper right
        e = 880
        f = 60
        for i in range (2):
            chair(e, f, i)
            seat = chair(e, f, i)

            for i in range(0, 24):
                if ((e < goblinList[i].x + 20 < e + 50) and (f - 50 < goblinList[i].y - 10 < f + 10)):  # get a seat
                    seat.vacancy = False

            if ((e < man.x + 20 < e + 50) and (f - 50 < man.y - 10 < f + 10)):  # get a seat
                print(seat.name)
                seat.vacancy = False
                man.vel = 0
                run = False
                while run == False:
                    win.fill(white)
                    message_to_screen("Congrats You Won!!", red, -50, size = "large")
                    message_to_screen("Thanks for Playing!", black, 0, size = "medium")
                    pygame.display.update()

                    while run == False:
                        win.fill(white)
                        message_to_screen("Congrats You Won!!", red, -50, size = "large")
                        message_to_screen("Thanks for Playing!", black, 0, size = "medium")
                        pygame.display.update()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                    run = False
                                    pygame.quit()
                                    quit()
                                if event.key == pygame.K_s:
                                    run = True
                                    gameLoop()
                break
            e += 60

        # 2 seats lower left
        e = -5
        f = 300
        for i in range (2):
            chair(e, f, i)
            seat = chair(e, f, i)

            for i in range(0, 24):
                if ((e < goblinList[i].x + 20 < e + 50) and (f - 50 < goblinList[i].y - 10 < f + 10)):  # get a seat
                    seat.vacancy = False

            if ((e < man.x + 20 < e + 50) and (f - 50 < man.y - 10 < f + 10)):  # get a seat
                print(seat.name)
                seat.vacancy = False
                man.vel = 0
                run = False
                while run == False:
                    win.fill(white)
                    message_to_screen("Congrats You Won!!", red, -50, size = "large")
                    message_to_screen("Thanks for Playing!", black, 0, size = "medium")
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                run = False
                                pygame.quit()
                                quit()
                            if event.key == pygame.K_s:
                                run = True
                                gameLoop()

                break
            e += 60

        # long seats lower row
        a = 270
        b = 300
        for i in range (8):
            chair(a, b, i)
            seat = chair(a, b, i)

            for i in range(0, 24):
                if ((e < goblinList[i].x + 20 < e + 50) and (f - 50 < goblinList[i].y - 10 < f + 10)):  # get a seat
                    seat.vacancy = False

            if ((a < man.x + 20 < a + 50) and (b - 50 < man.y - 10 < b + 10)):  # get a seat
                print(seat.name)
                seat.vacancy = False
                man.vel = 0
                run = False
                while run == False:
                    win.fill(white)
                    message_to_screen("Congrats You Won!!", red, -50, size = "large")
                    message_to_screen("Thanks for Playing!", black, 0, size = "medium")
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                run = False
                                pygame.quit()
                                quit()
                            if event.key == pygame.K_s:
                                run = True
                                gameLoop()
                break
            a += 60

        # 2 seats lower right
        e = 880
        f = 300
        for i in range (2):
            chair(e, f, i)
            seat = chair(e, f, i)

            for i in range(0, 24):
                if ((e < goblinList[i].x + 20 < e + 50) and (f - 50 < goblinList[i].y - 10 < f + 10)):  # get a seat
                    seat.vacancy = False

            if ((e < man.x + 20 < e + 50) and (f - 50 < man.y - 10 < f + 10)):  # get a seat
                print(seat.name)
                seat.vacancy = False
                man.vel = 0
                run = False
                
                while run == False:
                    win.fill(white)
                    message_to_screen("Congrats You Won!!", red, -50, size = "large")
                    message_to_screen("Thanks for Playing!", black, 0, size = "medium")
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                run = False
                                pygame.quit()
                                quit()
                            if event.key == pygame.K_s:
                                run = True
                                gameLoop()
                break
            e += 60

        if keys[pygame.K_LEFT] and man.x > -10:
           leftBarrier(man)

        elif keys[pygame.K_RIGHT] and man.x < 1009 - man.width:
           rightBarrier(man)

        elif keys[pygame.K_UP] and man.y > man.vel + 60:
           upBarrier(man)

        elif keys[pygame.K_DOWN] and man.y < 700 - man.height - man.vel:
           downBarrier(man)
        # if not(isJump):
        #    if keys[pygame.K_SPACE]:
            # isJump = True
        #        left = False
        #        right = False
        #       walkCount = 0
        # else:
        #    if jumpCount >= -10:
        #        y -= (jumpCount * abs(jumpCount)) * 0.5
        #        jumpCount -= 1
        #    else:
        #        jumpCount = 10
        #        isJump = False
        redrawGameWindow()

    
        

    pygame.quit()
    quit()

game_intro()
gameLoop()
