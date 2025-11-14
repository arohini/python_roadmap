import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        lock.acquire()  # Acquire the lock
        counter += 1
        lock.release()  # Release the lock

threads = []
for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter value: {counter}") # Will be 500000
