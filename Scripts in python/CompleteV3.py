import pygame
import move
import time


#%% Script to movement stimuli

timer = time.time()
time_to_wait = 10

# Screen size
width = 1680
height = 1050
black = (0, 0, 0)
white = (250, 250, 250)
        
#Configure square movement stimule

# Configure color of object and size
size_x = 60
size_y = 60

# Configure parameters for movement
stimule = ("down", "right", "left", "diagonal_right","right", "diagonal_left", "up" , "diagonal_right", "diagonal_left", "left", "right", "down")
speed_x = 10
speed_y = 10


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()
screen.fill(black)
pygame.draw.rect(screen, white, [0, 0, 10, 10])
pygame.display.flip()

# Wait the instruction in keyboard

wait = False



while wait == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            wait = True

timer_init = time.time()

for i in range(0, 3): 
    timer_init = time.time()
    for direction in stimule:
        #status_process()
        move.Square(screen, speed_x, speed_y, False, direction, width, height, size_y, size_x)
   
    #print ('Print last' + str(time.time()-timer_init))
    #Time to wait
    timer = time.time()
    time_last = 0
    while time_last <= time_to_wait:
        #status_process()
        screen.fill(black)
        pygame.display.flip()
        time_last = time.time() - timer
    print (time_last)
    
   

                
print('Final time:' + str(time.time()-timer_init))




#%% Script for form 


timer = time.time()
time_to_wait = 10


# Screen size
width = 1680
height = 1050
black = (0, 0, 0)
white = (250, 250, 250)

# Reset time
timer = time.time()
time_last = 0
state = False
cont = 1
wait = False

scale_transform = 0.1
scale = 1
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()
screen.fill(black)
pygame.draw.rect(screen, white, [0, 0, 10, 10])
pygame.display.flip()


while not wait :
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            wait = True
            active = True
            state = True

timer_init = time.time()


for k in range(0, 3):
    timer_init = time.time()
    if active:
        #status_process()
        timer = time.time()
        for i in range(1,12):
            screen.fill((255, 255, 255))
            imagen = './Formas/' + str(k) + '/' + str(i) + '.png'
            img = pygame.image.load(imagen)
            img_width = int(img.get_width())
            img_height = int(img.get_height())
            img = pygame.transform.scale(img, (img_width, img_height))
            position_x = width / 2 - img.get_width() // 2
            position_y = height / 2 - img.get_height() // 2
            screen.blit(img, (position_x, position_y))
            pygame.display.flip()
            time.sleep(3)
        time_last = time.time() - timer
        timer = time.time()
        time_last = time.time() - timer
        print(time_last)
        #print('Final time:' + str(time.time()-timer_init))
        """Time to wait """
        timer = time.time()
        time_last = 0
    
        while time_last <= time_to_wait:
            #status_process()
            screen.fill(black)
            pygame.display.flip()
            time_last = time.time() - timer
    
        print (time_last)

print('Final time:' + str(time.time()-timer_init))

#%% Scrip for words movement 

timer = time.time()
time_to_wait = 10

# Screen size
width = 1680
height = 1050
black = (0, 0, 0)
white = (250, 250, 250)
""" Configure square movement stimule"""

# Configure color of object and size
size_x = 50
size_y = 50
initial_value = 0

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()
screen.fill(black)
pygame.draw.rect(screen, white, [0, 0, 10, 10])
pygame.display.flip()

active = False
wait = False

while wait == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            active = True
            wait = True


timer_init = time.time()
speed_x = 5
speed_y = 5
directions = ("right", "left", "right", "left", "right", "right", "left", "left", "right", "left", "right", "left", "left", "right",  "left", "right", "left", "right", "left", "right", "left", "left", "right", "right", "left", "right", "left")
all_texts = (("LA", "EN", "ES", "UN", "CASA", "LUNA", "ALTO", "HOJA", "ZAPATO", "CUADERNO", "CABEZA", "FAMILIA"),
         ("UN", "EN", "LA", "ES", "LUNA", "HOJA", "CASA", "ALTO", "CUADERNO", "CABEZA", "FAMILIA", "ZAPATO"),
         ("UN", "ES", "LA", "EN", "HOJA", "CASA", "ALTO", "LUNA", "CABEZA", "FAMILIA", "CUADERNO", "ZAPATO"))


