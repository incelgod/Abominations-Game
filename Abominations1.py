import pygame
import math
from pygame.locals import *
from time import sleep
pygame.init()

screenWidth = (pygame.display.Info().current_w)-(math.floor(.13*(pygame.display.Info().current_w)))

screenHeight = (pygame.display.Info().current_h)-(math.floor(.231*(pygame.display.Info().current_h)))

window = pygame.display.set_mode((screenWidth,screenHeight))



pygame.display.set_caption("Abominations")

walkUp = [pygame.image.load('Assets/charUp1.png'),pygame.image.load('Assets/charUp2.png'),pygame.image.load('Assets/charUp3.png'),pygame.image.load('Assets/charUp4.png')]
walkDown = [pygame.image.load('Assets/charDown1.png'),pygame.image.load('Assets/charDown2.png'),pygame.image.load('Assets/charDown3.png'),pygame.image.load('Assets/charDown4.png')]
walkLeft = [pygame.image.load('Assets/charLeft1.png'),pygame.image.load('Assets/charLeft2.png'),pygame.image.load('Assets/charLeft3.png'),pygame.image.load('Assets/charLeft4.png')]
walkRight = [pygame.image.load('Assets/charRight1.png'),pygame.image.load('Assets/charRight2.png'),pygame.image.load('Assets/charRight3.png'),pygame.image.load('Assets/charRight4.png')]

office = pygame.image.load('Assets/Office.png')
office = pygame.transform.scale(office, (screenWidth-(math.floor(.1497*(screenWidth))), screenHeight-(math.floor(.1506*(screenHeight)))))

freezer = pygame.image.load('Assets/Freezer.png')
freezer = pygame.transform.scale(freezer, (screenWidth-(math.floor(.7*(screenWidth))), screenHeight-(math.floor(.3976*(screenHeight)))))

battle = pygame.image.load('Assets/Battle.png')
battle = pygame.transform.scale(battle, (screenWidth-(math.floor(.1497*(screenWidth))), screenHeight-(math.floor(.1506*(screenHeight)))))

officeTextBox = pygame.image.load('Assets/Office TextBox.png')
officeTextBox = pygame.transform.scale(officeTextBox, (screenWidth-(math.floor(.1796*(screenWidth))), screenHeight-(math.floor(.7831*(screenHeight)))))

battleTextBox = pygame.image.load('Assets/Battle TextBox.png')
battleTextBox = pygame.transform.scale(officeTextBox, (screenWidth-(math.floor(.1497*(screenWidth))), screenHeight-(math.floor(.7530*(screenHeight)))))

scientist = pygame.image.load('Assets/scientist.png')

standardBattleTheme = pygame.mixer.Sound('Assets/[ONTIVA.COM]-Pokemon FireRed_LeafGreen Music- Trainer Battle-128K.wav')
pokeCenterTheme = pygame.mixer.Sound('Assets/[ONTIVA.COM]-Pokémon Center_Poké Mart [Pokémon FireRed & LeafGreen]-128K.wav')

#Monster Sprites
mouseLegsPic = pygame.image.load('Assets/Monsters/MouseLegs.png')
mouseTorsoPic = pygame.image.load('Assets/Monsters/MouseTorso.png')
mouseHeadPic = pygame.image.load('Assets/Monsters/MouseHead.png')
dogLegsPic = pygame.image.load('Assets/Monsters/DogLegs.png')
dogTorsoPic = pygame.image.load('Assets/Monsters/DogTorso.png')
dogHeadPic = pygame.image.load('Assets/Monsters/DogHead.png')

#Move Sprites
kickPic = pygame.image.load('Assets/Move Sprites/Kick.png')
slashPic = pygame.image.load('Assets/Move Sprites/Slash.png')
bitePic = pygame.image.load('Assets/Move Sprites/Bite.png')
groomPic = pygame.image.load('Assets/Move Sprites/Groom.png')

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
                
#add monster classes here
#sprite, angle, width, height, centerOfTorso, attribute, hitPoints, strengthStat, constitutionStat, intelligenceStat, resilenceStat, mysticStat, willStat, speedStat, moveName, moveMP, movePower, moveDescription,moveAffectedStat,moveSprite,SpriteLocation):
mouseLegs = [mouseLegsPic, 0, (math.floor(.0449*(screenWidth))), (math.floor(.0904*(screenHeight))), .5, 'Physical', 10, 5, 5, 1, 1, 1, 1, 1,'Double Kick', 10, 5, 'Kicks Twice','enemyHP',kickPic,'enemy']
mouseTorso = [mouseTorsoPic, 0, (math.floor(.0299*(screenWidth))), (math.floor(.0904*(screenHeight))), .5, 'Physical', 10, 5, 5, 1, 1, 1, 1, 1, 'Groom', 10, 10, 'Heals','monsterHP',groomPic,'monster']
mouseHead = [mouseHeadPic, 0, (math.floor(.0225*(screenWidth))), (math.floor(.0904*(screenHeight))), .5, 'Physical', 10, 5, 5, 1, 1, 1, 1, 1, 'Bite', 10, 5, 'Bites','enemyHP',bitePic,'enemy']
dogLegs = [dogLegsPic, 0, (math.floor(.1120*(screenWidth))), (math.floor(.2410*(screenHeight))), .35, 'Physical', 20, 5, 5, 1, 1, 1, 1, 2, 'Double Kick', 10, 10, 'Kicks Twice','enemyHP',kickPic,'enemy']
dogTorso = [dogTorsoPic, 30, (math.floor(.0749*(screenWidth))), (math.floor(.2410*(screenHeight))), .35,'Physical', 20, 5, 5, 1, 1, 1, 1, 2, 'Scratch', 10, 10, 'Scratches','enemyHP',slashPic,'enemy']
dogHead = [dogHeadPic, 0, (math.floor(.0449*(screenWidth))), (math.floor(.2410*(screenHeight))), .2,'Physical', 20, 5, 5, 1, 1, 1, 1, 2, 'Bite', 10, 10, 'Bites','enemyHP',bitePic,'enemy']

