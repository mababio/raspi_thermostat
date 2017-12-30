import abc


class AControllable(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def on(self, script):
        pass

    @abc.abstractmethod
    def off(self, script):
        pass


