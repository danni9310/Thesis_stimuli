from multiprocessing import Process, Event
import time
import pygame
import sys

sys.argv = ['openvibe']

# Time to wait before to star the stiumule and duration of each square
time_initial = 4

# Size for screen
width = 1680
height = 1050

size_x = 60
size_y = 60
# Position for change
scale_x = int(width / 6)
scale_y = int(height / 6)
change_x = [scale_x * 2, scale_x, scale_x * 4, 0, width - size_x]
change_y = [scale_y, scale_y * 4, scale_y * 2, height - size_y, 0]

total_time = len(change_y)*len(change_x)*time_initial

class OVProcess(Process):
    def __init__(self):
        Process.__init__(self)
        self.initialized = Event()
        self.stop_asked = Event()

    def initialize(self):
        pass

    def process(self):
        pass

    def uninitialize(self):
        pass

    def stop(self):
        self.stop_asked.set()

    def run(self):
        self.initialize()
        self.initialized.set()
        print('corre')
        while not self.stop_asked.is_set():
            self.process()
        self.uninitialize()


class Field(OVProcess):
    def __init__(self):
        OVProcess.__init__(self)
        self.screen = None
        self.img = None
        self.state = True
        self.position_x = width / 2 - 10 // 2
        self.position_y = height / 2 - 10 // 2


    def initialize(self):
        pygame.init()
        pygame.display.set_caption(self.name)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
       # self.screen = pygame.display.set_mode((640, 480))

    def image_wait(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def move_square(self, change_x, change_y):
        self.state = not self.state
        if self.state:
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (255, 0, 0), [self.position_x, self.position_y, 10, 10])
        else:
            pygame.draw.rect(self.screen, (255, 0, 0), [self.position_x, self.position_y, 10, 10])
            pygame.draw.rect(self.screen, (255, 255, 255), [change_x, change_y, size_x, size_y])
        pygame.display.update()


class MyOVBox(OVBox):
    def __init__(self):
        OVBox.__init__(self)
        self.p = None
        self.screen = None
        self.active = False
        self.change_move_x = 0
        self.change_move_y = 0
        self.vector_x = 0
        self.vector_y = 0

    def initialize(self):
        self.p = Field()
        self.p.initialize()
        self.p.start()

    def process(self):
        for chunkIndex, chunkIndex2 in zip(range(len(self.input[0])), range(len(self.input[1]))):
            chunk = self.input[0].pop()
            chunk2 = self.input[1].pop()
            if (type(chunk) == OVStimulationSet):
                for stimIdx in range(len(chunk)):
                    stim = chunk.pop()
                    if self.active:
                        self.p.move_square(self.change_move_x, self.change_move_y)


            if (type(chunk2) == OVStimulationSet):
                for stimIdx2 in range(len(chunk2)):
                    stim2 = chunk2.pop()
                    print 'Received stim', stim2.identifier, 'stamped at', stim2.date, 's'
                    self.vector_y += 1
                    if self.vector_y >= len(change_y):
                        self.vector_y = 0
                        self.vector_x += 1
                        if self.vector_x >= len(change_x):
                            self.vector_x = 0
                            self.vector_y = 0
                            self.active = False
                    self.change_move_x = change_x[self.vector_x]
                    self.change_move_y = change_y[self.vector_y]

                    if stim2.date == time_initial:
                        self.active = True
                    elif stim2.date == total_time + time_initial:
                        self.active = False
                        self.p.image_wait()

        return



    def uninitialize(self):
        self.p.stop()
        self.p.join()
        pygame.quit()


if __name__ == '__main__':
    box = MyOVBox()
