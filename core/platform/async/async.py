"""Decorator for performing asynchronous method calls."""
from functools import wraps
from multiprocessing.dummy import Pool, Lock
import time

class Async(object):
    def __init__(self, workers=1):
        self.workers = workers
        self.pool = Pool(processes=workers)
        self.results = []

    def get_pool(self):
        return self.pool

    def get_lock(self):
        return Lock()

    def get_worker_count(self):
        return self.workers

    def acquire_lock(self, obj, lock):
        try:
            l = getattr(obj, lock)
            l.acquire()
        except ValueError as e:
            # This only occurs when Pool has been closed and if it is
            # then application has also been closed.
            pass
        return

    def release_lock(self, obj, lock):
        try:
            l = getattr(obj, lock)
            l.release()
        except ValueError as e:
            # This only occurs when Pool has been closed and if it is
            # then application has also been closed.
            pass
        return

    def async_call(self, callback):
        async = self
        def _async_decorator(func):
            def _decorator(self, *args):
                def _callback(result):
                    async.results.pop(0)
                    callback(self, result)
                res = async.pool.apply_async(
                    func, [self, *args], callback=_callback)
                async.results.append(res)
                return res
            return wraps(func)(_decorator)
        return _async_decorator

    def synchronize(self, lock):
        async = self
        def _async_synchronize(func):
            def _decorator(self, *args):
                async.acquire_lock(self, lock)
                ret = func(self, *args)
                async.release_lock(self, lock)
                return ret
            return wraps(func)(_decorator)
        return _async_synchronize

    def close(self):
        # Wait for all results to complete.
        for res in self.results:
            res.get()
        self.pool.close()
        self.pool.join()
