import math
import scipy.integrate as integrate

class TorsionBar():
    def __init__(self, length, outerDiameter, innerDiameter, shearModulus, elasticModulus, units):
        self.length = length
        self.outerDiameter = outerDiameter
        self.innerDiameter = innerDiameter
        self.shearModulus = shearModulus
        self.elasticModulus = elasticModulus
        self.units = units

    def stiffness(self):
        J = math.pi * (self.outerDiameter**4 - self.innerDiameter**4) / 32
    
        KTorsional = self.shearModulus * J / self.length

        print(KTorsional / self.length**2)

        return KTorsional


class Blade():
    def __init__(self, height, largeBase, smallBase, depth, shearModulus, elasticModulus, units):
        self.height = height
        self.largeBase = largeBase
        self.smallBase = smallBase
        self.depth = depth
        self.shearModulus = shearModulus
        self.elasticModulus = elasticModulus
        self.units = units
    
    def stiffnessVert(self):
        # This value of I was derived by taking the average value of bh(x)^3/12 over the length of the rod
        # I = 1 / 48 * self.depth * (self.largeBase + self.smallBase) * (self.largeBase**2 + self.smallBase**2)
        I = (integrate.quad(lambda x: self.depth * ((self.largeBase - self.smallBase) / self.height * x \
            + self.smallBase)**3 / 12, 0, self.height)[0]) * 1 / self.height
        
        KCantilever = 3 * self.elasticModulus * I / (self.height**3)
        
        return KCantilever
    
    def stiffnessHoriz(self):
        # This value of I was derived by (integrating) taking the average value of b(x)h^3/12 over the length of the rod
        # I = 1 / 24 * (self.largeBase + self.smallBase) * self.depth**3
        I = (integrate.quad(lambda x: self.depth**3 * ((self.largeBase - self.smallBase) / self.height * x \
            + self.smallBase) / 12, 0, self.height)[0]) * 1 / self.height

        KCantilever = 3 * self.elasticModulus * I / (self.height**3)

        return KCantilever

class TorsionBarAndBlade():
    def __init__(self, KTorsional, KCantilever, cantileverLength):
        self.KTorsional = KTorsional
        self.KCantilever = KCantilever
        self.cantileverLength = cantileverLength
    
    def combined_stiffness(self):

        K1 = self.KTorsional / (self.cantileverLength**2)
        K2 = self.KCantilever
        K3 = self.KCantilever
        
        KCombined = (K1 * K2 * K3) / (K1 * K2 + K2 * K3 + K1 * K3)
        
        # KCombined = (K1 * K2) / (K1 + K2) for one blade
        
        return KCombined