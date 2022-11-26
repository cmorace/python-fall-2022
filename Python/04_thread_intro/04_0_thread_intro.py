

first_thread_index: int = 0

second_thread_index: int = 0

for _ in range(100):
    first_thread_index += 1
    print(f"first_thread_index={first_thread_index}")

for _ in range(100):
    second_thread_index += 1
    print(f"second_thread_index={second_thread_index}")