for i in range(0, 3):
    timer = time.time()
    #timer_init = time.time()
    if active:
        """ Move words """
        timer = time.time()
        for text, direction in zip(all_texts[i], directions):
            #status_process()
            move.Words(screen, text,  speed_x, speed_y, False, direction, width, height, size=200)
            time.sleep(1)

        time_last = time.time() - timer
        print (time_last)

        #print('Final time:' + str(time.time()-timer_init))
        """Time to wait """
        timer = time.time()
        time_last = 0

        while time_last <= time_to_wait:
            #status_process()
            screen.fill(black)
            pygame.display.flip()
            time_last = time.time() - timer

        print (time_last)

print('Final time:' + str(time.time()-timer_init))
#%% Scrip for color 


timer = time.time()
time_to_wait = 10

# Screen size
width = 1680
height = 1050
black = (0, 0, 0)
white = (250, 250, 250)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

# Reset time
time_last = 0

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()
screen.fill((255,255,255))
pygame.draw.rect(screen, black, [0, 0, 10, 10])
pygame.display.flip()

active = False
wait = False

color_plain = ((blue, red, green, yellow),
               (red, green, yellow, blue),
               (green, blue, yellow, red),
               )

color_plain2 = ((green, yellow, blue, red),
               (yellow, blue, red, green),
               (red, yellow, green, blue),
               )

while wait == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            active = True
            wait = True

timer_init = time.time()

for i in range(0, 3):
    timer = time.time()
    #timer_init = time.time()
    for color_use in color_plain[i]:
        screen.fill(color_use)
        pygame.display.flip()
        time.sleep(6)

    for color_use, color_use2 in zip(color_plain[i], color_plain2[i]):
        timer = time.time()
        time_last = 0
        while time_last <= 8:
            time_last = time.time() - timer
            screen.fill(color_use)
            pygame.display.flip()
            time.sleep(1)
            screen.fill(color_use2)
            pygame.display.flip()
            time.sleep(1)

    if active:

        """Strop"""
        size_letter = 200
        texts = ("AMARILLO", "AZUL", "NARANJA", "NEGRO", "ROJO", "VERDE", "MORADO", "AMARILLO", "ROJO", "VERDE")
        colors = ((green, red, blue, yellow, blue, black, red, blue, green, blue),
                  (red, yellow, red, blue, yellow, blue, yellow, green, green, yellow),
                  (blue, black, yellow, green, black, red, yellow, black, green, red))
        screen.fill((255,255,255))


        for word, color in zip(texts, colors[i]):
            timer = time.time()
            time_last = 0
            while time_last <= 2:
                #status_process()
                time_last = time.time() - timer
                font = pygame.font.SysFont("arial", size_letter, bold = True)
                text = font.render(word, True, color)  # Configure color of word
                position_x = width / 2 - text.get_width() // 2
                position_y = height / 2 - text.get_height() // 2
                screen.blit(text, (position_x, position_y))
                pygame.display.flip()

            screen.fill((255, 255, 255))
            pygame.display.flip()
        print(time_last)

        """Time to wait """
        timer = time.time()
        time_last = 0
        print('Final time:' + str(time.time()-timer_init))
        while time_last <= time_to_wait :
            #status_process()
            screen.fill(black)
            pygame.display.flip()
            time_last = time.time() - timer
        print(time_last)

print('Final time:' + str(time.time()-timer_init))


#%% Complex Image


timer = time.time()
time_to_wait = 10

# Screen size
width = 1680
height = 1050
black = (0, 0, 0)
white = (250, 250, 250)

# Reset time
timer = time.time()
time_last = 0
state = True
cont = 1

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()
screen.fill(black)
pygame.draw.rect(screen, white, [0, 0, 10, 10])
pygame.display.flip()

active = False
wait = False

while wait == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            active = True
            wait = True
            
timer_init = time.time()     

for k in range(1, 4):
    timer = time.time()
    timer_init = time.time()
    if active:

        while state:
            #status_process()
            time_last = time.time() - timer
            if time_last >= 5:
                if cont <= 12:
                    time_last = 0
                    timer = time.time()
                    imagen = './Imagenes/' + str(k) + '/' + str(cont) + '.jpg'
                    img = pygame.image.load(imagen)
                    img = pygame.transform.scale(img, (width, height))
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    cont += 1
                else:
                    state = False
                    cont = 1
        """Time to wait """

        timer = time.time()
        time_last = 0
        print('Final time:' + str(time.time()-timer_init))
        while time_last <= time_to_wait :
            #status_process()
            screen.fill(black)
            pygame.display.flip()
            time_last = time.time() - timer
            state = True 

print('Final time:' + str(time.time()-timer_init))


pygame.quit()

