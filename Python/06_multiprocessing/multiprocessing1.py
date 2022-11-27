from pycat.core import Window
import multiprocessing

data = "testing"


def foo(x):
    global data
    data = "foo"
    print("foo")
    w = Window(100, 100)
    w._window.set_location(x, 0)
    w.set_clear_color(255, 255, 255)
    w.run()


def bar():
    global data
    data = "bar"
    print("bar")
    w = Window(100, 100)
    w.set_clear_color(255, 0, 255)
    w.run()


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    for i in range(10):
        p1 = multiprocessing.Process(target=foo, args=(i*100,))
        p1.start()
