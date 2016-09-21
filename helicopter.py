# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 17:57:12 2016

@author: Kingdom of Northumbria LLC
"""


import pygame #importing pygame module
import time
from random import randint
black = (0, 0, 0) #colors
white = (255, 255, 255) #colors
azure = (135,206,235) #colors
red = (214, 0, 0)#colors

imageWidth = 200
imageHeight = 100
screenTopLeft = 0

pygame.init() #initiating
surfaceWidth = 800 
surfaceHeight = 500
surface = pygame.display.set_mode((surfaceWidth, surfaceHeight)) #resolution
pygame.display.set_caption("Allahu Akbar") #name at the top of window
clock = pygame.time.Clock() #for setting frames per second

img = pygame.image.load('heili.png') #adding image

def score(count):
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Score: "+str(count), True, white)
    surface.blit(text,[0, 0])

def blocks(x_block, y_block, blockWidth, blockHeight, gap):
    pygame.draw.rect(surface, red, [x_block, y_block, blockWidth, blockHeight]) #verevi qarakusin
    pygame.draw.rect(surface, red, [x_block, y_block+blockHeight+gap, blockWidth, surfaceHeight]) #taki qarakusin. if you wanna have multiple gaps, change surface Height to blockHeight

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, white) #background can be
    return textSurface, textSurface.get_rect()

#in order to indicate that the game is lost
def msgSurface(text):
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    largeText = pygame.font.Font("freesansbold.ttf", 100)
    
    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth/2, surfaceHeight/2
    surface.blit(titleTextSurf, titleTextRect)
    
    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center = surfaceWidth/2, ((surfaceHeight/2)+100) 
    
    surface.blit(typTextSurf, typTextRect) #to the text lines things
    
    pygame.display.update() #update stuff
    time.sleep(1) #wait up for 1 sec
    
    while replay_or_quit() == None:
        clock.tick() 
    
    main() #calling the main function

#IF GAME IS LOST
def gameOver():
    msgSurface("Allahu Akbar!")

def helicopter(x, y, image): #beginning function
    surface.blit(img, (x, y)) #coordinates

def main():  
    x = 150 #X axis
    y = 200 #Y axis 
    y_move = 0  
    
    x_block = surfaceWidth #where blocks begin
    y_block = 0 #verevi texy
    
    blockWidth = 100 #boy@
    blockHeight = randint(0, (surfaceWidth/2))
    gap = imageHeight*2 #Defines the height of the gap
    block_move = 5 #Movement of blocks in pxs
    current_score = 0 #are you blind?     
    
    
    game_over = False #set game over to false until some event
    while not game_over: #  <-
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #quit via X
                game_over = True #16 <-
                
                
            if event.type == pygame.KEYDOWN: #-5 means up, kinda the opposit thing
                if event.key == pygame.K_UP:
                    y_move = -5
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5
            
        y += y_move
        
        surface.fill(azure) #filling background black
        helicopter(x, y, img) #position helicopter
        score(current_score) #for scoring
        
        blocks(x_block, y_block, blockWidth, blockHeight, gap)
        x_block -= block_move
        
        if y > surfaceHeight-imageHeight or y < screenTopLeft:
            gameOver()
            
        if x_block < (-1*blockWidth):
            x_block = surfaceWidth
            blockHeight = randint(0, (surfaceHeight/2))
        
        if x + imageWidth > x_block:
                if x < x_block + blockWidth:
                    #print("within the x")
                    if y < blockHeight:
                        #print("Y crossover upper")
                        if x-imageWidth < blockWidth+x_block:
                            #print("game over hit upper")
                            gameOver()
            
        if x + imageWidth > x_block:
            #print('x crossover')
            if y + imageHeight > blockHeight + gap:
                #print('possible y crossover')
                if x < blockWidth + x_block:
                   #print('game over low')
                    gameOver()
                    
        if x > x_block: #and x > x_block-block_move:
            current_score = round(current_score + 1/50, 2)
            
        if 3<=current_score < 5:
            block_move = 7
            gap = imageHeight*1.6
        
        if 5<=current_score < 8:
            block_move = 10
            gap = imageHeight*1.2
         
        if 8<=current_score < 12:
            block_move = 3
            gap = imageHeight*1.4
        
        if 12<=current_score < 15:
            block_move = 15
            gap = imageHeight*1.2
            
        if 15<=current_score < 20:
            block_move = 18
            gap = imageHeight*1.1
               
        pygame.display.update() #update parts
        clock.tick(60) #60 frames per second
main()
pygame.quit() #quit game
quit() #kill application