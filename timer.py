import time;  # This is required to include time module.
from threading import Timer
import winsound
# from csv_test import csv_to_d
from event.winservice import Service, instart


class TimerService(Service):
    def start(self):
        ""
        hello_start()
    def stop(self):
        ""


def hello(start, interval, count):
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    ticks = time.time()
    t = Timer(interval - (ticks-start-count*interval), hello, [start, interval, count+1])
    t.start()
    print "Number of ticks since 12:00am, January 1, 1970:", ticks, " #", count

    # csv_to_d('todo.csv')
    # csv_to_d('todo/boston.csv')
def hello_start():
    MINUTES=30
    dt = 1.0 * 60 * MINUTES # interval in sec
    t = Timer(dt, hello, [round(time.time()), dt, 0]) # start over at full second, round only for testing here
    t.start()

def main():
    instart(TimerService, 'besteventsystem', 'BEST Timer')

if __name__ == '__main__':
    main()