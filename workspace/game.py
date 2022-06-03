import pygame, sys
pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("아마도 게임")
clock= pygame.time.Clock()

class character:
    def __init__(self):
        self.x = 50
        self.y = 50
    def draw(self):
        pygame.draw.rect(window, (255,255,255), [self.x,self.y,20,20])    

coffee = character()


while True:
    window.fill((0,0,0))
    coffee.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                coffee.y -= 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                coffee.y += 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                coffee.x -= 10 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                coffee.x += 10                

                      

    pygame.display.update()
    clock.tick(30)



    
        
            