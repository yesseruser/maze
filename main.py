import pygame
map = [
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [2, 1, 1, 1, 3, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
       [2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
       [2, 1, 2, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
       [2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
       [2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
       [2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
       [2, 1, 1, 3, 2, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
       [2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
       [2, 1, 2, 3, 3, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
       [2, 1, 2, 3, 3, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    ]

pygame.init()

money_count = 0
font = pygame.font.SysFont("consolas", 40)

window = pygame.display.set_mode((1200, 600))

empty = pygame.image.load("img/1.png")
wall = pygame.image.load("img/2.png")
money = pygame.image.load("img/3.png")
finish = pygame.image.load("img/4.png")

character = pygame.image.load("img/character.png")
character_x = 1
character_y = 10

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if map[character_y][character_x + 1] != 2:
                    character_x += 1
            elif event.key == pygame.K_LEFT:
                if map[character_y][character_x - 1] != 2:
                    character_x -= 1
            elif event.key == pygame.K_DOWN:
                if map[character_y + 1][character_x] != 2:
                    character_y += 1
            elif event.key == pygame.K_UP:
                if map[character_y - 1][character_x] != 2:
                    character_y -= 1
            if map[character_y][character_x] == 3:
                map[character_y][character_x] = 1
                money_count += 1
            for y in range(0, 12, 1):
                for x in range(0, 24, 1):
                    space = map[y][x]
                    if space == 1:
                        window.blit(empty, (x * 50, y * 50))
                    elif space == 2:
                        window.blit(wall, (x * 50, y * 50))
                    elif space == 3:
                        window.blit(money, (x * 50, y * 50))
                    elif space == 4:
                        window.blit(finish, (x * 50, y * 50))
    window.blit(character, (character_x * 50, character_y * 50))
    window.blit(font.render(str(money_count), True, (255, 255, 255)), (400, 15))

    pygame.display.flip()