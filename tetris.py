from random import randint
import pygame

def podspodem(pos_x, pos_y, tetromino) -> bool:
    global static
    leci: bool = False
    for i in tetromino:
        if pos_y + i[1] != 19:
            print(pos_y + i[1], pos_y)
            if pos_y + i[1] > 0:
                if static[pos_y + i[1]][pos_x] != 0:
                    leci = True
        else:
            leci = True
    return leci

def maks(pos_y, tetromino) -> int:
    maks = 0
    for i in tetromino:
        if maks < (pos_y + i[1]):
            maks = pos_y + i[1]
    return maks

def kolory_11(element, palet) -> tuple:
    kolory = [(0, 89, 248), (66, 184, 255), (0, 169, 0), (178, 248, 27), (218, 0, 204), (249, 121, 246), (2, 88, 248), (89, 217, 90), (226, 0, 88), (89, 250, 157), (88, 248, 158), (107, 132, 254), (252, 52, 8), (125, 125, 125), (103, 69, 251), (176, 0, 31), (0, 89, 248), (244, 58, 2), (250, 53, 3), (252, 160, 68)]
    if element == 2:
        return kolory[palet * 2 + 1]
    else:
        return kolory[palet * 2]

def klatka(level) -> int:
    lista = [48, 43, 38, 33, 28, 23, 18, 13, 8, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    if level >= 29:
        return 1
    else:
        return lista[level]

tak = True
while tak:
    try:
        N = int(input("skala rozdzielczości: "))
    except:
        print("złe dane.")
    else:
        if N >= 1:
            tak = False
        else:
            print("złe dane.")
wymiary: tuple = (256 * N, 240 * N)
pygame.init()
screen = pygame.display.set_mode(wymiary)
clock = pygame.time.Clock()
running: bool = True
znaki = pygame.font.Font("nintendo-nes-font.ttf", (8 * N))
background = pygame.image.load("background.bmp")
background = pygame.transform.scale(background, wymiary)

tetromino = [
    [ # T
        [[-1, 0], [0, 1], [0, 0], [1, 0]],
        [[-1, 0], [0, 1], [0 ,0], [0, -1]],
        [[-1, 0], [0, -1], [1, 0], [0, 0]],
        [[0, -1], [0, 0], [1, 0], [0, 1]]
    ], [ # J
        [[0, -1], [0, 0], [0, 1], [-1, 1]],
        [[-1, -1], [-1, 0], [0, 0], [1, 0]],
        [[1, -1], [0, -1], [0, 0], [0, 1]],
        [[-1, 0], [0, 0], [1, 0], [1, 1]]
    ], [ # Z
        [[0, -1], [0, 0], [-1, 0], [-1, 1]],
        [[-1, -1], [0, -1], [0, 0], [0, 1]],
        [[0, -1], [0, 0], [-1, 0], [-1, 1]],
        [[-1, -1], [0, -1], [0, 0], [0, 1]]
    ], [ # O
        [[-1, -1], [-1, 0], [0, 0], [0, -1]],
        [[-1, -1], [-1, 0], [0, 0], [0, -1]],
        [[-1, -1], [-1, 0], [0, 0], [0, -1]],
        [[-1, -1], [-1, 0], [0, 0], [0, -1]]
    ], [ # S
        [[-1, -1], [-1, 0], [0, 0], [0, 1]],
        [[-1, 0], [0, 0], [0, -1], [1, -1]],
        [[-1, -1], [-1, 0], [0, 0], [0, 1]],
        [[-1, 0], [0, 0], [0, -1], [1, -1]]
    ], [ # L
        [[0, -1], [0, 0], [0, 1], [1, 1]],
        [[-1, 1], [-1, 0], [0, 0], [1, 0]],
        [[-1, -1], [-1, 0], [0, 0], [1, 0]],
        [[1, -1], [0, -1], [0, 0], [0, 1]]
    ], [ # I
        [[0, -2], [0, -1], [0, 0], [0, 1]],
        [[-2, 0], [-1, 0], [0, 0], [1, 0]],
        [[0, -2], [0, -1], [0, 0], [0, 1]],
        [[-2, 0], [-1, 0], [0, 0], [1, 0]]
    ]
]

klocek: bool = True
frame: int = 0
nastepny: int = randint(0, 6)
rotation: int = 0
pos_x: int = 5
pos_y: int = 0
score: int = 0
level: int = 0
lines: int = 0
stat: list[int] = [0, 0, 0, 0, 0, 0, 0]
jaki_klocek: int = randint(0, 6)
static: list[list[int]] = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #20
    ]
