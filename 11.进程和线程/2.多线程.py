import time,threading


#新线程执行的代码
# def loop():
#     print("thread %s is running..."  % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print("thread %s >>> %s" % (threading.current_thread().name, n))
#         time.sleep(1)
#     print("thread %s ended" % threading.current_thread().name)
#
# print("threading %s is running..." % threading.current_thread().name)
# t = threading.Thread(target=loop, name="LoopThread")
# t.start()
# t.join()
# print("thread %s ended" % threading.current_thread().name)

# #假定这是你的银行存款
# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     #先存后取，结果应该为0
#     global balance
#     balance += n
#     balance -= n
#
# def run_thread(n):
#     for i in range(1000000):
#         #先要获取锁
#         lock.acquire()
#         #我们用try...finally来确保锁一定会被释放
#         try:
#             change_it(n)
#         finally:
#             lock.release()
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(6,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# #!!!死循环 由于Python GIL锁的问题 可以使用多线程 但是多线程是不可能在python中并发的 但是多进程可以
# import threading,multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()