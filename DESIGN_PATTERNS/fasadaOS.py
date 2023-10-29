from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State','new running sleeping restart zombie')

class User:
    pass

class Process:
    pass

class File:
    pass

class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
    
    def __str__(self):
        return self.name
    
    @abstractmethod
    def boot(self):
        pass
    
    @abstractmethod
    def kill(self,restart=True):
        pass
    
    
