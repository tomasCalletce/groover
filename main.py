import numpy as np

class Groover:
    def __init__(self, numberOfElementsInputDomain, rangeOfFunction):
        import numpy as np

        self.numberOfElementsInputDomain = numberOfElementsInputDomain
        self.numberOfSates = 2**numberOfElementsInputDomain
        self.register = self.state0()

        if(rangeOfFunction.size != self.numberOfSates):
            raise ValueError("range size those not match the domain size")
        
        
        
        self.rangeOfFunction = rangeOfFunction

    def run(self):
        self.register = self.makeKetH()
        self.register = self.rotateOverB()
        print(self.register)


    # |b> represents the state with an equal superposition of all states that output 1 for the function f(x).
    def rotateOverB(self):
        return np.dot(self.rotationMatrix(), self.register)


    def rotationMatrix(self):
        identity = np.eye(self.numberOfSates)

        for i in range(self.numberOfSates - 1):
            identity[i][i] = (-1) ** self.rangeOfFunction[i]

        return identity


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


groover_instance = Groover(numberOfElementsInputDomain=2, rangeOfFunction=np.array([0, 1, 0, 0]))
groover_instance.run()