import pygame 

pygame.init()
screen = pygame.display.set_mode([500, 500])
run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("red")
    pygame.draw.rect(screen, "blue", [100, 100, 100, 100], 1)
    pygame.draw.rect(screen, "blue", [200, 100, 100, 100], 1)
    pygame.draw.rect(screen, "blue", [300, 100, 100, 100], 1)
    pygame.draw.rect(screen, "blue", [100, 100, 100, 200], 1)
    pygame.draw.rect(screen, "blue", [200, 100, 100, 200], 1)
    pygame.draw.rect(screen, "blue", [300, 100, 100, 200], 1)
    pygame.draw.rect(screen, "blue", [100, 100, 100, 300], 1)
    pygame.draw.rect(screen, "blue", [200, 100, 100, 300], 1)
    pygame.draw.rect(screen, "blue", [300, 100, 100, 300], 1)
    pygame.display.flip()


pygame.quit()