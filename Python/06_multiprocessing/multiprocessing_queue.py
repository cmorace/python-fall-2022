from pycat.core import Window

import multiprocessing as mp


def foo(q):
    q.put('hello')
    w = Window()
    w.run()


if __name__ == '__main__':
    print(mp.cpu_count())
    mp.set_start_method('spawn')
    q = mp.Queue()
    p1 = mp.Process(target=foo, args=(q,))
    p1.start()
    print(q.get())
    p2 = mp.Process(target=foo, args=(q,))
    p2.start()
    print(q.get())

    p1.join()
    p2.join()
