import numpy as np
from v_math import VMath
import math

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

        identity = np.eye(self.numberOfSates)
        notM = self.vMath.getNot()
        hadamard = self.vMath.gethadamard()
        gate1 = np.kron(identity, notM)
        gate2 = np.kron(identity, hadamard)
        return np.dot(gate2, np.dot(gate1, startingState))

    def run(self):
        startingState = self.getStartingState()
   
        state = self.applyHadamard(startingState)

        for i in range(int(math.sqrt(self.numberOfSates))):
            afterRotB = self.rotateOverB(state)
            had = self.applyHadamard(afterRotB)
            xMapped0 = self.rotateOver0(had)
            state = self.applyHadamard(xMapped0)
    
    def rotationMatrix0(self):
        rot = np.eye(self.numberOfSates)

        for i in range(self.numberOfSates):
            rot[i][i] = -1
        
        rot[0][0] = 1

        return np.kron(rot, self.vMath.getIdentity())
    
    def rotateOver0(self, state):
        return np.dot(self.rotationMatrix0(), state)
    
    def rotateOverB(self, state):
        return np.dot(self.rotationMatrixF(), state)

    def rotationMatrixF(self):
        rot = np.eye(self.numberOfSates)

        for i in range(self.numberOfSates):
            rot[i][i] = (-1) ** self.rangeOfFunction[i]

        return np.kron(rot, self.vMath.getIdentity())


    def state0(self):
        allzeros = np.zeros(self.numberOfSatesTotal)
        allzeros[0] = 1
        return allzeros
    
    def applyHadamard(self, state):
        return np.dot(self.hadamardN(), state)


    def hadamardN(self):
        hadamardForNSates = self.hadamard()

        for i in range(self.numQbits - 1):
            hadamardForNSates = np.kron(hadamardForNSates, self.hadamard())

        return np.kron(hadamardForNSates, self.vMath.getIdentity())
    
    def hadamard(self):
        matrix = np.ones((2, 2))
        matrix[1][1] = -1

        return 1/np.sqrt(2) * matrix


groover_instance = Groover(numQbits=2, rangeOfFunction=np.array([0, 1,0,0]))
groover_instance.run()