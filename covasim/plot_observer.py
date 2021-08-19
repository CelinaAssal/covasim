from abc import ABCMeta, abstractclassmethod

class IObservable(metaclass=ABCMeta):

    @staticmethod
    @abstractclassmethod
    def subscribe(self, observer: Observer):
        pass

    @staticmethod
    @abstractclassmethod
    def detach(self, observer: Observer):
        pass

    @staticmethod
    @abstractclassmethod
    def notify(self, observer: Observer):
        pass

class Subject(IObservable):
    def __init__(self):
        # set() ensures unique values
        self._observers = set()

        def subscribe(self, observer):
            self._observers.add(observer)

        def unsubscribe(self, observer):
            self._observers.remove(observer)

        def notify(self, *args, **kwargs):
            for observer in self._observers:
                observer.notify(self, *args, **kwargs)

class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractclassmethod
    def notify(observable, *args, **kwargs):
        pass

class Observer(IObserver):
    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        # give a notification
        print("Observer received", args, kwargs)
