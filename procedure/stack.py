import numpy as np

class NumpyStack(object):
    def __init__(self, length):
        """
        init stack with length that you need
        """
        self.stack = []
        self.length = length
    
    def pop(self):
        """
        get the last element in stack
        """
        temp = -1
        temp = self.stack[-1]
        return temp
    
    def put(self, value):
        """
        delete the first element and insert new element at final position
        """
        if len(self.stack) == 10:
            # delete element in memory
            del self.stack[0]
        #     self.len = len(self.stack) - 1
        
        self.stack = self.stack + [value]
        return self.stack
        
    @property
    def len(self):
        """
        Length of stack
        """
        return len(self.stack)