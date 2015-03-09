import eventhandlers
import threading
import psutil
from event.winservice import Service
from logger import Logger
from jsonconfig import JsonConfig
from event import Event

__company__ = 'Boulder Environmental Sciences and Technology'
__project__ = ''
__author__ = 'Y. Shao'
__created__ = '3/2/2015' '2:36 PM'

def find_pid():
    ""

def create_daemon(evt):
    ""
    func=evt['action']
    t=threading.Thread(evt,time=evt['interval'])
    t.start()
    pid=t.pid
    return pid


class EventSystem(Service):
    def __init__(self):
        config=JsonConfig('event.json')
        self.pid={}
        self.l=Logger('weatherevent')

        for c in config:
            evt= Event(c)
            if evt['type'] == 'daemon':
                if not self.find_pid():
                    pid=create_daemon()

                    self.pid[evt['event']]=pid
            else:
                status=evt['status']
                status=getattr(eventhandlers,status)
                action=evt['action']
                action=getattr(eventhandlers,action)
                res=status()
                if not res:
                    action()

    def status(self):
        d={}
        for p in self.pid:
            d[p]={}
            d[p]['running']=psutil.find(p)

    def start(self):
        ""
        self.runflag=True
        while self.runflag:
        # self.runflag=True
        # while self.runflag:
            self.log("Event System On")

    def stop(self):
        ""
        self.log("I'm done")

    def find_pid(self):
        ""
        return self.pid.has_key('pid') != None

    def setLogger(self):
        ""



# winservice_test.py



# class Test(Service):
#     def start(self):
#         self.runflag=True
#         while self.runflag:
#             self.sleep(10)
#             self.log("I'm alive ...")
#     def stop(self):
#         self.runflag=False
#         self.log("I'm done")


