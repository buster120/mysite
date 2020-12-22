#实例化Thread
#继承Thread类
import time
from threading import Thread

def sleep_task(sleep_time):
    print(f"sleep {sleep_time} seconds start!")
    time.sleep(sleep_time)
    print(f"sleep {sleep_time} seconds end!")

class Time_threading(Thread):
    def __init__(self,sleep_time):
        self.sleep_time=sleep_time
        super().__init__()

    def run(self):
        print(f"sleep {self.sleep_time} seconds start!")
        time.sleep(self.sleep_time)
        print(f"sleep {self.sleep_time} seconds end!")









if __name__=="__main__":
    t1=Thread(target=sleep_task,args=(2,))
    # t1.setDaemon(True)
    t1.start()
    t2 =Thread(target=sleep_task,args=(3,))
    # t2.setDaemon(True)
    t2.start()
    # t1.join()
    # t2.join()
#
#     print("时间到啦，要结束啦！！！")
# if __name__=="__main__":
#     t1=Time_threading(2)
#     t2=Time_threading(3)
#     t1.start()
#     t2.start()