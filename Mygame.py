import pygame
pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Squarey")
x = 100
y = 100
baddyX = 300
baddyY = 300
vel = 100
baddyvel = 80
run = True
def draw_game():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, 20, 20))
    pygame.draw.rect(win, (255, 0, 0), (baddyX, baddyY, 40, 40))
    pygame.display.update()
    
    
while run:
    pygame.time.delay(100)
    
    if baddyX < x - 50:
        baddyX = baddyX + baddyvel
        draw_game()
       
    elif baddyX > x + 50:
        baddyX = baddyX - baddyvel
        draw_game()
        
       
    elif baddyY < y - 50:
        baddyY = baddyY + baddyvel
        draw_game()
        
    elif baddyY > y + 50:
        baddyY = baddyY - baddyvel   
    else:
        run = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel
    
    if keys[pygame.K_RIGHT]:
        x += vel
    
    if keys[pygame.K_UP]:
        y -= vel
    
    if keys[pygame.K_DOWN]:
        y += vel
        
    draw_game()
pygame.quit()