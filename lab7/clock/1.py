import pygame
import datetime
pygame.init()
angle1 = 0
angle2 = 0

pygame.mixer.music.load(r"C:\Users\123\Documents\lab3\pp\lab7\clock\sound\clock.mp3")
pygame.mixer.music.play(-1)

sc = pygame.display.set_mode((600,400))
sys = pygame.font.SysFont("arial",35)

pygame.display.set_caption("clock")
pygame.display.set_icon(pygame.image.load(r"C:\Users\123\Documents\lab3\pp\lab7\clock\images\clock.png"))

sc.fill('White')
clock = pygame.time.Clock()

mickey = pygame.image.load(r'C:\Users\123\Documents\lab3\pp\lab7\clock\images\mickey.png')
left = pygame.image.load(r'C:\Users\123\Documents\lab3\pp\lab7\clock\images\left.png').convert_alpha()
right = pygame.image.load(r'C:\Users\123\Documents\lab3\pp\lab7\clock\images\right.png').convert_alpha()

mickey = pygame.transform.scale(mickey,(mickey.get_width()//3,mickey.get_height()//3))
x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    t = datetime.datetime.now()
    angle1 = -t.second*6
    angle2 = -t.minute*6

    sc_sys = sys.render(f'{t:%H-%M-%S}',1,(0,0,0),(255,255,255))
    left_hand_surf1 = pygame.transform.rotate(left,angle1)
    right_hand_surf1 = pygame.transform.rotate(right,angle2)
    
    right_hand_surf1=pygame.transform.scale(right_hand_surf1,(right_hand_surf1.get_width()//1.2 ,right_hand_surf1.get_height()//1.5))
    left_hand_surf1=pygame.transform.scale(left_hand_surf1,(left_hand_surf1.get_width()//1.2 , left_hand_surf1.get_height()//1.5))
    
    mickeyrect = mickey.get_rect(center = (600//2,400//2))
    left_hand_rect = left_hand_surf1.get_rect(center = (600//2,400//2))
    right_hand_rect = right_hand_surf1.get_rect(center = (600//2,400//2))
    
    sc.blit(mickey,mickeyrect)
    sc.blit(left_hand_surf1,left_hand_rect)
    sc.blit(right_hand_surf1,right_hand_rect)
    sc.blit(sc_sys,(10,10))    
    x-=1

    pygame.display.update()
    clock.tick(60)
