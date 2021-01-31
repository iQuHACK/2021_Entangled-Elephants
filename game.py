import pygame

pygame.init()
gridWidth = 400
gridHeight = 550
screen = pygame.display.set_mode((gridWidth + 200, gridHeight))
r = 255
redPieces = pygame.sprite.Group()

class RedSoldier1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill((r,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (75, 25)

redSoldier1 = RedSoldier1()
redPieces.add(redSoldier1)

class RedSoldier2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill((r,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (125, 25)

redSoldier2 = RedSoldier2()
redPieces.add(redSoldier2)

class RedSoldier3(pygame.sprite.Sprite):
    r = 255
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill((r,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (275, 25)

redSoldier3 = RedSoldier3()
redPieces.add(redSoldier3)

class RedSoldier4(pygame.sprite.Sprite):
    r = 255
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill((r,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (325, 25)

redSoldier4 = RedSoldier4()
redPieces.add(redSoldier4)

buttons = pygame.sprite.Group()
class EntangleButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((120,20))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (500,25)

entangleButton = EntangleButton()
buttons.add(entangleButton)

class MoveButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((120,20))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (500,75)

moveButton = MoveButton()
buttons.add(moveButton)

running = True

tempSprite = RedSoldier1()
tempSprite_2 = RedSoldier1()
sprite1 = tempSprite
sprite2 = tempSprite_2

display_surface = pygame.display.set_mode((gridWidth + 200, gridHeight))

font = pygame.font.Font('freesansbold.ttf', 18)
#Entanglment button text
text_en = font.render('Entangle', True, (255,255,255))
textRect_en = text_en.get_rect()
textRect_en.center = (500, 25)

#Move button text
text_move = font.render('Move', True, (255,255,255))
textRect_move = text_move.get_rect()
textRect_move.center = (500, 75)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for sprite in redPieces:
                if sprite.rect.collidepoint(x, y):
                    if sprite1 == tempSprite:
                        sprite1 = sprite
                    elif sprite1 == sprite:
                        sprite1 = tempSprite
                    elif sprite2 == sprite:
                        sprite2 = tempSprite
                    else:
                        sprite2 = sprite
            if moveButton.rect.collidepoint(x,y):
                if sprite1 != tempSprite && sprite2 == tempSprite:
                    #check if can move to new location, if so, move the sprite
                    

    screen.fill((255, 255, 255))
    columns = 8
    rows = 11
    for x in range(columns):
        for y in range(rows):
            blockSize = gridWidth / 8
            rect = pygame.Rect(x * (blockSize), y * (blockSize), (blockSize),
                               (blockSize))
            pygame.draw.rect(screen, (0, 0, 0), rect,1)

    
    redPieces.update()
    redPieces.draw(screen)
    buttons.update()
    buttons.draw(screen)
    display_surface.blit(text_en, textRect_en)
    display_surface.blit(text_move, textRect_move)

    pygame.display.flip()

pygame.quit()

def canMove(loc1, loc2):
