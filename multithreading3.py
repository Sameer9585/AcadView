from threading import *


class Mamta(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print("\n\t Hello run function "+str(self.name))


def main():
    sameer=Mamta("sameer")
    komal=Mamta("komal")
    sameer.start()
    komal.start()
