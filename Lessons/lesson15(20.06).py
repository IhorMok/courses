# import time
# import _thread
#
# print(dir(_thread))
#
# lock = _thread.allocate()
#
# def worker(id):
#     lock.acquire()
#     time.sleep(2)
#     print(_thread.get_ident())
#     lock.release()
#
# for i in range(5):
#     _thread.start_new_thread(worker, (i,))
#
# time.sleep(10)

import time
from threading import Thread, Lock

count = 0


lock = Lock()

def worker():
    global count
    for _ in range(5):
        with lock:
            count += 1
            time.sleep(.001)
            print(count)
            count += 1

threads = []

for i in range(10):
    thread = Thread(name=f'{i}', target=worker, args=())
    threads.append(thread)


for thread in threads:
    thread.start()

# for thread in threads:
#     thread.join()

print(count)