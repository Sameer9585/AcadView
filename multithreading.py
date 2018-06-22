from threading import *

def first():
    
    print("\n\tHello first run by "+str(current_thread().getName()))




def second():
    print("\n\tHello second run by "+str(current_thread().getName()))



def three():
    first()
    second()
