'''

Chapter 13 : Sprites
Aye Myat @ Charlotte

'''

import sys
import pygame
import time

class Human (pygame.sprite.Sprite):
    def __init__ (self,x,y):
        super().__init__()
        
        self.frame = [] #the characteristic of frame is an empty list

        sheet = pygame.image.load("links.gif").convert()

        #frame
        for i in range (32):
            self.frame.append (pygame.Surface([80,100]).convert())

            patch= (100*(i%32),47*(i//32),80,100)

            self.frame[i].blit(sheet, (0,0), patch)
            self.frame[i].set_colorkey ((0,0,0))

        #starting varibles 
        self.anim_frame = 0
        self.image = self.frame [0]
        self.rect = self.image.get_rect()

        self.rect.x=x
        self.rect.y=y                             
        self.accel=500
        self.deltax=0
        self.deltay=0


    #animation 
    def update (self):
        self.anim_frame = (self.anim_frame+1)%8

        if self.deltax>0:
            self.image=self.frame[self.anim_frame]
        else:
            self.image=pygame.transform.flip(self.frame[self.anim_frame],True,False)
            

        self.rect.x += self.deltax
        self.rect.y += self.deltay


def main():

    pygame.init()

    main_surface = pygame.display.set_mode((474,330))


    background=pygame.image.load("beach.jpg")
    main_surface.blit(background,(0,0))


    # create the sprites and initialize the sprite groups
    human=Human(100,158)
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(human)



    while True:


            # The below for loop checks to see if someone has tried to exit the game.
            # if so close out gracefully.

            #do other event checks here too like look for keyboard or mouse input
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = event.dict['key']
                if key == 32:
                    human.accel=-500
                elif key == pygame.K_LEFT:
                   human.deltax=-3
                elif key == pygame.K_RIGHT:
                   human.deltax=3
                else:
                   human.deltax=0
                
        all_sprites.update()

        main_surface.blit(background,(0,0))

        all_sprites.draw(main_surface)

        pygame.display.flip()

        time.sleep(0.01) 

       

        # redraw the screen

if __name__=='__main__':    
    main()
    
        
