import pygame
level = [
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
       [2, 1, 2, 3, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    ]

pygame.init()

clock = pygame.time.Clock()
time = 0
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

money_collect = pygame.mixer.Sound("sounds/collectcoin.wav")

for y in range(0, 12, 1):
    for x in range(0, 24, 1):
        space = level[y][x]
        if space == 1:
            window.blit(empty, (x * 50, y * 50))
        elif space == 2:
            window.blit(wall, (x * 50, y * 50))
        elif space == 3:
            window.blit(money, (x * 50, y * 50))
        elif space == 4:
            window.blit(finish, (x * 50, y * 50))

run = True
playing = False

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                if character_x < 23 and level[character_y][character_x + 1] != 2:
                    character_x += 1

            elif event.key == pygame.K_LEFT:
                if character_x > 0 and level[character_y][character_x - 1] != 2:
                    character_x -= 1

            elif event.key == pygame.K_DOWN:
                if character_y > 0 and level[character_y + 1][character_x] != 2:
                    character_y += 1

            elif event.key == pygame.K_UP:
                if character_y < 11 and level[character_y - 1][character_x] != 2:
                    character_y -= 1

            playing = True

            if level[character_y][character_x] == 3:
                level[character_y][character_x] = 1
                money_count += 1
                money_collect.play()

            if level[character_y][character_x] == 4:
                if money_count == 8:
                    run = False

    window.fill((0, 0, 0))

    for y in range(0, 12, 1):
            for x in range(0, 24, 1):
                space = level[y][x]
                if space == 1:
                    window.blit(empty, (x * 50, y * 50))
                elif space == 2:
                    window.blit(wall, (x * 50, y * 50))
                elif space == 3:
                    window.blit(money, (x * 50, y * 50))
                elif space == 4:
                    window.blit(finish, (x * 50, y * 50))
    window.blit(character, (character_x * 50, character_y * 50))
    window.blit(font.render(str(money_count), True, (0, 0, 255)), (400, 15))
    window.blit(font.render(str(time), True, (255, 0, 0)), (10, 10))

    pygame.display.flip()

    clock.tick(60)
    time += clock.get_time()
