from pycat.core import Window
import multiprocessing as mp


def foo():
    print("foo")
    w = Window(100, 100)
    w.set_clear_color(255, 255, 255)
    w.run()


def bar():
    print("bar")
    w = Window(100, 100)
    w.set_clear_color(255, 0, 255)
    w.run()


if __name__ == '__main__':
    mp.set_start_method('spawn')
    p1 = mp.Process(target=foo)
    p1.start()
    p2 = mp.Process(target=bar)
    p2.start()

    p1.join()
    p2.join()
