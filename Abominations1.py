import pygame
from pygame.locals import *
from time import sleep
pygame.init()

screenWidth = 3340
screenHeight = 1660

window = pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("Abominations")

walkUp = [pygame.image.load('Assets/charUp1.png'),pygame.image.load('Assets/charUp2.png'),pygame.image.load('Assets/charUp3.png'),pygame.image.load('Assets/charUp4.png')]
walkDown = [pygame.image.load('Assets/charDown1.png'),pygame.image.load('Assets/charDown2.png'),pygame.image.load('Assets/charDown3.png'),pygame.image.load('Assets/charDown4.png')]
walkLeft = [pygame.image.load('Assets/charLeft1.png'),pygame.image.load('Assets/charLeft2.png'),pygame.image.load('Assets/charLeft3.png'),pygame.image.load('Assets/charLeft4.png')]
walkRight = [pygame.image.load('Assets/charRight1.png'),pygame.image.load('Assets/charRight2.png'),pygame.image.load('Assets/charRight3.png'),pygame.image.load('Assets/charRight4.png')]

office = pygame.image.load('Assets/Office.png')
office = pygame.transform.scale(office, (screenWidth-500, screenHeight-250))

freezer = pygame.image.load('Assets/Freezer.png')
freezer = pygame.transform.scale(freezer, (screenWidth-2340, screenHeight-660))

battle = pygame.image.load('Assets/Battle.png')
battle = pygame.transform.scale(battle, (screenWidth-500, screenHeight-250))

officeTextBox = pygame.image.load('Assets/Office TextBox.png')
officeTextBox = pygame.transform.scale(officeTextBox, (screenWidth-600, screenHeight-1300))

battleTextBox = pygame.image.load('Assets/Battle TextBox.png')
battleTextBox = pygame.transform.scale(officeTextBox, (screenWidth-500, screenHeight-1250))

scientist = pygame.image.load('Assets/scientist.png')

standardBattleTheme = pygame.mixer.Sound('Assets/[ONTIVA.COM]-Pokemon FireRed_LeafGreen Music- Trainer Battle-128K.wav')
pokeCenterTheme = pygame.mixer.Sound('Assets/[ONTIVA.COM]-Pokémon Center_Poké Mart [Pokémon FireRed & LeafGreen]-128K.wav')

