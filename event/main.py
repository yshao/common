from event.eventsystem import EventSystem
from winservice import Service, instart

class EventSystemService(Service):
    def start(self):
        self.runflag=True
        while self.runflag:
            ev=EventSystem()
            ev.setLogger(self.log)

            self.log("I'm alive ...")
    def stop(self):
        self.runflag=False
        self.log("I'm done")

if __name__ == '__main__':
    # instart(Test, 'aTest', 'Python Service Test')
    instart(EventSystemService)
    # main=EventSystem()
    # daemon=daemonize(main)
    # daemon.start()