monsterLegsList = [mouseLegs, dogLegs]
monsterTorsoList = [mouseTorso, dogTorso]
monsterHeadList = [mouseHead, dogHead]





#player monster part inventory
playerPartInventory = []
enemyPartInventory = [mouseLegs, mouseTorso,mouseHead]
                
infoMove4 = ['Move X', '15 MP', 'You dont have the right parts for this move...yet']

bigFont = pygame.font.SysFont('Agency FB', 100)
smallFont = pygame.font.SysFont('Agency FB', 60)
    
def dialogueFunction(surface, textDialogue,textButton1, textButton2):
    global dialogue
    global click
    global overWorld
    global inBattle
    while dialogue:
        surface.blit(officeTextBox, ((math.floor(.0823*(screenWidth))),(math.floor(.6910*(screenHeight)))))
        dialogueText = bigFont.render(textDialogue, 1, (0,0,0))
        buttonText1 = smallFont.render(textButton1, 1, (0,0,0))
        buttonText2 = smallFont.render(textButton2, 1, (0,0,0))
        surface.blit(dialogueText, ((math.floor(.0898*(screenWidth))), (math.floor(.7741*(screenHeight)))))
        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect((math.floor(.7994*(screenWidth))), (math.floor(.7349*(screenHeight))), (math.floor(.0599*(screenWidth))), (math.floor(.0602*(screenHeight))))
        button2 = pygame.Rect((math.floor(.7994*(screenWidth))), (math.floor(.8133*(screenHeight))), (math.floor(.0599*(screenWidth))), (math.floor(.0602*(screenHeight))))
        border1 = pygame.Rect((math.floor(.8009*(screenWidth))), (math.floor(.7380*(screenHeight))), (math.floor(.0569*(screenWidth))), (math.floor(.0542*(screenHeight))))
        border2 = pygame.Rect((math.floor(.8009*(screenWidth))), (math.floor(.8163*(screenHeight))), (math.floor(.0569*(screenWidth))), (math.floor(.0542*(screenHeight))))

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
        surface.blit(buttonText1, ((math.floor(.8174*(screenWidth))), (math.floor(.7410*(screenHeight)))))
        surface.blit(buttonText2, ((math.floor(.8174*(screenWidth))), (math.floor(.8193*(screenHeight)))))
        
        click = False
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()

def dialogueFusingFunction(surface, textDialogue,textButton1, textButton2):
    global dialogue
    global click
    global overWorld
    global fusingMachine
    while dialogue:
        surface.blit(officeTextBox, ((math.floor(.0823*(screenWidth))),(math.floor(.6910*(screenHeight)))))
        dialogueText = bigFont.render(textDialogue, 1, (0,0,0))
        buttonText1 = smallFont.render(textButton1, 1, (0,0,0))
        buttonText2 = smallFont.render(textButton2, 1, (0,0,0))
        surface.blit(dialogueText, ((math.floor(.0898*(screenWidth))), (math.floor(.7741*(screenHeight)))))
        mx, my = pygame.mouse.get_pos()
        button1 = pygame.Rect((math.floor(.7994*(screenWidth))), (math.floor(.7349*(screenHeight))), (math.floor(.0599*(screenWidth))), (math.floor(.0602*(screenHeight))))
        button2 = pygame.Rect((math.floor(.7994*(screenWidth))), (math.floor(.8133*(screenHeight))), (math.floor(.0599*(screenWidth))), (math.floor(.0602*(screenHeight))))
        border1 = pygame.Rect((math.floor(.8009*(screenWidth))), (math.floor(.7380*(screenHeight))), (math.floor(.0569*(screenWidth))), (math.floor(.0542*(screenHeight))))
        border2 = pygame.Rect((math.floor(.8009*(screenWidth))), (math.floor(.8163*(screenHeight))), (math.floor(.0569*(screenWidth))), (math.floor(.0542*(screenHeight))))

        if button1.collidepoint((mx, my)):
            if click:
                dialogue = False
                overWorld = False
                fusingMachine = True
                fusingMachineFunction(window)
        if button2.collidepoint((mx, my)):
            if click:
                dialogue = False
                
        pygame.draw.rect(surface, (0,0,0), button1)
        pygame.draw.rect(surface, (0,0,0), button2)
        pygame.draw.rect(surface, (255,255,255), border1)
        pygame.draw.rect(surface, (255,255,255), border2)
        surface.blit(buttonText1, ((math.floor(.8174*(screenWidth))), (math.floor(.7410*(screenHeight)))))
        surface.blit(buttonText2, ((math.floor(.8174*(screenWidth))), (math.floor(.8193*(screenHeight)))))
        
        click = False
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        

def redrawBattleWindow(surface):
    surface.blit(battle, ((math.floor(.0749*(screenWidth))),(math.floor(.0663*(screenHeight)))))
    pygame.display.update()

    
