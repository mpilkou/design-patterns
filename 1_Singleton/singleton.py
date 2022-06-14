from threading import Lock


def singleton_as_decorator_fun(function_to_do):
    lock = Lock()
    def execute_function(self, *args, **kwargs):
        with lock:
            if(self.__class__.instanse is None):
                self.__class__.instanse = self
            return function_to_do(self.__class__.instanse, *args, **kwargs)
    return execute_function

class Singleton:

    instanse = None
    lock = Lock()

    def get_instanse(self):
        with Singleton.lock:
            if (type(self) is Singleton):
                if (Singleton.instanse is None):
                    Singleton.instanse = self
                return Singleton.instanse
            else:
                if (self.__class__.instanse is None):
                    self.__class__.instanse = self
                return self.__class__.instanse


class ChildSingleton(Singleton):
    instanse = None

class SingletonClass(object):
    # lock = Lock()
    def __new__(cls, *args, **kwargs):
        # with SingletonClass.lock:
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls, *args, **kwargs)
        return cls.instance