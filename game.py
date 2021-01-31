import pygame

pygame.init()
gridWidth = 400
gridHeight = 550
screen = pygame.display.set_mode((gridWidth + 200, gridHeight))
r = 255
redPieces = pygame.sprite.Group()
squares = pygame.sprite.Group()

class Square1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((25,25))

square1 = Square1()
squares.add(square1)

class Square2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((75,25))

square2 = Square2()
squares.add(square2)

class Square3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((125,25))

square3 = Square3()
squares.add(square3)

class Square4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((175,25))

square4 = Square4()
squares.add(square4)

class Square5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((225,25))

square5 = Square5()
squares.add(square5)

class Square6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((275,25))

square6 = Square6()
squares.add(square6)

class Square7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((325,25))

square7 = Square7()
squares.add(square7)

class Square8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((375,25))

square8 = Square8()
squares.add(square8)

class Square9(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((25,75))

square9 = Square9()
squares.add(square9)

class Square10(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((75,75))

square10 = Square10()
squares.add(square10)

class Square11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((125,75))

square11 = Square11()
squares.add(square11)

class Square12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((175,75))

square12 = Square12()
squares.add(square12)

class Square13(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((225,75))

square13 = Square13()
squares.add(square13)

class Square14(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((275,75))

square14 = Square14()
squares.add(square14)

class Square15(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((325,75))

square15 = Square15()
squares.add(square15)

class Square16(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((375,75))

square16 = Square16()
squares.add(square16)

class Square17(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((25,125))

square17 = Square17()
squares.add(square17)

class Square18(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((75,125))

square18 = Square18()
squares.add(square18)

class Square19(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((125,175))

square19 = Square19()
squares.add(square19)

class Square20(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((175,225))

square20 = Square20()
squares.add(square20)

class Square21(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((225,125))

square21 = Square21()
squares.add(square21)

class Square22(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((275,125))

square22 = Square22()
squares.add(square22)

class Square23(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((325,125))

square23 = Square23()
squares.add(square23)

class Square24(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48,48))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((375,125))

square24 = Square24()
squares.add(square24)


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
    def updateColor(self):
        self.image.fill((140,0,0))

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
    columns = 8
    rows = 11
    screen.fill((255, 255, 255))
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
            for square in squares:
                if(square.rect.collidepoint(x, y)):
                    if sprite1 == tempSprite:
                        sprite1 = sprite
                    elif sprite1 == sprite:
                        sprite1 = tempSprite
                    elif sprite2 == sprite:
                        sprite2 = tempSprite
                    else:
                        sprite2 = sprite
            if moveButton.rect.collidepoint(x,y) and sprite1 != tempSprite and sprite2 != tempSprite:
                #check if can move to new location, if so, move the sprite
                temp = 1
    
    
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