def inBattleFunction(surface):
    global inBattle
    global overWorld
    global run
    winText = bigFont.render('You Win!', 1, (0,0,0))
    loseText = bigFont.render('You Lose!', 1, (0,0,0))
    monsterHP = (playerPartInventory[0][6]+playerPartInventory[1][6]+playerPartInventory[2][6])
    maxMonsterHP = (playerPartInventory[0][6]+playerPartInventory[1][6]+playerPartInventory[2][6])
    enemyHP = (enemyPartInventory[0][6]+enemyPartInventory[1][6]+enemyPartInventory[2][6])
    maxEnemyHP = (enemyPartInventory[0][6]+enemyPartInventory[1][6]+enemyPartInventory[2][6])
    redrawBattleWindow(surface)
    pokeCenterTheme.stop()
    #standardBattleTheme.play()
    
    if (playerPartInventory[0][13]+playerPartInventory[1][13]+playerPartInventory[2][13]) >= (enemyPartInventory[0][13]+enemyPartInventory[1][13]+enemyPartInventory[2][13]):
        playerTurn = True
        enemyTurn = False
    else:    
        playerTurn = False
        enemyTurn = True
    
    
    playerClearing = False
    enemyClearing = False
    while inBattle == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                inBattle = False
            
        moveText1 = smallFont.render(playerPartInventory[0][14], 1, (0,0,0))
        moveText2 = smallFont.render(playerPartInventory[1][14], 1, (0,0,0))
        moveText3 = smallFont.render(playerPartInventory[2][14], 1, (0,0,0))
        moveText4 = smallFont.render(infoMove4[0], 1, (0,0,0))
        move1MP = smallFont.render(str(playerPartInventory[0][15])+' MP', 1, (0,0,0))
        move2MP = smallFont.render(str(playerPartInventory[1][15])+' MP', 1, (0,0,0))
        move3MP = smallFont.render(str(playerPartInventory[2][15])+' MP', 1, (0,0,0))
        move4MP = smallFont.render(infoMove4[1], 1, (0,0,0))
        move1description = smallFont.render(playerPartInventory[0][17], 1, (0,0,0))
        move2description = smallFont.render(playerPartInventory[1][17], 1, (0,0,0))
        move3description = smallFont.render(playerPartInventory[2][17], 1, (0,0,0))
        move4description = smallFont.render(infoMove4[2], 1, (0,0,0))
        moveTextYes = smallFont.render('Yes', 1, (0,0,0))
        moveTextNo = smallFont.render('No', 1, (0,0,0))
        
        monsterHPText = smallFont.render((str(monsterHP)+'/'+str(maxMonsterHP)), 1, (0,0,0))
        enemyHPText = smallFont.render((str(enemyHP)+'/'+str(maxEnemyHP)), 1, (0,0,0))
        
        buttonMove1 = pygame.Rect((math.floor(.1796*(screenWidth))), (math.floor(.6988*(screenHeight))), (math.floor(.1796*(screenWidth))), (math.floor(.0904*(screenHeight))))
        buttonMove2 = pygame.Rect((math.floor(.1796*(screenWidth))), (math.floor(.7952*(screenHeight))), (math.floor(.1796*(screenWidth))), (math.floor(.0904*(screenHeight))))
        buttonMove3 = pygame.Rect((math.floor(.4491*(screenWidth))), (math.floor(.6988*(screenHeight))), (math.floor(.1796*(screenWidth))), (math.floor(.0904*(screenHeight))))
        buttonMove4 = pygame.Rect((math.floor(.4491*(screenWidth))), (math.floor(.7952*(screenHeight))), (math.floor(.1796*(screenWidth))), (math.floor(.0904*(screenHeight))))
        buttonYes = pygame.Rect((math.floor(.7994*(screenWidth))), (math.floor(.7349*(screenHeight))), (math.floor(.0599*(screenWidth))), (math.floor(.0602*(screenHeight))))
        buttonNo = pygame.Rect((math.floor(.7994*(screenWidth))), (math.floor(.8133*(screenHeight))), (math.floor(.0599*(screenWidth))), (math.floor(.0602*(screenHeight))))
        
        border1 = pygame.Rect((math.floor(.1811*(screenWidth))), (math.floor(.7018*(screenHeight))), (math.floor(.1766*(screenWidth))), (math.floor(.0843*(screenHeight))))
        border2 = pygame.Rect((math.floor(.1811*(screenWidth))), (math.floor(.7982*(screenHeight))), (math.floor(.1766*(screenWidth))), (math.floor(.0843*(screenHeight))))
        border3 = pygame.Rect((math.floor(.4506*(screenWidth))), (math.floor(.7018*(screenHeight))), (math.floor(.1766*(screenWidth))), (math.floor(.0843*(screenHeight))))
        border4 = pygame.Rect((math.floor(.4506*(screenWidth))), (math.floor(.7982*(screenHeight))), (math.floor(.1766*(screenWidth))), (math.floor(.0843*(screenHeight))))
        borderYes = pygame.Rect((math.floor(.8009*(screenWidth))), (math.floor(.7380*(screenHeight))), (math.floor(.0569*(screenWidth))),(math.floor(.0542*(screenHeight))))
        borderNo = pygame.Rect((math.floor(.8009*(screenWidth))), (math.floor(.8163*(screenHeight))), (math.floor(.0569*(screenWidth))), (math.floor(.0542*(screenHeight))))
        

        spriteLegCoord = ((math.floor(.1497*(screenWidth))), (math.floor(.6930*(screenHeight)))-(playerPartInventory[0][3]*playerPartInventory[0][4])-max(playerPartInventory[0][3],playerPartInventory[1][3],playerPartInventory[2][3]))
        spriteTorsoCoord = ((math.floor(.1497*(screenWidth)))+(.9*(playerPartInventory[0][2])), (math.floor(.6930*(screenHeight)))-(playerPartInventory[1][3]*playerPartInventory[1][4])-max(playerPartInventory[0][3],playerPartInventory[1][3],playerPartInventory[2][3]))
        spriteHeadCoord = ((math.floor(.1497*(screenWidth)))+(.9*(playerPartInventory[0][2]))+(.85*(playerPartInventory[1][2])), (math.floor(.6930*(screenHeight)))-(playerPartInventory[2][3]*playerPartInventory[2][4])-max(playerPartInventory[0][3],playerPartInventory[1][3],playerPartInventory[2][3]))

        spriteLeg = (playerPartInventory[0][0])
        spriteTorso = pygame.transform.rotate((playerPartInventory[1][0]), playerPartInventory[0][1])
        spriteHead = pygame.transform.rotate((playerPartInventory[2][0]), playerPartInventory[1][1])

        enemySpriteLegCoord = ((math.floor(.7186*(screenWidth))), (math.floor(.4518*(screenHeight)))-(enemyPartInventory[0][3]*enemyPartInventory[0][4])-max(enemyPartInventory[0][3],enemyPartInventory[1][3],enemyPartInventory[2][3]))
        enemySpriteTorsoCoord = ((math.floor(.7186*(screenWidth)))-(.55*(enemyPartInventory[0][2])), (math.floor(.4518*(screenHeight)))-(enemyPartInventory[1][3]*enemyPartInventory[1][4])-max(enemyPartInventory[0][3],enemyPartInventory[1][3],enemyPartInventory[2][3]))
        enemySpriteHeadCoord = ((math.floor(.7186*(screenWidth)))-(.55*(enemyPartInventory[0][2]))-(.6*(enemyPartInventory[1][2])), (math.floor(.4518*(screenHeight)))-(enemyPartInventory[2][3]*enemyPartInventory[2][4])-max(enemyPartInventory[0][3],enemyPartInventory[1][3],enemyPartInventory[2][3]))

        enemySpriteLeg = pygame.transform.flip(enemyPartInventory[0][0], True, False)
        enemySpriteTorso = pygame.transform.flip(pygame.transform.rotate((enemyPartInventory[1][0]), enemyPartInventory[0][1]), True, False)
        enemySpriteHead = pygame.transform.flip(pygame.transform.rotate((enemyPartInventory[2][0]), enemyPartInventory[1][1]), True, False)

        while playerTurn:
            mMoveScreenx, mMoveScreeny = pygame.mouse.get_pos()
            if buttonMove1.collidepoint((mMoveScreenx, mMoveScreeny)):
                if click:
                    inMove1 = True
                    while inMove1:
                        surface.blit(battleTextBox, ((math.floor(.0749*(screenWidth))),(math.floor(.6747*(screenHeight)))))
                        mMove1x, mMove1y = pygame.mouse.get_pos()
                        
                        if buttonYes.collidepoint((mMove1x, mMove1y)):
                            if click:
                                if playerPartInventory[0][20] == 'enemy':
                                    surface.blit(playerPartInventory[0][19], enemySpriteTorsoCoord)
                                elif playerPartInventory[0][20] == 'monster':
                                    surface.blit(playerPartInventory[0][19], spriteTorsoCoord)
                                
                                if playerPartInventory[0][18] == 'enemyHP':
                                    enemyHP -= playerPartInventory[0][16]
                                elif playerPartInventory[0][18] == 'monsterHP':
                                    monsterHP += playerPartInventory[0][16]
                                inMove1 = False
                                playerTurn = False
                                playerClearing = True
                                pygame.display.update()
                                sleep(4)
                        if buttonNo.collidepoint((mMove1x, mMove1y)):
                            if click:
                                inMove1 = False
                        
                        pygame.draw.rect(surface, (0,0,0), buttonYes)
                        pygame.draw.rect(surface, (0,0,0), buttonNo)
                        pygame.draw.rect(surface, (255,255,255), borderYes)
                        pygame.draw.rect(surface, (255,255,255), borderNo)
                        surface.blit(moveTextYes, ((math.floor(.8174*(screenWidth))), (math.floor(.7410*(screenHeight)))))
                        surface.blit(moveTextNo, ((math.floor(.8174*(screenWidth))), (math.floor(.8193*(screenHeight)))))
                        surface.blit(moveText1, ((math.floor(.1677*(screenWidth))), (math.floor(.6930*(screenHeight)))))
                        surface.blit(move1MP, ((math.floor(.2874*(screenWidth))), (math.floor(.6930*(screenHeight)))))
                        surface.blit(move1description, ((math.floor(.1677*(screenWidth))), (math.floor(.8133*(screenHeight)))))
                        
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
                        surface.blit(battleTextBox, ((math.floor(.0749*(screenWidth))),(math.floor(.6747*(screenHeight)))))
                        mMove2x, mMove2y = pygame.mouse.get_pos()
                        
                        if buttonYes.collidepoint((mMove2x, mMove2y)):
                            if click:
                                if playerPartInventory[1][20] == 'enemy':
                                    surface.blit(playerPartInventory[1][19], enemySpriteTorsoCoord)
                                elif playerPartInventory[1][20] == 'monster':
                                    surface.blit(playerPartInventory[1][19], spriteTorsoCoord)
                                
                                if playerPartInventory[1][18] == 'enemyHP':
                                    enemyHP -= playerPartInventory[1][16]
                                elif playerPartInventory[1][18] == 'monsterHP':
                                    monsterHP += playerPartInventory[1][16]
                                inMove2 = False
                                playerTurn = False
                                playerClearing = True
                                pygame.display.update()
                                sleep(4)
                        if buttonNo.collidepoint((mMove2x, mMove2y)):
                            if click:
                                inMove2 = False
                        
                        pygame.draw.rect(surface, (0,0,0), buttonYes)
                        pygame.draw.rect(surface, (0,0,0), buttonNo)
                        pygame.draw.rect(surface, (255,255,255), borderYes)
                        pygame.draw.rect(surface, (255,255,255), borderNo)
                        surface.blit(moveTextYes, ((math.floor(.8174*(screenWidth))), (math.floor(.7410*(screenHeight)))))
                        surface.blit(moveTextNo, ((math.floor(.8174*(screenWidth))), (math.floor(.8193*(screenHeight)))))
                        surface.blit(moveText2, ((math.floor(.1677*(screenWidth))), (math.floor(.6930*(screenHeight)))))
                        surface.blit(move2MP, ((math.floor(.2874*(screenWidth))), (math.floor(.6930*(screenHeight)))))
                        surface.blit(move2description, ((math.floor(.1677*(screenWidth))), (math.floor(.8133*(screenHeight)))))
                        
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
                        surface.blit(battleTextBox, ((math.floor(.0749*(screenWidth))),(math.floor(.6747*(screenHeight)))))
                        mMove3x, mMove3y = pygame.mouse.get_pos()
                        
                        if buttonYes.collidepoint((mMove3x, mMove3y)):
                            if click:
                                if playerPartInventory[2][20] == 'enemy':
                                    surface.blit(playerPartInventory[2][19], enemySpriteTorsoCoord)
                                elif playerPartInventory[2][20] == 'monster':
                                    surface.blit(playerPartInventory[2][19], spriteTorsoCoord)
                                
                                if playerPartInventory[2][18] == 'enemyHP':
                                    enemyHP -= playerPartInventory[2][16]
                                elif playerPartInventory[2][18] == 'monsterHP':
                                    monsterHP += playerPartInventory[2][16]
                                inMove3 = False
                                playerTurn = False
                                playerClearing = True
                                pygame.display.update()
                                sleep(4)
                        if buttonNo.collidepoint((mMove3x, mMove3y)):
                            if click:
                                inMove3 = False
                        
                        pygame.draw.rect(surface, (0,0,0), buttonYes)
                        pygame.draw.rect(surface, (0,0,0), buttonNo)
                        pygame.draw.rect(surface, (255,255,255), borderYes)
                        pygame.draw.rect(surface, (255,255,255), borderNo)
                        surface.blit(moveTextYes, ((math.floor(.8174*(screenWidth))), (math.floor(.7410*(screenHeight)))))
                        surface.blit(moveTextNo, ((math.floor(.8174*(screenWidth))), (math.floor(.8193*(screenHeight)))))
                        surface.blit(moveText3, ((math.floor(.1677*(screenWidth))), (math.floor(.6930*(screenHeight)))))
                        surface.blit(move3MP, ((math.floor(.2874*(screenWidth))), (math.floor(.6930*(screenHeight)))))
                        surface.blit(move3description, ((math.floor(.1677*(screenWidth))), (math.floor(.8133*(screenHeight)))))
                        
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
                        surface.blit(battleTextBox, ((math.floor(.0749*(screenWidth))),(math.floor(.6747*(screenHeight)))))
                        mMove4x, mMove4y = pygame.mouse.get_pos()
                        
                        if buttonYes.collidepoint((mMove4x, mMove4y)):
                            if click:
                                inMove4 = False
                        if buttonNo.collidepoint((mMove4x, mMove4y)):
                            if click:
                                inMove4 = False
                        
                        pygame.draw.rect(surface, (0,0,0), buttonYes)
                        pygame.draw.rect(surface, (0,0,0), buttonNo)
                        pygame.draw.rect(surface, (255,255,255), borderYes)
                        pygame.draw.rect(surface, (255,255,255), borderNo)
                        surface.blit(moveTextYes, ((math.floor(.8174*(screenWidth))), (math.floor(.7410*(screenHeight)))))
                        surface.blit(moveTextNo, ((math.floor(.8174*(screenWidth))), (math.floor(.8193*(screenHeight)))))
                        surface.blit(moveText4, ((math.floor(.1677*(screenWidth))), (math.floor(.6930*(screenHeight)))))
                        surface.blit(move4MP, ((math.floor(.2874*(screenWidth))), (math.floor(.6930*(screenHeight)))))
                        surface.blit(move4description, ((math.floor(.1677*(screenWidth))), (math.floor(.8133*(screenHeight)))))
                        
                        click = False
            
                        for event in pygame.event.get():
                            if event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    click = True                
                        pygame.display.update()
            
            surface.blit(battleTextBox, ((math.floor(.0749*(screenWidth))),(math.floor(.6747*(screenHeight)))))            
            pygame.draw.rect(surface, (0,0,0), buttonMove1)
            pygame.draw.rect(surface, (0,0,0), buttonMove2)
            pygame.draw.rect(surface, (0,0,0), buttonMove3)
            pygame.draw.rect(surface, (0,0,0), buttonMove4)
            pygame.draw.rect(surface, (255,255,255), border1)
            pygame.draw.rect(surface, (255,255,255), border2)
            pygame.draw.rect(surface, (255,255,255), border3)
            pygame.draw.rect(surface, (255,255,255), border4)
            surface.blit(moveText1, ((math.floor(.1976*(screenWidth))), (math.floor(.7169*(screenHeight)))))
            surface.blit(moveText2, ((math.floor(.1976*(screenWidth))), (math.floor(.8133*(screenHeight)))))
            surface.blit(moveText3, ((math.floor(.4671*(screenWidth))), (math.floor(.7169*(screenHeight)))))
            surface.blit(moveText4, ((math.floor(.4671*(screenWidth))), (math.floor(.8133*(screenHeight)))))
            surface.blit(monsterHPText, ((math.floor(.1497*(screenWidth))), (math.floor(.6024*(screenHeight)))-max(playerPartInventory[0][3],playerPartInventory[1][3],playerPartInventory[2][3])-20))
            surface.blit(enemyHPText, (enemySpriteHeadCoord[0], (math.floor(.2410*(screenHeight)))-max(enemyPartInventory[0][3],enemyPartInventory[1][3],enemyPartInventory[2][3])-40))
        
            surface.blit(pygame.transform.scale(spriteLeg, (playerPartInventory[0][2],playerPartInventory[0][3])), spriteLegCoord)
            surface.blit(pygame.transform.scale(spriteTorso, (playerPartInventory[1][2],playerPartInventory[1][3])), spriteTorsoCoord)
            surface.blit(pygame.transform.scale(spriteHead, (playerPartInventory[2][2],playerPartInventory[2][3])), spriteHeadCoord)
            
            surface.blit(pygame.transform.scale(enemySpriteLeg, (enemyPartInventory[0][2],enemyPartInventory[0][3])), enemySpriteLegCoord)
            surface.blit(pygame.transform.scale(enemySpriteTorso, (enemyPartInventory[1][2],enemyPartInventory[1][3])), enemySpriteTorsoCoord)
            surface.blit(pygame.transform.scale(enemySpriteHead, (enemyPartInventory[2][2],enemyPartInventory[2][3])), enemySpriteHeadCoord)
            click = False
        
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()
        while enemyTurn:
            redrawBattleWindow(surface)
            monsterHP -= 10 
            surface.blit(monsterHPText, (spriteLegCoord[0], (math.floor(.6024*(screenHeight)))-max(playerPartInventory[0][3],playerPartInventory[1][3],playerPartInventory[2][3])-40))
            surface.blit(enemyHPText, (enemySpriteHeadCoord[0], (math.floor(.2410*(screenHeight)))-max(enemyPartInventory[0][3],enemyPartInventory[1][3],enemyPartInventory[2][3])-40))
            
            surface.blit(pygame.transform.scale(spriteLeg, (playerPartInventory[0][2],playerPartInventory[0][3])), spriteLegCoord)
            surface.blit(pygame.transform.scale(spriteTorso, (playerPartInventory[1][2],playerPartInventory[1][3])), spriteTorsoCoord)
            surface.blit(pygame.transform.scale(spriteHead, (playerPartInventory[2][2],playerPartInventory[2][3])), spriteHeadCoord)
            
            surface.blit(pygame.transform.scale(enemySpriteLeg, (enemyPartInventory[0][2],enemyPartInventory[0][3])), enemySpriteLegCoord)
            surface.blit(pygame.transform.scale(enemySpriteTorso, (enemyPartInventory[1][2],enemyPartInventory[1][3])), enemySpriteTorsoCoord)
            surface.blit(pygame.transform.scale(enemySpriteHead, (enemyPartInventory[2][2],enemyPartInventory[2][3])), enemySpriteHeadCoord)
            
            enemyTurn = False
            enemyClearing = True
            pygame.display.update()
            sleep(2)
        while enemyClearing:
            redrawBattleWindow(surface)
            enemyClearing = False
            playerTurn = True
            pygame.display.update()
        while playerClearing:
            redrawBattleWindow(surface)
            playerClearing = False
            enemyTurn = True
            pygame.display.update()
            
        if monsterHP > maxMonsterHP :
            monsterHP = maxMonsterHP
        if monsterHP <= 0 :
            surface.blit(loseText, ((math.floor(.4790*(screenWidth))), (math.floor(.3012*(screenHeight)))))
            pygame.display.update()
            sleep(2)
            inBattle = False
            overWorld = True
            inOfficeFunction(window)

        elif enemyHP <= 0:
            surface.blit(winText, ((math.floor(.4790*(screenWidth))), (math.floor(.3012*(screenHeight)))))
            pygame.display.update()
            sleep(2)
            inBattle = False
            overWorld = True
            inOfficeFunction(window)

        pygame.display.update()
