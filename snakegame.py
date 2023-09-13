import pygame 


#INITIALIZING THE WINDOW 
if __name__ == "__snakegame__":
    pygame.init()

surface = pygame.display.set_mode((1000,1000))
surface.fill((110,110,5))
pygame.display.flip()
pygame.display.set_caption("Shaytan Fruit")

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
            
pygame.quit
quit()

#MOVING THE SNAKE