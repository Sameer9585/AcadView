from threading import *


def first():
    i=1
    while(i<=10):
        print("\n\t Hello first run by "+str(current_thread().getName()))
        i=i+1


def second():
    i=1
    while(i<=10):
        print("\n\t Hello second run by "+str(current_thread().getName()))
        i=i+1

def three():
    t1=Thread(target=first)
    t2=Thread(target=second)
    t1.start()
    t2.start()