def inOfficeFunction(surface):
    pokeCenterTheme.stop()
    #pokeCenterTheme.play()
    global run
    global overWorld
    global inFreezer
    global inBattle
    global dialogue
    global click
    global char
    global fusingMachine
    while overWorld:
        clock.tick(10)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                overWorld = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and char.x > (math.floor(.0749*(screenWidth))):
            char.x -= char.vel
            char.left = True
            char.right = False
            char.up = False
            char.down = False
            char.faceLeft = True
            char.faceRight = False
            char. faceUp = False
            char. faceDown = False
        elif keys[pygame.K_RIGHT] and char.x < (math.floor(.9222*(screenWidth))) - char.vel - char.width:
            char.x += char.vel
            char.left = False
            char.right = True
            char.up = False
            char.down = False
            char.faceLeft = False
            char.faceRight = True
            char. faceUp = False
            char. faceDown = False
        elif keys[pygame.K_UP] and char.y > (math.floor(.0663*(screenHeight))) + char.vel:
            char.y -= char.vel
            char.left = False
            char.right = False
            char.up = True
            char.down = False
            char.faceLeft = False
            char.faceRight = False
            char. faceUp = True
            char. faceDown = False
        elif keys[pygame.K_DOWN] and char.y < (math.floor(.9036*(screenHeight))) - char.height:
            char.y += char.vel
            char.left = False
            char.right = False
            char.up = False
            char.down = True
            char.faceLeft = False
            char.faceRight = False
            char.faceUp = False
            char.faceDown = True
        elif keys[pygame.K_SPACE] and char.x < (math.floor(.3443*(screenWidth))) and char.x > (math.floor(.2844*(screenWidth))) and char.y < (math.floor(.4217*(screenHeight))) and char.y > (math.floor(.3012*(screenHeight))):
            dialogue = True
            dialogueFunction(window, 'Ayy Im Italian baby, you wanna tustle wid dis muscle?', 'Yes', 'No')
        elif char.x > (math.floor(.0599*(screenWidth))) and char.x < (math.floor(.1198*(screenWidth))) and char.y > (math.floor(.3313*(screenHeight))) and char.y < (math.floor(.5060*(screenHeight))) and inFreezer == False:
            inFreezer = True
            overWorld = False
            inFreezerFunction(window)
        elif keys[pygame.K_SPACE] and char.x < (math.floor(.8234*(screenWidth))) and char.x > (math.floor(.6437*(screenWidth))) and char.y < (math.floor(.8434*(screenHeight))) and char.y > (math.floor(.4819*(screenHeight))):
            dialogue = True
            dialogueFusingFunction(window, 'Fuse Parts?', 'Yes', 'No')
        else:
            char.left = False
            char.right = False
            char.up = False
            char.down = False
            
        surface.blit(office, ((math.floor(.0749*(screenWidth))),(math.floor(.0663*(screenHeight)))))
        char.charDraw(surface)
        surface.blit(scientist, ((math.floor(.2994*(screenWidth))),(math.floor(.3614*(screenHeight)))))
        pygame.display.update()
    
