from threading import Thread
from time import sleep


def first_thread_func():
    first_thread_index: int = 0
    for _ in range(100):
        first_thread_index += 1
        print(f"first_thread_index={first_thread_index}")
        sleep(0.01)


def second_thread_func():
    second_thread_index: int = 0
    for _ in range(100):
        second_thread_index += 1
        print(f"second_thread_index={second_thread_index}")
        sleep(0.01)


first_thread = Thread(target=first_thread_func)
second_thread = Thread(target=second_thread_func)
first_thread.start()
second_thread.start()
