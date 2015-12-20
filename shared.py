#-*- coding: utf-8 -*-
from traits.api import *
from traitsui.api import *
import multiprocessing as mp
from multiprocessing.managers import SyncManager

class Shared(HasTraits):
    manager = Instance(SyncManager, transient = True)

    def __init__(self, ncpu=1):
        self.manager = mp.Manager()
        self.populate()

    def populate(self):
        self.running = self.manager.Value('i', 0)
        self.iteration = self.manager.Value('i', 0)
        self.wlist = self.manager.list([])
        self.tlist = self.manager.list([])
        self.vlist = self.manager.list([])
        self.ilist = self.manager.list([])


if __name__ == "__main__":
    s = Shared()
    def func(s):
        s.value = 1
        s.running.value = 1
    p = mp.Process(target=func, args=(s,))
    p.start()
    p.join()
    print s.running.value == 1
    print hasattr(s, 'value')