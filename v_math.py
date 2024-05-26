import numpy as np

class VMath:
    
    def gethadamard(self):
        matrix = np.ones((2, 2))
        matrix[1][1] = -1
        return 1/np.sqrt(2) * matrix
    
    def getIdentity(self):
        return np.array([[1, 0], [0, 1]])
    
    def getNot(self):
        return np.array([[0, 1], [1, 0]])