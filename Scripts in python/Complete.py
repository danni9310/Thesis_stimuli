import pygame
import move
import time
import cv2
import sys


pathVideos = 'D:/Proyecto visual Daniela Ortega/Videos/'
fs = 7.5
cam = 0



def status_process(): 
    for event in pygame.event.get():
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            sys.exit("Error message")

    
#%% Scripy acuity

black = (0, 0, 0)
white = (255, 255, 255)
timer = time.time()
time_to_wait = 10
 
color = white

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()
screen.fill(black)
pygame.draw.rect(screen, white, [0, 0, 10, 10])
pygame.display.flip()

active = False
wait = False

# Configure video 

cap = cv2.VideoCapture(cam)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter( pathVideos + 'acuity.avi',fourcc, fs, (640,480))

while not wait:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            done = False
            print('enstro space')
            wait = True

clock = pygame.time.Clock()
scale_acuity = ['A5.8', 'A2.9', 'A1.8', 'A1.1','A0.7', 'A0.4', 'A0.3']

timer_init = time.time()

while(cap.isOpened()):

    for i in range(0, 3):
        timer = time.time()
        
        for scale in scale_acuity:
            img = pygame.image.load('./Acuity_image/'+ scale +'.png')
            timer = time.time()
            done = False
            while not done:
                #status_process()
                timer2 = time.time() - timer
                ret, frame = cap.read()
                out.write(frame)

                if timer2 > 20:
                    done = True
                for event in pygame.event.get():  # User did something
                    if event.type == pygame.QUIT:  # If user clicked close
                        done = True  # Flag that we are done so we exit this loop
                # Set the screen background
                if color == white:
                    screen.blit(img, (0, 0))
                    color = black
                else:
                    color = white
                    screen.fill(color)
        
                pygame.display.flip()
                clock.tick(7.5)
        
        """Time to wait """
        timer = time.time()
        time_last = 0
        
        while time_last <= time_to_wait :
            #status_process()
            screen.fill(black)
            pygame.display.flip()
            time_last = time.time() - timer

    break

print('Final time:' + str(time.time()-timer_init))
cap.release()
out.release()
cv2.destroyAllWindows()
#%% Scripy contrast
    
black = (0, 0, 0)
white = (255, 255, 255)
timer = time.time()
time_to_wait = 10
 
color = white

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()
screen.fill(black)
pygame.draw.rect(screen, white, [0, 0, 10, 10])
pygame.display.flip()

active = False
wait = False

# Configure video 

cap = cv2.VideoCapture(cam)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter( pathVideos + 'contrast.avi',fourcc, fs, (640,480))



while not wait:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            done = False
            wait = True

clock = pygame.time.Clock()

timer_init = time.time()

while(cap.isOpened()):
    
    for i in range(0, 3):
        timer = time.time()
        
        for scale in range(8,13):
            img = pygame.image.load('./Contrast_image/'+ str(scale) +'.png')
            timer = time.time()
            done = False
            while not done:
                #status_process()
                timer2 = time.time() - timer
                ret, frame = cap.read()
                out.write(frame)
                
                if timer2 > 4:
                    done = True
                for event in pygame.event.get():  # User did something
                    if event.type == pygame.QUIT:  # If user clicked close
                        done = True  # Flag that we are done so we exit this loop
                # Set the screen background
                if color == white:
                    screen.blit(img, (0, 0))
                    color = black
                else:
                    color = white
                    screen.fill(color)
        
                pygame.display.flip()
                clock.tick(7.5)
        
        """Time to wait """
        timer = time.time()
        time_last = 0
        
        while time_last <= time_to_wait :
            #status_process()
            screen.fill(black)
            pygame.display.flip()
            time_last = time.time() - timer
        print(time_last)

    break

print('Final time:' + str(time.time()-timer_init))

cap.release()
out.release()
cv2.destroyAllWindows()


#%% Script visual field 

timer = time.time()
time_to_wait = 10

# Screen size
width = 1680
height = 1050
black = (0, 0, 0) 
white = (250, 250, 250)
red = (255, 0, 0)

""" Configure square movement stimule"""

# Configure color of object and size
size_x = 60
size_y = 60

# Configure parameters for movement
speed_x = 10
speed_y = 10


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()
screen.fill(black)
pygame.draw.rect(screen, white, [0, 0, 10, 10])
pygame.display.flip()

# Wait the instruction in keyboard

active = False
wait = False
done = False
change = True

cont = 0
key_pressed = []

# Configure video 

cap = cv2.VideoCapture(cam)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter( pathVideos + 'field.avi',fourcc, fs, (640,480))


while not wait:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            active = True
            wait = True

clock = pygame.time.Clock()

scale_x = int(width/6)
scale_y = int(height/6)

position_x = width / 2 - 10 // 2
position_y = height / 2 - 10 // 2

change_x = [scale_x*3,
            scale_x*2,
            scale_x,
            scale_x*4,
            0,
            width-size_x]
change_y = [scale_y,
            scale_y*5,
            scale_y*3,
            height-size_y,
            0]

