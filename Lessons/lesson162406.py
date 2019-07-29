# import  time
# import queue
#
# from functools import partial
#
# from threading import Thread, Timer, Lock
#
#
#
#
# def  callback(i):
#     print(i)
#
# t = Timer(10, callback)
# t.start()
# t.join()
#
#
#
# class SetInterval(Thread):
#     def __init__(self, callback, *args, **kwargs):
#         super().__init__(*args,  **kwargs)
#         self.lock = Lock()
#         self.callback = callback
#         self.count = 0
#
#
#     def run(self):
#         while True:
#             time.sleep(1)
#             callback = partial(self.callback, self.count)
#             with self.lock:
#                 t = Timer(.5, callback)
#                 t.start()
#                 self.count += 1
#
#
# t = SetInterval(callback, daemon=True)
# t.start()
#
# time.sleep(4)
#===============================================

# import time
# import queue
#
# from threading import Thread, Lock
#
#
#
#
# q = queue.Queue(5)
# lock = Lock()
#
#
# def writer_worker(q):
#     for i in range(10):
#         try:
#             q.put(i)
#             # q.put(block=False, timeout=1)
#         except queue.Full:
#             return
#
# def reader_worker(q):
#     while True:
#         try:
#             time.sleep(0.5)
#             item = q.get(timeout=0.5)
#             print(item)
#         except queue.Empty:
#             return
#
#
#
# w = Thread(target=writer_worker, args=(q,))
# r = Thread(target=reader_worker, args=(q,))
#
# w.start()
# r.start()
#
# w.join()
# r.join()


#============================================

import argparse

parser = argparse.ArgumentParser()                               # дає можливість читати аргумент командного рядка choices=(345, '345')
parser.add_argument('-l', '--len', )            # 1 імя аргументу командного рядка  #action='source' значення у терміналі запишеться
print(parser.parse_args().len)