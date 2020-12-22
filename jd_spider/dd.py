import time
from threading import Thread
def sleep_task(sleep_time):
    print(f"sleep {sleep_time} seconds start!!!")
    time.sleep(sleep_time)
    print(f"sleep {sleep_time} seconds end!!!\n")

t1=Thread(target=sleep_task,args=(2,))#target传函数方法，args传参数，这里边是元组的方式，所以参数后边一定要加括号
t1.start()
t2=Thread(target=sleep_task,args=(3,))
t2.start()
# t1.join()
# t2.join() #相当于吧线程阻塞住

time.sleep(1) #希望线程在运行一秒钟后就退出



sleep_task(1) #并发的t1,t2会和其后边的线程一起开始运行。如果想让并发的线程先运行的话，可以用join()方法