soft_drop: bool = False
while running:
    frame += 1
    A_nacisk: bool = False
    D_nacisk: bool = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: # klawisze start
            if event.key == pygame.K_d:
                D_nacisk = True
            elif event.key == pygame.K_a:
                A_nacisk = True
            elif event.key == pygame.K_s:
                soft_drop = True
            elif event.key == pygame.K_l:
                rotation += 1
            elif event.key == pygame.K_j:
                rotation -= 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                soft_drop = False
    
    if not klocek:
        jaki_klocek = nastepny
        nastepny = randint(0, 6)
    nacisk = D_nacisk + A_nacisk * 2
    if nacisk == 1:
        D_nacisk = False # D
        pos_x -= 1
    elif nacisk == 2:
        A_nacisk = False # A
        pos_x += 1
    elif nacisk == 3:
        A_nacisk = False # A + D
        D_nacisk = False
    
    if frame == klatka(level):
        if (maks(pos_y, tetromino[jaki_klocek][rotation]) != 19) & podspodem(pos_x, pos_y, tetromino[jaki_klocek][rotation]):
            pos_y += 1
        else:
            for i in tetromino:
                X = i[0]
                Y = i[1]
                static[pos_x + X][pos_y + Y] = jaki_klocek % 3 + 1

    rotation %= 4
    screen.fill("black")
    screen.blit(background, (0, 0))
    scale = N
    screen.blit(znaki.render(f"{min(999999,score):0>6}", False, (255, 255, 255)), (192 * scale, 66 * scale)) # wynik
    screen.blit(znaki.render(f"{level:0>2}", False, (255, 255, 255)), (208 * scale, 169 * scale)) # poziom
    screen.blit(znaki.render(f"{lines:0>3}", False, (255, 255, 255)), (153 * scale, 24 * scale)) # linie
    for i in range(7):
        screen.blit(znaki.render(f"{stat[i]:0>3}", False, (255, 0, 0)), (49 * scale, 95 * scale + 16 * scale * i)) # statsy
    paleta = level % 10
    for Y in range(20):
        for X in range(10):
            element = static[Y][X]
            X1, Y1 = 95 * scale + X * scale * 8, 47 * scale + Y * scale * 8 # pozycja w px
            kolor = pygame.Color(kolory_11(element, paleta))
            if element == 0:
                pygame.draw.polygon(screen, "black", [(X1 + scale, Y1 + scale), (X1 + scale * 8, Y1 + scale), (X1 + scale * 8, Y1 + scale * 8), (X1 + scale, Y1 + scale * 8)])
            elif element == 1:
                pygame.draw.polygon(screen, kolor, [(X1 + scale, Y1 + scale), (X1 + scale * 8, Y1 + scale), (X1 + scale * 8, Y1 + scale * 8), (X1 + scale, Y1 + scale * 8)])
                pygame.draw.polygon(screen, "white", [(X1 + scale, Y1 + scale), (X1 + scale * 2, Y1 + scale), (X1 + scale * 2, Y1 + scale * 2), (X1 + scale, Y1 + scale * 2)])
                pygame.draw.polygon(screen, "white", [(X1 + scale * 2, Y1 + scale * 2), (X1 + scale * 7, Y1 + scale * 2), (X1 + scale * 7, Y1 + scale * 7), (X1 + scale * 2, Y1 + scale * 7)])
            elif element == 2:
                pygame.draw.polygon(screen, kolor, [(X1 + scale, Y1 + scale), (X1 + scale * 8, Y1 + scale), (X1 + scale * 8, Y1 + scale * 8), (X1 + scale, Y1 + scale * 8)])
                pygame.draw.polygon(screen, "white", [(X1 + scale, Y1 + scale), (X1 + scale * 2, Y1 + scale), (X1 + scale * 2, Y1 + scale * 2), (X1 + scale, Y1 + scale * 2)])
                pygame.draw.polygon(screen, "white", [(X1 + scale * 2, Y1 + scale * 2), (X1 + scale * 4, Y1 + scale * 2), (X1 + scale * 4, Y1 + scale * 3), (X1 + scale * 3, Y1 + scale * 3), (X1 + scale * 3, Y1 + scale * 4), (X1 + scale * 2, Y1 + scale * 4), (X1 + scale * 2, Y1 + scale * 2)])
            elif element == 3:
                pygame.draw.polygon(screen, kolor, [(X1 + scale, Y1 + scale), (X1 + scale * 8, Y1 + scale), (X1 + scale * 8, Y1 + scale * 8), (X1 + scale, Y1 + scale * 8)])
                pygame.draw.polygon(screen, "white", [(X1 + scale, Y1 + scale), (X1 + scale * 2, Y1 + scale), (X1 + scale * 2, Y1 + scale * 2), (X1 + scale, Y1 + scale * 2)])
                pygame.draw.polygon(screen, "white", [(X1 + scale * 2, Y1 + scale * 2), (X1 + scale * 4, Y1 + scale * 2), (X1 + scale * 4, Y1 + scale * 3), (X1 + scale * 3, Y1 + scale * 3), (X1 + scale * 3, Y1 + scale * 4), (X1 + scale * 2, Y1 + scale * 4), (X1 + scale * 2, Y1 + scale * 2)])
    for i in tetromino[jaki_klocek][rotation]:
        kolor = pygame.Color(kolory_11(jaki_klocek % 3 + 1, paleta))
        X1, Y1 = pos_x + i[0], pos_y + i[1]
        kocek = jaki_klocek % 3
        match kocek:
            case 0:
                pygame.draw.polygon(screen, kolor, [(X1 + scale, Y1 + scale), (X1 + scale * 8, Y1 + scale), (X1 + scale * 8, Y1 + scale * 8), (X1 + scale, Y1 + scale * 8)])
                pygame.draw.polygon(screen, "white", [(X1 + scale, Y1 + scale), (X1 + scale * 2, Y1 + scale), (X1 + scale * 2, Y1 + scale * 2), (X1 + scale, Y1 + scale * 2)])
                pygame.draw.polygon(screen, "white", [(X1 + scale * 2, Y1 + scale * 2), (X1 + scale * 7, Y1 + scale * 2), (X1 + scale * 7, Y1 + scale * 7), (X1 + scale * 2, Y1 + scale * 7)])
            case 1:
                pygame.draw.polygon(screen, kolor, [(X1 + scale, Y1 + scale), (X1 + scale * 8, Y1 + scale), (X1 + scale * 8, Y1 + scale * 8), (X1 + scale, Y1 + scale * 8)])
                pygame.draw.polygon(screen, "white", [(X1 + scale, Y1 + scale), (X1 + scale * 2, Y1 + scale), (X1 + scale * 2, Y1 + scale * 2), (X1 + scale, Y1 + scale * 2)])
                pygame.draw.polygon(screen, "white", [(X1 + scale * 2, Y1 + scale * 2), (X1 + scale * 4, Y1 + scale * 2), (X1 + scale * 4, Y1 + scale * 3), (X1 + scale * 3, Y1 + scale * 3), (X1 + scale * 3, Y1 + scale * 4), (X1 + scale * 2, Y1 + scale * 4), (X1 + scale * 2, Y1 + scale * 2)])
            case 2:
                pygame.draw.polygon(screen, kolor, [(X1 + scale, Y1 + scale), (X1 + scale * 8, Y1 + scale), (X1 + scale * 8, Y1 + scale * 8), (X1 + scale, Y1 + scale * 8)])
                pygame.draw.polygon(screen, "white", [(X1 + scale, Y1 + scale), (X1 + scale * 2, Y1 + scale), (X1 + scale * 2, Y1 + scale * 2), (X1 + scale, Y1 + scale * 2)])
                pygame.draw.polygon(screen, "white", [(X1 + scale * 2, Y1 + scale * 2), (X1 + scale * 4, Y1 + scale * 2), (X1 + scale * 4, Y1 + scale * 3), (X1 + scale * 3, Y1 + scale * 3), (X1 + scale * 3, Y1 + scale * 4), (X1 + scale * 2, Y1 + scale * 4), (X1 + scale * 2, Y1 + scale * 2)])

                
    pygame.display.flip() # update screen

    clock.tick(60.0988) # frame rate

pygame.quit()
print(f"Wynik = {score:.0f}")
