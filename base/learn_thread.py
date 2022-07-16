# Python 多线程
from multiprocessing import Process
from threading import Thread


def task(name=''):
    for i in range(100):
        print(f"exec task: {i}, {name}")


class MyThread(Thread):

    def run(self) -> None:
        for n in range(1000):
            print(f'custom thread exec: {n}')


if __name__ == '__main__':
    t = Thread(target=task)
    t.start()

    t2 = MyThread()
    t2.start()

    # 多进程
    p = Process(target=task)
    p.start()

    # 给线程传参
    t3 = Thread(target=task, args=('yuxing',))
    t3.start()

    for j in range(100):
        print(f'exec main: {j}')