def inFreezerFunction(surface):
    pokeCenterTheme.stop()
    #pokeCenterTheme.play()
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
        if keys[pygame.K_LEFT] and char.x > (math.floor(.2096*(screenWidth))) + char.vel + (math.floor(.0602*(screenHeight))):
            char.x -= char.vel
            char.left = True
            char.right = False
            char.up = False
            char.down = False
            char.faceLeft = True
            char.faceRight = False
            char. faceUp = False
            char. faceDown = False
        elif keys[pygame.K_RIGHT] and char.x < (math.floor(.5090*(screenWidth))) - char.width - char.vel:
            char.x += char.vel
            char.left = False
            char.right = True
            char.up = False
            char.down = False
            char.faceLeft = False
            char.faceRight = True
            char. faceUp = False
            char. faceDown = False
        elif keys[pygame.K_UP] and char.y > (math.floor(.2108*(screenHeight))) + char.vel + (math.floor(.0602*(screenHeight))):
            char.y -= char.vel
            char.left = False
            char.right = False
            char.up = True
            char.down = False
            char.faceLeft = False
            char.faceRight = False
            char. faceUp = True
            char. faceDown = False
        elif keys[pygame.K_DOWN] and char.y < (math.floor(.8133*(screenHeight))) - char.height - char.vel - 130:
            char.y += char.vel
            char.left = False
            char.right = False
            char.up = False
            char.down = True
            char.faceLeft = False
            char.faceRight = False
            char. faceUp = False
            char. faceDown = True
        elif char.x < (math.floor(.5090*(screenWidth))) and char.x > (math.floor(.4641*(screenWidth))) and char.y > (math.floor(.4217*(screenHeight))) and char.y < (math.floor(.5422*(screenHeight))) and overWorld == False:
            inFreezer = False
            overWorld = True
            inOfficeFunction(window)
        elif char.x < (math.floor(.2096*(screenWidth))) and inFreezer == True:
            char.x = (math.floor(.4491*(screenWidth))) 
        else:
            char.left = False
            char.right = False
            char.up = False
            char.down = False
        surface.fill((0,0,0))
        surface.blit(freezer, ((math.floor(.2096*(screenWidth))),(math.floor(.2108*(screenHeight)))))
        char.charDraw(surface)
        pygame.display.update()
        
        
