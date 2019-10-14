from multiprocessing import Process, Event
import time
import pygame
import sys

sys.argv = ['openvibe']
path_initial = r'D:/UDEA-MAESTRIA/Result/Set Stimuli/OpenDesigner/Contrast_image/'
total_image = 6
time_initial = 4
time_stimuli = 4*total_image  # Each stimuli take 4 s



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


class Change(OVProcess):
    def __init__(self):
        OVProcess.__init__(self)
        self.screen = None
        self.img = None
        self.state = True

    def initialize(self):
        pygame.init()
        pygame.display.set_caption(self.name)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.screen = pygame.display.set_mode((640, 480))
        self.img = pygame.image.load(r'D:/UDEA-MAESTRIA/Result/Set Stimuli/OpenDesigner/Contrast_image/1.png')

    def image_change(self, path):
        self.img = pygame.image.load(path)

    def image_wait(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def process(self):
        self.state = not self.state
        if self.state:
            self.screen.blit(self.img, (0, 0))
        else:
            self.screen.fill((255, 255, 255))
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
                        if stim.date % time_initial == 0:
                            self.path = path_initial + str(self.number_image) + '.png'
                            self.p.image_change(self.path)
                            self.number_image += 1
                            if self.number_image >= total_image:
                                self.number_image = 1
            if (type(chunk2) == OVStimulationSet):
                for stimIdx2 in range(len(chunk2)):
                    stim2 = chunk2.pop()
                    print 'Received stim', stim2.identifier, 'stamped at', stim2.date, 's'
                    if stim2.date == time_initial:
                        self.active = True
                    elif stim2.date == time_stimuli + time_initial:
                        self.active = False
                        self.p.image_wait()
                    elif stim2.date == time_stimuli*2 + time_initial:
                        self.number_image = 1
                        self.active = True
                    elif stim2.date == time_stimuli*3 + time_initial:
                        self.active = False
                        self.p.image_wait()
                    elif stim2.date == time_stimuli*4 + time_initial:
                        self.number_image = 1
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
