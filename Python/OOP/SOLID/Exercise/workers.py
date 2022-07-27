"""
[DIP]
You are provided with a code on which you have to apply the DIP (Dependency Inversion Principle) so that when
adding new worker classes, the Manager class will work properly.
"""

class Worker:

    def work(self):
        print("I'm working!!")


class SuperWorker(Worker):

    def work(self):
        print("I work very hard!!!")

class LazyWorker(Worker):

    def work(self):
        print("I dont work")

class Manager:

    def __init__(self):
        pass

    def set_worker(self, worker: Worker):
        #assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()



worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
lazy_worker = LazyWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
    manager.set_worker(lazy_worker)
    manager.manage()

except AssertionError:
    print("manager fails to support super_worker....")
