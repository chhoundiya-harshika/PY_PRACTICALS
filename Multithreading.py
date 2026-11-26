# in a process multiple threads are running then its called multhreading
# if multipalethread running simultaneously called multitasking
import time
def task1():
    print("T1 started:")
    time.sleep(2)
    print("T1 completed:")
def task2():
    print("T2 started:")
    time.sleep(2)
    print("T2 completed:")
task1()
task2()
    