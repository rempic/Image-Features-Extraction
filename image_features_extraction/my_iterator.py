from abc import ABCMeta, abstractmethod


class my_iterator(object):
    """
    abstract class used to implement a collection class
    """
    __metaclass__ = ABCMeta

    def __iterator_init__(self):
        self.current = -1
        self.__count = 0


    def item(self, i):
        """
        item has to be inplemented in the main class
        """
        pass

    def count_update(self, count):
        self.__count = count
        return count

    def count(self):
        """
        returns the number of items 
        """
        return self.__count


    def __iter__(self):
        """
        Python method to define and call the iterator
        """
        return self


    # used to define the iterator: next element
    def __next__(self):
        """
        Python method to calls the iterator next element
        """
        self.current += 1
        if self.current >= self.__count:
            self.current = -1
            raise StopIteration
        return self.item(self.current)
