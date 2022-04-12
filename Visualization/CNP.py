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

        return KTorsional


class Blade():
    def __init__(self, height, largeBase, smallBase, depth, angle, shearModulus, elasticModulus, units):
        self.height = height
        self.largeBase = largeBase
        self.smallBase = smallBase
        self.depth = depth
        self.shearModulus = shearModulus
        self.elasticModulus = elasticModulus
        self.units = units
        self.angle = angle
    
    def stiffness(self):
        # This value of I was derived by taking the average value of bh(x)^3/12 over the length of the rod
        I = (integrate.quad(lambda x: (self.depth * (self.largeBase - (self.largeBase - self.smallBase) / self.height * x) / 12) \
                    * (self.depth**2 * (math.cos(self.angle * math.pi / 180)**2) + (self.largeBase - (self.largeBase - self.smallBase) \
                        / self.height * x)**2 * (math.sin(self.angle * math.pi / 180)**2)), 0, self.height - 0.5 * 0.0254)[0]  + integrate.quad(lambda x: math.pi \
                            * (0.00254)**4 / 64, 0, 0.5)[0]) * 1 / self.height

        KCantilever = 3 * self.elasticModulus * I / (self.height**3)

        return KCantilever

class TorsionBarAndBlade():
    def __init__(self, KTorsional, KCantilever, cantileverLength):
        self.KTorsional = KTorsional
        self.KCantilever1 = KCantilever
        self.cantileverLength = cantileverLength
    
    def combined_stiffness(self):

        K1 = self.KTorsional # / (self.cantileverLength**2)
        K2 = self.KCantilever1 * self.cantileverLength**2
        K3 = self.KCantilever1 * self.cantileverLength**2

        KCombined = (K1 * K2 * K3) / (K1 * K2 + K2 * K3 + K1 * K3)
        
        # KCombined = (K1 * K2) / (K1 + K2) for one blade

        return KCombined