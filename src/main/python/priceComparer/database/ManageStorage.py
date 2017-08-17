import abc


class ManageStorage(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def setup():
        return

    @abc.abstractmethod
    def closeConnection():
        return

    @abc.abstractmethod
    def writeProduct(product):
        return
