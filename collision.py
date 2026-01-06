import pygame
import random

screen_width,screen_height=500,400
movement_speed=5
font_size=72

pygame.init()
#bg=pygame.image.load("C:\Users\DELL\Desktop\python\space invader\rock.jpg")
#backgroundImage=pygame.transform.scale(bg,(screen_width,screen_height))
font=pygame.font.SysFont("Time New Roman",font_size)

class Sprite:
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color("dodgerblue"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()
    def move(self,x_change,y_change):
        self.x.rect=max(min(self.rect.x+x_change,screen_width-self.rect.width),0)
        self.y.rect=max(min(self.rect.y+y_change,screen_height-self.rect.height),0)

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Collision")
all_sprites=pygame.sprite.Group()

sp1=Sprite(pygame.Color("black"),20,30)
sp1.rect.x,sp1.rect.y=random.randint(0,screen_width-sp1.rect.width),random.randint(0,screen_height-sp1.rect.height)
all_sprites.add(sp1)

sp2=Sprite(pygame.Color("red"),20,30)
sp2.rect.x,sp1.rect.y=random.randint(0,screen_width-sp2.rect.width),random.randint(0,screen_height-sp2.rect.height)
all_sprites.add(sp2)

running,won=True,False
clock=pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_x):
            running=False 
    if not won:
        keys=pygame.key.get_pressed()
        x_change=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*movement_speed
        y_change=(keys[pygame.K_DOWN]-keys[pygame.K_UP])*movement_speed
        sp1.move(x_change,y_change)
        if sp1.rect.colliderect(sp2.rect):
            all_sprites.remove(sp2)
            won=True
   # screen.blit(backgroundImage(0,0))
    all_sprites.draw(screen)

    if won:
        win_text=font.render("YOU WON",True,pygame.Color("black"))
        screen.blit(win_text,((screen_width-win_text.get_width())//2,(screen_height-win_text.get_height())//2))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()