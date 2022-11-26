from pycat.core import Window
from threading import Thread


def foo():
    w = Window()
    w.run()


if __name__ == '__main__':
    p1 = Thread(target=foo)
    p1.start()
    p2 = Thread(target=foo)
    p2.start()

    p1.join()
    p2.join()
