# in a process multiple threads are running then its called multhreading
# if multipalethread running simultaneously called multitasking
# import time
# def task1():
#     print("T1 started:")
#     time.sleep(2)
#     print("T1 completed:")
# def task2():
#     print("T2 started:")
#     time.sleep(2)
#     print("T2 completed:")
# task1()
# task2()

import threading
import time
def greet():
    print("Hello from the thread")
    time.sleep(5)
    print("after waiting Hello from the thread")
def greet1():
    print("Hello from the thread 1")
def greet2():
    print("Hello from the thread 2")
t=threading.Thread(target=greet)
t1=threading.Thread(target=greet1)
t2=threading.Thread(target=greet2)
t.start()
t1.start()
t2.start()
print("")