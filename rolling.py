import pygame
pygame.init()
win = pygame.display.set_mode((1000,700))
pygame.display.set_caption("First Game")
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('mrt1000x700.png')
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()
class player(object):
    def __init__(self,x,y,width,height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                
class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
    def draw(self,win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        
def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    goblin.draw(win)

    arr = []
    x = 270
    y = 300
    for i in range (0,7):
        arr[i] = seat(x, y)


    red = (250, 0, 0)
    box1 = pygame.draw.rect(win, red, (270, 300, 50, 60), 2)
    box2 = pygame.draw.rect(win, red, (325, 300, 50, 60), 2)

    pygame.display.update()

class seat(x, y):
    vacancy = True
    #centre = [x, y]
    

#mainloop
man = player(200, 410, 64,64, 10)
goblin = enemy(100, 410, 64, 64, 1000)

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if ((240 < man.x < 350) and (270 < man.y < 390)): #get a seat
        vacancy = False
        man.vel = 0   
        
        if keys[pygame.K_SPACE]:
            if man.left:
                facing = -1
            else:
                facing = 1

        
        

        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT] and man.x < 1000 - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
        elif keys[pygame.K_UP] and man.y > man.vel + 60:
            man.y -= man.vel
        elif keys[pygame.K_DOWN] and man.y < 700 - man.height - man.vel:
            if man.x > 700 and man.x < 800 and man.y == 300:
                man.y += man.vel
            elif man.x > 110 and man.x < 230 and man.y == 300:
                man.y += man.vel
            elif man.y == 300:
                man.y += 0
            else:
                man.y += man.vel

        else:
            man.standing = True
            man.walkCount = 0
        
                
        redrawGameWindow()
pygame.quit()