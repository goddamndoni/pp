import pygame
import os
pygame.init()

w = 600
h = 400
begin , is_sing = False,False
vol,i = 1, 0
stop , volumeUP,volumeDown = True,False,False
icon = None

sc = pygame.display.set_mode((w,h))
pygame.display.set_icon(pygame.image.load(r"C:\Users\123\Documents\lab3\pp\lab7\player\buttons\icon.png"))
pygame.display.set_caption("Music")


def load():
    songs = []
    list_of_musics = os.listdir(r"C:\Users\123\Documents\lab3\pp\lab7\player\music")
    for i in list_of_musics:
        if i.endswith(".mp3"):
            songs.append(i)
    return songs
surf = pygame.Surface((340,55))
musics = load()


song_end1 = False
song_end = pygame.USEREVENT
pygame.mixer.music.set_endevent(song_end)
clock = pygame.time.Clock()
x = 33
surf_1 = pygame.Surface((340, 55))

while True:
    sc.fill((0,0,0))
    if pygame.mixer.music.get_busy() == True:
        is_sing = True
    else:
        is_sing = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                begin = True
                music = musics[i]
                i = musics.index(music)
                pygame.mixer.music.load(f'music\{music}')
                pygame.mixer.music.play()
                icon = 0
                x = 33
                stop = False
                
            if event.key == pygame.K_SPACE: 
                if not is_sing:
                    pygame.mixer.music.unpause()
                    stop = False
                else:
                    pygame.mixer.music.pause()
                    stop = True

            if event.key == pygame.K_RIGHT and is_sing:
                x = 33
                if i == len(musics) - 1:
                    i = 0
                    icon = 0
                else:
                    i += 1
                    icon += 1
                pygame.mixer.music.load(f'music\{musics[i]}')
                pygame.mixer.music.play()
                a = pygame.mixer.Sound(f'music\{musics[i]}')
               
            if event.key == pygame.K_LEFT and is_sing:
                x = 33
                if i == 0:
                    icon = len(musics) - 1
                    i = len(musics) - 1
                else:
                    i -= 1
                    icon -= 1
        
                pygame.mixer.music.rewind()
                pygame.mixer.music.load(f'music\{musics[i]}')
                pygame.mixer.music.play()
        
            if event.key == pygame.K_UP: 
                volumeUP = True
                
            if event.key == pygame.K_DOWN:
                volumeDown = True

        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP,pygame.K_DOWN]:
                volumeUP , volumeDown = False , False
        if event.type == song_end:
            song_end1 = 1

    font = pygame.font.SysFont('Tahoma', 16, True) 
    
    if song_end1:
        if i == 0:
            i = len(musics) - 1
        else:
            i -= 1
        song_end1 = False
        pygame.mixer.music.load(f'music\{musics[i]}')
        pygame.mixer.music.play()
    
    
    sc.blit(surf_1, (30, 350))
    surf_1.fill((50,50,50))

    if begin:
        s = font.render(musics[i][:-4], True, 'white')  
        sc.blit(s, (x, 350)) 
    
    if x >=200:
        x = 33

    if volumeUP == True:
        vol += 0.01
        pygame.mixer.music.set_volume(vol)
    if volumeDown == True:
        vol -= 0.01
        pygame.mixer.music.set_volume(vol)

    pygame.display.update()
    clock.tick(60)
    