import numpy as np
from v_math import VMath

class Groover:
    def __init__(self, numQbits, rangeOfFunction):
        self.numQbits = numQbits
        self.numberOfSates = 2**self.numQbits

        self.numQbitsTotal = numQbits + 1
        self.numberOfSatesTotal = 2**self.numQbitsTotal

        if(rangeOfFunction.size != self.numberOfSates):
            raise ValueError("range size those not match the domain size")
        
        self.rangeOfFunction = rangeOfFunction
        self.vMath = VMath()

    def getStartingState(self):
        startingState = self.state0()

        print(startingState)

        identity = self.vMath.getIdentity()
        notM = self.vMath.getNot()
        hadamard = self.vMath.gethadamard()
        gate1 = np.kron(identity, notM)
        gate2 = np.kron(identity, hadamard)
        return np.dot(gate2, np.dot(gate1, startingState))

    def run(self):

        startingState = self.getStartingState()
        print(startingState)
   
        # h = self.applyHadamard(h)

        # x = self.rotateOverB(h)

        # xMapped0 = self.applyHadamard(x)
        # xMapped0 = self.rotateOver0(xMapped0)
        # print(xMapped0)
        # h = self.applyHadamard(xMapped0)

        # print(h)
    
    def rotationMatrix0(self):
        identity = np.eye(self.numberOfSates)

        for i in range(self.numberOfSates):
            identity[i][i] = -1
        
        identity[0][0] = 1

        return identity
    
    def rotateOver0(self, state):
        return np.dot(self.rotationMatrix0(), state)
    

    # |b> represents the state with an equal superposition of all states that output 1 for the function f(x).
    def rotateOverB(self, state):
        return np.dot(self.rotationMatrixF(), state)

    def rotationMatrixF(self):
        identity = np.eye(self.numberOfSates)

        for i in range(self.numberOfSates):
            identity[i][i] = (-1) ** self.rangeOfFunction[i]

        return identity


    def state0(self):
        allzeros = np.zeros(self.numberOfSatesTotal)
        allzeros[0] = 1
        return allzeros
    
    def applyHadamard(self, state):
        return np.dot(self.hadamardN(), state)


    def hadamardN(self):
        hadamardForNSates = self.hadamard()

        for i in range(self.numberOfElementsInputDomain - 1):
            hadamardForNSates = np.kron(hadamardForNSates, self.hadamard())

        return hadamardForNSates
    
    def hadamard(self):
        matrix = np.ones((2, 2))
        matrix[1][1] = -1

        return 1/np.sqrt(2) * matrix


groover_instance = Groover(numQbits=1, rangeOfFunction=np.array([0, 1]))
groover_instance.run()