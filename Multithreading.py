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

# import threading
# import time
# def greet():
#     print("Hello from the thread")
#     time.sleep(5)
#     print("after waiting Hello from the thread")
# def greet1():
#     print("Hello from the thread 1")
#     time.sleep(5)
#     print("t2after waiting Hello from the thread")
# def greet2():
#     print("Hello from the thread 2")
# t=threading.Thread(target=greet)
# t1=threading.Thread(target=greet1)
# t2=threading.Thread(target=greet2)
# t.start()
# t1.start()
# t2.start()
# t.join()
# print("Main program ended!")

# import threading 
# import time

# def greet(name,age):
#     print("Hii", name,age)
# t=threading.Thread( target=greet, args=(name:="Hrshk", age:=22))
# t.start()

# import threading
# import time
# counter=0
# def increase_counter():
#     global counter
#     for _ in range(100000):
#         counter+=1
# t=threading.Thread(target=increase_counter)      
# t1=threading.Thread(target=increase_counter)      
# t.start()
# t1.start()
# t1.join()
# print("counter",counter)

import threading 
lock=threading.Lock()
def task():
    lock.acquire()
    try:
        print("Inside locked section")
    finally:
        lock.release()