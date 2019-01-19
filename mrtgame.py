import pygame

pygame.init()

win = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("First Game")
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load(
   'R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load(
   'L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('mrt1000x700.png')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()


class player(object):
   def __init__(self, x, y, width, height):
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.vel = 10
       self.isJump = False
       self.left = False
       self.right = False
       self.walkCount = 0
       self.jumpCount = 10
       self.hitbox = (self.x + 10, self.y + 11, 45, 52)

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

       self.hitbox = (self.x + 10, self.y + 11, 45, 52)
       pygame.draw.rect(win, (250, 0, 0), self.hitbox, 2)


#isJump = False
#jumpCount = 10
left = False
right = False
walkCount = 0
red = (250, 0, 0)


def redrawGameWindow():
   win.blit(bg, (0, 0))
   man.draw(win)
   pygame.draw.rect(win, red, (270, 300, 50, 60), 2)
   pygame.draw.rect(win, red, (330, 300, 50, 60), 2)
   pygame.draw.rect(win, red, (390, 300, 50, 60), 2)
   pygame.draw.rect(win, red, (450, 300, 50, 60), 2)
   pygame.draw.rect(win, red, (505, 300, 50, 60), 2)
   pygame.draw.rect(win, red, (560, 300, 50, 60), 2)
   pygame.display.update()


# mainloop
man = player(450, 600, 64, 64)

run = True
while run:
   clock.tick(27)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
   keys = pygame.key.get_pressed()

   if keys[pygame.K_LEFT] and man.x > -10:
       if 0 < man.y < 140 and man.x == 120:
           man.x -= 0
       elif 0 < man.y < 140 and man.x == 260:
           man.x -= 0
       elif 0 < man.y < 140 and man.x == 740:
           man.x -= 0
       elif 0 < man.y < 140 and man.x == 880:
           man.x -= 0
       elif 230 < man.y < 350 and man.x == 120:
           man.x -= 0
       elif 230 < man.y < 350 and man.x == 260:
           man.x -= 0
       elif 230 < man.y < 350 and man.x == 740:
           man.x -= 0
       elif 230 < man.y < 350 and man.x == 880:           
           man.x -= 0
       else:
           man.x -= man.vel
           man.left = True
           man.right = False

   elif keys[pygame.K_RIGHT] and man.x < 1009 - man.width:
        if 0 < man.y < 140 and man.x == 70:
           man.x -= 0
        elif 0 < man.y < 140 and man.x == 210:
           man.x -= 0
        elif 0 < man.y < 140 and man.x == 690:
           man.x -= 0
        elif 0 < man.y < 140 and man.x == 820:
           man.x -= 0
        elif 230 < man.y < 350 and man.x == 70:
           man.x -= 0
        elif 230 < man.y < 350 and man.x == 210:
           man.x -= 0
        elif 230 < man.y < 350 and man.x == 690:
           man.x -= 0
        elif 230 < man.y < 350 and man.x == 820:           
           man.x -= 0
        else:
           man.x += man.vel
           man.left = True
           man.right = False

   elif keys[pygame.K_UP] and man.y > man.vel + 60:
       if man.y == 140 and (70 < man.x < 120 or 210 < man.x < 260 or 690 < man.x < 740 or 820 < man.x < 880):
           man.y -= 0
       elif man.y != 350 or 110 < man.x < 210 or 720 < man.x < 830:
           man.y -= man.vel

   elif keys[pygame.K_DOWN] and man.y < 700 - man.height - man.vel:
       if man.y == 230 and (70 < man.x < 120 or 210 < man.x < 260 or 690 < man.x < 740 or 820 < man.x < 880):
           man.y += 0       
       elif man.y != 300 or 110 < man.x < 210 or 720 < man.x < 830:
           man.y += man.vel

   else:
       man.right = False
       man.left = False
       man.walkCount = 0

   # if not(isJump):
   #    if keys[pygame.K_SPACE]:
       #isJump = True
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



Collapse