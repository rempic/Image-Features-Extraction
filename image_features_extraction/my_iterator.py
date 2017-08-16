from abc import ABCMeta, abstractmethod


class my_iterator(object):
    """
    abstract class for the object iterator to implement a collection
    """
    __metaclass__ = ABCMeta

    def __iterator_init__(self):
        self.current = -1
        self.__count = 0


    def item(self, i):
            pass

    def count_update(self, count):
        self.__count = count
        return count

    def count(self):
        return self.__count

    # used to define the iterator: next element
    def __iter__(self):
        return self


    # used to define the iterator: next element
    def __next__(self):
        self.current += 1
        if self.current >= self.__count:
            self.current = -1
            raise StopIteration
        return self.item(self.current)
