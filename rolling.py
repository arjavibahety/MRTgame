import pygame
pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

x = 50
y = 400
width = 40
height = 60
vel = 10

clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char, (self.x,self.y))

#isJump = False
#jumpCount = 10

left = False
right = False
walkCount = 0
 
def redrawGameWindow():
    win.blit(bg, (0,0))  
    man.draw(win)
        
    pygame.display.update() 
    
#mainloop
man = player(200, 410, 64, 64)
run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False

    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    
    elif keys[pygame.K_UP] and man.y > man.vel:
          man.y -= man.vel

    elif keys[pygame.K_DOWN] and man.y < 500 - man.height - man.vel:
           man.y += man.vel
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        
    #if not(isJump):
    #    if keys[pygame.K_SPACE]:
            #isJump = True
    #        left = False
    #        right = False
    #       walkCount = 0
    #else:
    #    if jumpCount >= -10:
    #        y -= (jumpCount * abs(jumpCount)) * 0.5
    #        jumpCount -= 1
    #    else: 
    #        jumpCount = 10
    #        isJump = False

    redrawGameWindow() 
    
    
pygame.quit()