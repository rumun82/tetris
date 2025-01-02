from random import randint
import pygame

def kolory_11(element, palet):
    kolory = [(0, 89, 248), (66, 184, 255), (0, 169, 0), (178, 248, 27), (218, 0, 204), (249, 121, 246), (2, 88, 248), (89, 217, 90), (226, 0, 88), (89, 250, 157), (88, 248, 158), (107, 132, 254), (252, 52, 8), (125, 125, 125), (103, 69, 251), (176, 0, 31), (0, 89, 248), (244, 58, 2), (250, 53, 3), (252, 160, 68)]
    if element == 2:
        return kolory[palet * 2 + 1]
    else:
        return kolory[palet * 2]

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
wymiary = (256 * N, 240 * N)
pygame.init()
screen = pygame.display.set_mode(wymiary)
clock = pygame.time.Clock()
running = True
znaki = pygame.font.Font("nintendo-nes-font.ttf", (8 * N))
background = pygame.image.load("background.bmp")
background = pygame.transform.scale(background, wymiary)

klocek = False
nastepny = randint(0, 6)
pos_x = 5
pos_y = 0
score = 0
level = 0
lines = 0
stat = [0, 0, 0, 0, 0, 0, 0]
static = [
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    screen.blit(background, (0, 0))

    scale = N
    screen.blit(znaki.render(f"{min(999999,score):0>6}", False, (255, 255, 255)), (192 * scale, 66 * scale))
    screen.blit(znaki.render(f"{level:0>2}", False, (255, 255, 255)), (208 * scale, 169 * scale))
    screen.blit(znaki.render(f"{lines:0>3}", False, (255, 255, 255)), (153 * scale, 24 * scale))
    for i in range(7):
        screen.blit(znaki.render(f"{stat[i]:0>3}", False, (255, 0, 0)), (49 * scale, 95 * scale + 16 * scale * i))
    for Y in range(20):
        for X in range(10):
            element = static[Y][X]
            paleta = level % 10
            X1, Y1 = 95 * scale + X * scale * 8, 47 * scale + Y * scale * 8
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
    
    pygame.display.flip()

    clock.tick(60.0988)

pygame.quit()
print(f"Wynik = {score:.0f}")
