
import pygame
import sys



screen_width = 800
screen_height = 600

#creating game class

class Game:
     # creating constructor
     def _init_(self):
          pass
     
     #run method
     def run(self):
          print("running")
     
     #draw method
     def draw(self):
          print("drawing")
     




if __name__ == '_main_' :  
          
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()


    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                screen.fill((33, 112,224))

                pygame.display.update()
                clock.tick(60)