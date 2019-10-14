from multiprocessing import Process, Event
import time
import pygame
import sys

sys.argv = ['openvibe']
path_initial = r'D:\UDEA-MAESTRIA\Result\Set Stimuli\OpenDesigner\Acuity_image/'
scale_acuity = ['A5.8', 'A2.9', 'A1.8', 'A1.1', 'A0.7', 'A0.4', 'A0.2']
time_initial = 4
time_stimuli = 4*len(scale_acuity)  # Each stimuli take 4 s



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
        while not self.stop_asked.is_set():
            self.process()
        self.uninitialize()


class Change(OVProcess):
    def __init__(self):
        OVProcess.__init__(self)
        self.screen = None
        self.img = None
        self.pos = [320, 240]
        self.speed = 5
        self.dirx = -self.speed
        self.diry = -self.speed
        self.state = True
        self.img2 = None


    def initialize(self):
        pygame.init()
        pygame.display.set_caption(self.name)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.screen = pygame.display.set_mode((640, 480))
        self.img = pygame.image.load(r'D:\UDEA-MAESTRIA\Result\Set Stimuli\OpenDesigner\Acuity_image/A5.8.png')
        self.img2 = pygame.image.load(r'D:\UDEA-MAESTRIA\Result\Set Stimuli\OpenDesigner\Acuity_image/0.png')

    def image_change(self, path):
        self.img = pygame.image.load(path)

    def image_wait(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def process(self):
        self.state = not self.state
        if self.state:
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.img, (0, 0))
        else:
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.img2, (0, 0))
        pygame.display.update()


class MyOVBox(OVBox):
    def __init__(self):
        OVBox.__init__(self)
        self.p = None
        self.screen = None
        self.number_image = 1
        self.path = ''
        self.active = False

    def initialize(self):
        self.p = Change()
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
                        self.p.process()
                        value = stim.date % time_initial
                        if value == 0:
                            if self.number_image == len(scale_acuity):
                                self.number_image = 0
                            self.path = path_initial + scale_acuity[self.number_image] + '.png'
                            self.p.image_change(self.path)
                            self.number_image += 1
            if (type(chunk2) == OVStimulationSet):
                for stimIdx2 in range(len(chunk2)):
                    stim2 = chunk2.pop()
                    #print 'Received stim', stim2.identifier, 'stamped at', stim2.date, 's'
                    if stim2.date == time_initial:
                        self.active = True
                    elif stim2.date == time_stimuli + time_initial:
                        self.active = False
                        self.p.image_wait()
                    elif stim2.date == time_stimuli*2 + time_initial:
                        self.active = True
                    elif stim2.date == time_stimuli*3 + time_initial:
                        self.active = False
                        self.p.image_wait()
                    elif stim2.date == time_stimuli*4 + time_initial:
                        self.active = True
                    elif stim2.date == time_stimuli*5 + time_initial:
                        self.active = False
                        self.p.image_wait()


        return



    def uninitialize(self):
        self.p.stop()
        self.p.join()
        pygame.quit()


if __name__ == '__main__':
    box = MyOVBox()