menuLegsCount = 0
menuTorsoCount = 0
menuHeadCount = 0
        
def fusingMachineFunction(surface):        
    global run
    global overWorld     
    global click
    global fusingMachine
    global menuLegsCount
    global menuTorsoCount
    global menuHeadCount
    while fusingMachine:
        
        clock.tick(60)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                fusingMachine = False
                
        textUp = smallFont.render('Up', 1, (255,255,255))
        textDown = smallFont.render('Down', 1, (255,255,255))
        textFuse = bigFont.render('Stitch Em Up!', 1, (255,255,255))
        
        mx, my = pygame.mouse.get_pos()
        
        buttonUp1 = pygame.Rect((math.floor(.2021*(screenWidth))), (math.floor(.1687*(screenHeight))), (math.floor(.0449*(screenWidth))), (math.floor(.0602*(screenHeight))))
        buttonDown1 = pygame.Rect((math.floor(.2021*(screenWidth))), (math.floor(.5542*(screenHeight))), (math.floor(.0449*(screenWidth))), (math.floor(.0602*(screenHeight))))
        buttonUp2 = pygame.Rect((math.floor(.4716*(screenWidth))), (math.floor(.1687*(screenHeight))), (math.floor(.0449*(screenWidth))), (math.floor(.0602*(screenHeight))))
        buttonDown2 = pygame.Rect((math.floor(.4716*(screenWidth))), (math.floor(.5542*(screenHeight))), (math.floor(.0449*(screenWidth))), (math.floor(.0602*(screenHeight))))
        buttonUp3 = pygame.Rect((math.floor(.7410*(screenWidth))), (math.floor(.1687*(screenHeight))), (math.floor(.0449*(screenWidth))), (math.floor(.0602*(screenHeight))))
        buttonDown3 = pygame.Rect((math.floor(.7410*(screenWidth))), (math.floor(.5542*(screenHeight))), (math.floor(.0449*(screenWidth))), (math.floor(.0602*(screenHeight))))
        buttonFuse = pygame.Rect((math.floor(.4251*(screenWidth))), (math.floor(.6627*(screenHeight))), (math.floor(.3012*(screenHeight))), (math.floor(.0599*(screenWidth))))
                  
        if buttonUp1.collidepoint((mx, my)):
            if click:
                menuLegsCount += 1
                if menuLegsCount >= len(monsterLegsList):
                    menuLegsCount = 0
        if buttonDown1.collidepoint((mx, my)):
            if click:
                menuLegsCount -= 1
                if menuLegsCount < 0:
                    menuLegsCount = 0 
        if buttonUp2.collidepoint((mx, my)):
            if click:
                menuTorsoCount += 1
                if menuTorsoCount >= len(monsterTorsoList):
                    menuTorsoCount = 0
        if buttonDown2.collidepoint((mx, my)):
            if click:
                menuTorsoCount -= 1
                if menuTorsoCount < 0:
                    menuTorsoCount = 0 
        if buttonUp3.collidepoint((mx, my)):
            if click:
                menuHeadCount += 1
                if menuHeadCount >= len(monsterHeadList):
                    menuHeadCount = 0
        if buttonDown3.collidepoint((mx, my)):
            if click:
                menuHeadCount -= 1
                if menuHeadCount < 0:
                    menuHeadCount = 0
        if buttonFuse.collidepoint((mx, my)):
            if click:
                playerPartInventory.clear()
                playerPartInventory.insert(0, monsterLegsList[menuLegsCount])
                playerPartInventory.insert(1, monsterTorsoList[menuTorsoCount])
                playerPartInventory.insert(2, monsterHeadList[menuHeadCount])
                fusingMachine = False
                overWorld = True
                inOfficeFunction(window)
                                
        surface.fill((0,0,0))
        pygame.draw.rect(surface, (200,200,200), ((math.floor(.0749*(screenWidth))),(math.floor(.0663*(screenHeight))),(math.floor(.8503*(screenWidth))),(math.floor(.8494*(screenHeight)))))
        pygame.draw.rect(surface, (0,0,0), ((math.floor(.1497*(screenWidth))),(math.floor(.2410*(screenHeight))),(math.floor(.1497*(screenWidth))),(math.floor(.3012*(screenHeight)))))
        pygame.draw.rect(surface, (200,200,200), ((math.floor(.1512*(screenWidth))),(math.floor(.2440*(screenHeight))),(math.floor(.1467*(screenWidth))),(math.floor(.2952*(screenHeight)))))        
        pygame.draw.rect(surface, (0,0,0), ((math.floor(.4251*(screenWidth))),(math.floor(.2410*(screenHeight))),(math.floor(.1497*(screenWidth))),(math.floor(.3012*(screenHeight)))))
        pygame.draw.rect(surface, (200,200,200), ((math.floor(.4266*(screenWidth))),(math.floor(.2440*(screenHeight))),(math.floor(.1467*(screenWidth))),(math.floor(.2952*(screenHeight)))))
        pygame.draw.rect(surface, (0,0,0), ((math.floor(.6886*(screenWidth))),(math.floor(.2410*(screenHeight))),(math.floor(.1497*(screenWidth))),(math.floor(.3012*(screenHeight)))))
        pygame.draw.rect(surface, (200,200,200), ((math.floor(.6901*(screenWidth))),(math.floor(.2440*(screenHeight))),(math.floor(.1467*(screenWidth))),(math.floor(.2952*(screenHeight)))))
        
        pygame.draw.rect(surface, (0,0,0), buttonUp1)
        pygame.draw.rect(surface, (0,0,0), buttonDown1)
        pygame.draw.rect(surface, (0,0,0), buttonUp2)
        pygame.draw.rect(surface, (0,0,0), buttonDown2)
        pygame.draw.rect(surface, (0,0,0), buttonUp3)
        pygame.draw.rect(surface, (0,0,0), buttonDown3)
        pygame.draw.rect(surface, (0,0,0), buttonFuse)
   
        surface.blit(textUp, ((math.floor(.2186*(screenWidth))), (math.floor(.1747*(screenHeight)))))
        surface.blit(textUp, ((math.floor(.4880*(screenWidth))), (math.floor(.1747*(screenHeight)))))
        surface.blit(textUp, ((math.floor(.7575*(screenWidth))), (math.floor(.1747*(screenHeight)))))
        surface.blit(textDown, ((math.floor(.2096*(screenWidth))), (math.floor(.5602*(screenHeight)))))
        surface.blit(textDown, ((math.floor(.4790*(screenWidth))), (math.floor(.5602*(screenHeight)))))
        surface.blit(textDown, ((math.floor(.7485*(screenWidth))), (math.floor(.5602*(screenHeight)))))
        surface.blit(textFuse, ((math.floor(.4341*(screenWidth))), (math.floor(.6930*(screenHeight)))))
        
        surface.blit(monsterLegsList[menuLegsCount][0], ((math.floor(.1796*(screenWidth))), (math.floor(.3012*(screenHeight)))))
        surface.blit(monsterTorsoList[menuTorsoCount][0], ((math.floor(.4790*(screenWidth))), (math.floor(.3012*(screenHeight)))))
        surface.blit(monsterHeadList[menuHeadCount][0], ((math.floor(.7485*(screenWidth))), (math.floor(.3012*(screenHeight)))))
        
        click = False
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        

run = True
overWorld = True
inFreezer = False
inBattle = True
dialogue = False
click = False
char = player((math.floor(.2096*(screenWidth))), (math.floor(.8434*(screenHeight))), (math.floor(.0219*(screenWidth))), (math.floor(.0602*(screenHeight))), (math.floor(.0452*(screenHeight))))

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