mouseLegsPic = pygame.image.load('Assets/Monsters/MouseLegs.png')
mouseTorsoPic = pygame.image.load('Assets/Monsters/MouseTorso.png')
mouseHeadPic = pygame.image.load('Assets/Monsters/MouseHead.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.left =False
        self.right = False
        self.up = False
        self.down = False
        self.faceLeft = False
        self.faceRight = False
        self. faceUp = False
        self. faceDown = True
        self.walkCount = 0
        
    def charDraw(self,surface):
        if self.walkCount + 1 >= 32:
            self.walkCount = 0

        if self.left:
            surface.blit(walkLeft[self.walkCount%4], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            surface.blit(walkRight[self.walkCount%4], (self.x,self.y))
            self.walkCount += 1
        elif self.up:
            surface.blit(walkUp[self.walkCount%4], (self.x,self.y))
            self.walkCount += 1
        elif self.down:
            surface.blit(walkDown[self.walkCount%4], (self.x,self.y))
            self.walkCount += 1
        else:
            if self.faceLeft:
                surface.blit(walkLeft[0], (self.x,self.y))
            elif self.faceRight:
                surface.blit(walkRight[0], (self.x,self.y))
            elif self.faceUp:
                surface.blit(walkUp[0], (self.x,self.y))
            elif self.faceDown:
                surface.blit(walkDown[0], (self.x,self.y))
                
infoMove1 = ['Move 1', '15 MP', 'Description of Move 1']
infoMove2 = ['Move 2', '15 MP', 'Description of Move 2']
infoMove3 = ['Move 3', '15 MP', 'Description of Move 3']
infoMove4 = ['Move 4', '15 MP', 'Description of Move 4']

bigFont = pygame.font.SysFont('Agency FB', 100)
smallFont = pygame.font.SysFont('Agency FB', 60)
    
def dialogueFunction(surface, textDialogue,textButton1, textButton2):
    global dialogue
    while dialogue:
        surface.blit(officeTextBox, (275,1147))
        dialogueText = bigFont.render(textDialogue, 1, (0,0,0))
        buttonText1 = smallFont.render(textButton1, 1, (0,0,0))
        buttonText2 = smallFont.render(textButton2, 1, (0,0,0))
        surface.blit(dialogueText, (300, 1285))
        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect(2670, 1220, 200, 100)
        button2 = pygame.Rect(2670, 1350, 200, 100)
        border1 = pygame.Rect(2675, 1225, 190,90)
        border2 = pygame.Rect(2675, 1355, 190, 90)

        if button1.collidepoint((mx, my)):
            if click:
                dialogue = False
                overWorld = False
                inBattle = True
                inBattleFunction(window)
        if button2.collidepoint((mx, my)):
            if click:
                dialogue = False
                
        pygame.draw.rect(surface, (0,0,0), button1)
        pygame.draw.rect(surface, (0,0,0), button2)
        pygame.draw.rect(surface, (255,255,255), border1)
        pygame.draw.rect(surface, (255,255,255), border2)
        surface.blit(buttonText1, (2730, 1230))
        surface.blit(buttonText2, (2730, 1360))
        
        click = False
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        
def redrawBattleWindow(surface):
    surface.blit(battle, (250,110))
    pygame.display.update()

    
def inBattleFunction(surface):
    global inBattle
    global run
    redrawBattleWindow(surface)
    pokeCenterTheme.stop()
    standardBattleTheme.play()
    while inBattle == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                inBattle = False
                
        moveText1 = smallFont.render(infoMove1[0], 1, (0,0,0))
        moveText2 = smallFont.render(infoMove2[0], 1, (0,0,0))
        moveText3 = smallFont.render(infoMove3[0], 1, (0,0,0))
        moveText4 = smallFont.render(infoMove4[0], 1, (0,0,0))
        move1MP = smallFont.render(infoMove1[1], 1, (0,0,0))
        move2MP = smallFont.render(infoMove2[1], 1, (0,0,0))
        move3MP = smallFont.render(infoMove3[1], 1, (0,0,0))
        move4MP = smallFont.render(infoMove4[1], 1, (0,0,0))
        move1description = smallFont.render(infoMove1[2], 1, (0,0,0))
        move2description = smallFont.render(infoMove2[2], 1, (0,0,0))
        move3description = smallFont.render(infoMove3[2], 1, (0,0,0))
        move4description = smallFont.render(infoMove4[2], 1, (0,0,0))
        moveTextYes = smallFont.render('Yes', 1, (0,0,0))
        moveTextNo = smallFont.render('No', 1, (0,0,0))
        
        mMoveScreenx, mMoveScreeny = pygame.mouse.get_pos()
        
        buttonMove1 = pygame.Rect(600, 1160, 600, 150)
        buttonMove2 = pygame.Rect(600, 1320, 600, 150)
        buttonMove3 = pygame.Rect(1500, 1160, 600, 150)
        buttonMove4 = pygame.Rect(1500, 1320, 600, 150)
        buttonYes = pygame.Rect(2670, 1220, 200, 100)
        buttonNo = pygame.Rect(2670, 1350, 200, 100)
        
        border1 = pygame.Rect(605, 1165, 590,140)
        border2 = pygame.Rect(605, 1325, 590, 140)
        border3 = pygame.Rect(1505, 1165, 590,140)
        border4 = pygame.Rect(1505, 1325, 590, 140)
        borderYes = pygame.Rect(2675, 1225, 190,90)
        borderNo = pygame.Rect(2675, 1355, 190, 90)

        if buttonMove1.collidepoint((mMoveScreenx, mMoveScreeny)):
            if click:
                inMove1 = True
                while inMove1:
                    surface.blit(battleTextBox, (250,1120))
                    mMove1x, mMove1y = pygame.mouse.get_pos()
                    
                    if buttonYes.collidepoint((mMove1x, mMove1y)):
                        if click:
                            pygame.draw.rect(surface, (255,0,0), (500, 500, 500 ,500))
                    if buttonNo.collidepoint((mMove1x, mMove1y)):
                        if click:
                            inMove1 = False
                    
                    pygame.draw.rect(surface, (0,0,0), buttonYes)
                    pygame.draw.rect(surface, (0,0,0), buttonNo)
                    pygame.draw.rect(surface, (255,255,255), borderYes)
                    pygame.draw.rect(surface, (255,255,255), borderNo)
                    surface.blit(moveTextYes, (2730, 1230))
                    surface.blit(moveTextNo, (2730, 1360))
                    surface.blit(moveText1, (560, 1150))
                    surface.blit(move1MP, (960, 1150))
                    surface.blit(move1description, (560, 1350))
                    
                    click = False
        
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                    pygame.display.update()

        if buttonMove2.collidepoint((mMoveScreenx, mMoveScreeny)):
            if click:
                inMove2 = True
                while inMove2:
                    surface.blit(battleTextBox, (250,1120))
                    mMove2x, mMove2y = pygame.mouse.get_pos()
                    
                    if buttonYes.collidepoint((mMove2x, mMove2y)):
                        if click:
                            pygame.draw.rect(surface, (255,0,0), (500, 500, 500 ,500))
                    if buttonNo.collidepoint((mMove2x, mMove2y)):
                        if click:
                            inMove2 = False
                    
                    pygame.draw.rect(surface, (0,0,0), buttonYes)
                    pygame.draw.rect(surface, (0,0,0), buttonNo)
                    pygame.draw.rect(surface, (255,255,255), borderYes)
                    pygame.draw.rect(surface, (255,255,255), borderNo)
                    surface.blit(moveTextYes, (2730, 1230))
                    surface.blit(moveTextNo, (2730, 1360))
                    surface.blit(moveText2, (560, 1150))
                    surface.blit(move2MP, (960, 1150))
                    surface.blit(move2description, (560, 1350))
                    
                    click = False
        
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                    pygame.display.update()
                    
        if buttonMove3.collidepoint((mMoveScreenx, mMoveScreeny)):
            if click:
                inMove3 = True
                while inMove3:
                    surface.blit(battleTextBox, (250,1120))
                    mMove3x, mMove3y = pygame.mouse.get_pos()
                    
                    if buttonYes.collidepoint((mMove3x, mMove3y)):
                        if click:
                            pygame.draw.rect(surface, (255,0,0), (500, 500, 500 ,500))
                    if buttonNo.collidepoint((mMove3x, mMove3y)):
                        if click:
                            inMove3 = False
                    
                    pygame.draw.rect(surface, (0,0,0), buttonYes)
                    pygame.draw.rect(surface, (0,0,0), buttonNo)
                    pygame.draw.rect(surface, (255,255,255), borderYes)
                    pygame.draw.rect(surface, (255,255,255), borderNo)
                    surface.blit(moveTextYes, (2730, 1230))
                    surface.blit(moveTextNo, (2730, 1360))
                    surface.blit(moveText3, (560, 1150))
                    surface.blit(move3MP, (960, 1150))
                    surface.blit(move3description, (560, 1350))
                    
                    click = False
        
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                    pygame.display.update()                                
        if buttonMove4.collidepoint((mMoveScreenx, mMoveScreeny)):
            if click:
                inMove4 = True
                while inMove4:
                    surface.blit(battleTextBox, (250,1120))
                    mMove4x, mMove4y = pygame.mouse.get_pos()
                    
                    if buttonYes.collidepoint((mMove4x, mMove4y)):
                        if click:
                            pygame.draw.rect(surface, (255,0,0), (500, 500, 500 ,500))
                    if buttonNo.collidepoint((mMove4x, mMove4y)):
                        if click:
                            inMove4 = False
                    
                    pygame.draw.rect(surface, (0,0,0), buttonYes)
                    pygame.draw.rect(surface, (0,0,0), buttonNo)
                    pygame.draw.rect(surface, (255,255,255), borderYes)
                    pygame.draw.rect(surface, (255,255,255), borderNo)
                    surface.blit(moveTextYes, (2730, 1230))
                    surface.blit(moveTextNo, (2730, 1360))
                    surface.blit(moveText4, (560, 1150))
                    surface.blit(move4MP, (960, 1150))
                    surface.blit(move4description, (560, 1350))
                    
                    click = False
        
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True                
                    pygame.display.update()
        
        surface.blit(battleTextBox, (250,1120))            
        pygame.draw.rect(surface, (0,0,0), buttonMove1)
        pygame.draw.rect(surface, (0,0,0), buttonMove2)
        pygame.draw.rect(surface, (0,0,0), buttonMove3)
        pygame.draw.rect(surface, (0,0,0), buttonMove4)
        pygame.draw.rect(surface, (255,255,255), border1)
        pygame.draw.rect(surface, (255,255,255), border2)
        pygame.draw.rect(surface, (255,255,255), border3)
        pygame.draw.rect(surface, (255,255,255), border4)
        surface.blit(moveText1, (660, 1190))
        surface.blit(moveText2, (660, 1350))
        surface.blit(moveText3, (1560, 1190))
        surface.blit(moveText4, (1560, 1350))
        
        surface.blit(mouseLegsPic, (500, 700))
        surface.blit(mouseTorsoPic, (763, 700))
        surface.blit(mouseHeadPic, (918, 700))
        click = False
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        
def inOfficeFunction(surface):
    pokeCenterTheme.stop()
    pokeCenterTheme.play()
    global run
    global overWorld
    global inFreezer
    global inBattle
    global dialogue
    global click
    global char
    while overWorld:
        clock.tick(10)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                overWorld = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and char.x > 250:
            char.x -= char.vel
            char.left = True
            char.right = False
            char.up = False
            char.down = False
            char.faceLeft = True
            char.faceRight = False
            char. faceUp = False
            char. faceDown = False
        elif keys[pygame.K_RIGHT] and char.x < 3080 - char.vel - char.width:
            char.x += char.vel
            char.left = False
            char.right = True
            char.up = False
            char.down = False
            char.faceLeft = False
            char.faceRight = True
            char. faceUp = False
            char. faceDown = False
        elif keys[pygame.K_UP] and char.y > 110 + char.vel:
            char.y -= char.vel
            char.left = False
            char.right = False
            char.up = True
            char.down = False
            char.faceLeft = False
            char.faceRight = False
            char. faceUp = True
            char. faceDown = False
        elif keys[pygame.K_DOWN] and char.y < 1500 - char.height:
            char.y += char.vel
            char.left = False
            char.right = False
            char.up = False
            char.down = True
            char.faceLeft = False
            char.faceRight = False
            char.faceUp = False
            char.faceDown = True
        elif keys[pygame.K_SPACE] and char.x < 1150 and char.x > 950 and char.y < 700 and char.y > 500:
            dialogue = True
            dialogueFunction(window, 'Ayy Im Italian baby, you wanna tustle wid dis muscle?', 'Yes', 'No')
        elif char.x > 200 and char.x < 400 and char.y > 550 and char.y < 840 and inFreezer == False:
            inFreezer = True
            overWorld = False
            inFreezerFunction(window)

        else:
            char.left = False
            char.right = False
            char.up = False
            char.down = False
            
        surface.blit(office, (250,110))
        char.charDraw(surface)
        surface.blit(scientist, (1000,600))
        pygame.display.update()
    
def inFreezerFunction(surface):
    pokeCenterTheme.stop()
    pokeCenterTheme.play()
    global run
    global overWorld
    global inFreezer
    global char
    global char
    while inFreezer:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                inFreezer = False
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and char.x > 700 + char.vel + 100:
            char.x -= char.vel
            char.left = True
            char.right = False
            char.up = False
            char.down = False
            char.faceLeft = True
            char.faceRight = False
            char. faceUp = False
            char. faceDown = False
        elif keys[pygame.K_RIGHT] and char.x < 1700 - char.width - char.vel:
            char.x += char.vel
            char.left = False
            char.right = True
            char.up = False
            char.down = False
            char.faceLeft = False
            char.faceRight = True
            char. faceUp = False
            char. faceDown = False
        elif keys[pygame.K_UP] and char.y > 350 + char.vel + 100:
            char.y -= char.vel
            char.left = False
            char.right = False
            char.up = True
            char.down = False
            char.faceLeft = False
            char.faceRight = False
            char. faceUp = True
            char. faceDown = False
        elif keys[pygame.K_DOWN] and char.y < 1350 - char.height - char.vel - 130:
            char.y += char.vel
            char.left = False
            char.right = False
            char.up = False
            char.down = True
            char.faceLeft = False
            char.faceRight = False
            char. faceUp = False
            char. faceDown = True
        elif char.x < 1700 and char.x > 1550 and char.y > 700 and char.y < 900 and overWorld == False:
            inFreezer = False
            overWorld = True
            inOfficeFunction(window)
        elif char.x < 700 and inFreezer == True:
            char.x = 1500
        else:
            char.left = False
            char.right = False
            char.up = False
            char.down = False
        surface.fill((0,0,0))
        surface.blit(freezer, (700,350))
        char.charDraw(surface)
        pygame.display.update()
        
char = player(700, 1400, 73, 100, 75)

run = True
overWorld = True
inFreezer = False
inBattle = True
dialogue = False
click = False

def mainGame(surface):
    global run
    global overWorld
    global inFreezer
    global inBattle
    global dialogue
    global click


    while run:
        clock.tick(10)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        while overWorld:
            inOfficeFunction(window)
    pygame.quit()
mainGame(window)