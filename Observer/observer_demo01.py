# -*- coding: utf-8 -*-

"""
观察者模式
"""


class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(f'{type(self).__name__}:: Got {args} From {subject}')


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(f'{type(self).__name__}:: Got {args} From {subject}')


subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)
subject.notify_all('notification')