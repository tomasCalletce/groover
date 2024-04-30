import numpy as np

class Groover:
    def __init__(self, numberOfElementsInputDomain):
        import numpy as np

        self.numberOfElementsInputDomain = numberOfElementsInputDomain
        self.numberOfSates = 2**numberOfElementsInputDomain
        self.register = self.state0()

    def run(self):
        self.register = self.makeKetH()
        print(self.register)


    def state0(self):
        allzeros = np.zeros(self.numberOfSates)
        allzeros[0] = 1
        return allzeros
    
    def makeKetH(self):
        return np.dot(self.hadamardN(), self.register)


    def hadamardN(self):
        hadamardForNSates = self.hadamard()

        for i in range(self.numberOfElementsInputDomain - 1):
            hadamardForNSates = np.kron(hadamardForNSates, self.hadamard())

        return hadamardForNSates
    
    def hadamard(self):
        matrix = np.ones((2, 2))
        matrix[1][1] = -1

        return 1/np.sqrt(2) * matrix


groover_instance = Groover(numberOfElementsInputDomain=2)
groover_instance.run()