timer_init = time.time()

while(cap.isOpened()):
    
    for i in range(0, 3):
        timer = time.time()
    
        for change_move_x in change_x:
            for change_move_y in change_y:
                timer = time.time()
                time_last = 0
                active = True
                cont += 1
                while active:
                    #status_process()
                    ret, frame = cap.read()
                    out.write(frame)
                    if time_last <= 2: 
                        time_last = time.time() - timer
                    else:
                        time_last = 0
                        active = False
    
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            key_pressed.append(cont)
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            cap.release()
                            out.release()
                            cv2.destroyAllWindows()
                            sys.exit("Error message")
    
                    if change:
                        screen.fill(black)
                        pygame.draw.rect(screen, red, [position_x, position_y, 10, 10])
                        pygame.display.flip()
                        change = False
                    else:
                        pygame.draw.rect(screen, red, [position_x, position_y, 10, 10])
                        pygame.draw.rect(screen, white, [change_move_x, change_move_y, size_x, size_y])
                        pygame.display.flip()
                        change = True
    
                    clock.tick(10)
    
                """Time to wait """
        timer = time.time()
        time_last = 0
    
        while time_last <= time_to_wait:
            #status_process()
            screen.fill(black)
            pygame.display.flip()
            time_last = time.time() - timer
    
        print (key_pressed)
    
        with open(pathVideos + 'visual_field' + str(i) + '.txt', 'w') as f:
            for item in key_pressed:
                f.write("%s\n" % item)
    
        cont = 0
        key_pressed = []

    break

print('Final time:' + str(time.time()-timer_init))

cap.release()
out.release()
cv2.destroyAllWindows()


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
    for direction in stimule:
        #status_process()
        move.Square(screen, speed_x, speed_y, False, direction, width, height, size_y, size_x)
   
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
            if active:
                #status_process()
                timer = time.time()
                for i in range(1,5):
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
                print(time_last)

                timer = time.time()
                for j in range(5,12):
                    imagen = './Formas/' + str(k) + '/' + str(j) + '.png'
                    img = pygame.image.load(imagen)
                    clock = pygame.time.Clock()
                    state = True
                    scale = 1
                    while state:
                        screen.fill((255, 255, 255))
                        scale -= scale_transform
                        img_width = int(img.get_width()*scale)
                        img_height = int(img.get_height()*scale)
                        if img_width <= 10 or img_height <= 10:
                            state = False
                        img = pygame.transform.scale(img, (img_width, img_height))
                        position_x = width / 2 - img.get_width() // 2
                        position_y = height / 2 - img.get_height() // 2
                        screen.blit(img, (position_x, position_y))
                        pygame.display.flip()
                        clock.tick(2)
                time_last = time.time() - timer
                print(time_last)

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

for i in range(0, 3):
    timer = time.time()

    if active:
        """ Move words """
        timer = time.time()

        speed_x = 5
        speed_y = 5
        directions = ("right", "left", "right", "left", "right", "right", "left", "left", "right", "left", "right", "left", "left", "right",  "left", "right", "left", "right", "left", "right", "left", "left", "right", "right", "left", "right", "left")
        texts = ("LA", "EN", "ES", "UN", "CASA", "LUNA", "ALTO", "HOJA", "ZAPATO", "CUADERNO", "CABEZA", "FAMILIA")

        for text, direction in zip(texts, directions):
            #status_process()
            move.Words(screen, text,  speed_x, speed_y, False, direction, width, height, size=100)
            time.sleep(1)

        time_last = time.time() - timer
        print (time_last)

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

color_plain = (blue, red, green, yellow, black)

while wait == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            active = True
            wait = True

timer_init = time.time()

for i in range(0, 3):
    timer = time.time()

    for color_use in color_plain:
        screen.fill(color_use)
        pygame.display.flip()
        time.sleep(5)

    for color_use in color_plain:
        timer = time.time()
        time_last = 0
        while time_last <= 5:
            #status_process()
            time_last = time.time() - timer
            screen.fill(color_use)
            pygame.display.flip()
            time.sleep(1)
            screen.fill(black)
            pygame.display.flip()
            time.sleep(1)

    if active:

        """Strop"""
        size_letter = 100
        texts = ("AMARILLO", "AZUL", "NARANJA", "NEGRO", "ROJO", "VERDE", "MORADO", "AMARILLO", "ROJO", "NARANJA", "VERDE", "NEGRO", "AZUL", "ROJO", "MORADO" )
        colors = (green, red, blue, yellow, blue, black, red, blue, green, black, red, yellow, green, blue, black)
        screen.fill((255,255,255))


        for word, color in zip(texts, colors):
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

for k in range(1, 3):
    timer = time.time()
    if active:

        while state:
            #status_process()
            time_last = time.time() - timer
            if time_last >= 10:
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

        while time_last <= time_to_wait :
            #status_process()
            screen.fill(black)
            pygame.display.flip()
            time_last = time.time() - timer
            state = True 

print('Final time:' + str(time.time()-timer_init))


pygame.quit()

