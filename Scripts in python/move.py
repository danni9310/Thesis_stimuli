import pygame

black = (0, 0, 0)
white = (255, 255, 255)

def Square(screen, speed_x, speed_y, done, direction, width, height, size_y, size_x):
    # Definimos algunos colores
    # Starting position of the rectangle
    middle_x = width/2
    middle_y = height/2
    position_x = 10
    position_y = 10
    clock = pygame.time.Clock()

    if direction == "left":
        position_x = width
    elif direction == "up":
        position_y = height
    elif direction == "diagonal_right":
        position_x = 1000
        position_y = 0

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
        # Set the screen background
        screen.fill(black)
        if direction == "right":
            position_y = middle_y
            position_x += speed_x
        elif direction == "down":
            position_x = middle_x
            position_y += speed_y
        elif direction == "diagonal_left":
            position_x += speed_x
            position_y += speed_y
        elif direction == "left":
            position_y = middle_y
            position_x -= speed_x
        elif direction == "up":
            position_x = middle_x
            position_y -= speed_y
        elif direction == "diagonal_right":
            position_x -= speed_x
            position_y += speed_y

        pygame.draw.rect(screen, white, [position_x, position_y, size_x, size_y])
        pygame.display.flip()

        if position_x >= width or position_y >= height or position_x <= 0 or position_y < 0:
            done = True

        clock.tick(60)


def Words(screen, texts, speed_x, speed_y, done, directions, width, height,size ):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", size, bold=True)
    position_x = 0
    if directions == "left":
        position_x = width

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
        screen.fill(black)
        text = font.render(texts, True, white) # Configure color of word
        position_y = height/2 - text.get_height() // 2
        screen.blit(text,(position_x, position_y))
        pygame.display.flip()
        if directions == "right":
            position_x += speed_x
        elif directions == "left":
            position_x -= speed_x

        if position_x >= width or position_x <= -400:
            done = True
        clock.tick(60)
