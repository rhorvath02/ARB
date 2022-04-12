import CNP
import Conversions as conv

# The for loops here are actively modified to optimize different components of the ARB. The current loops are not the only ones
# that were used

maxDiff = 0
maxNums = []

# Imports data from Json
jsonValues = conv.processing()

torsionBarValues = jsonValues[0]
BladeValues = jsonValues[1]
units = jsonValues[2]

for i in range(25, 40):
    print(i)
    x = i / 10 * 0.0254
    if x > torsionBarValues[0] / 4:
        continue
    BladeValues[0] = x
    for j in range(50, 200):
        y = j / 100 * 0.0254
        BladeValues[1] = y
        for k in range(50, 200):
            z = k / 100 * 0.0254
            BladeValues[2] = z

            # Definition of torsion bar, blades, and their individual stiffnesses
            TorsionBar = CNP.TorsionBar(*torsionBarValues, units)

            Blade = CNP.Blade(*BladeValues, units)

            KTorsional = TorsionBar.stiffness()

            KCantileverMax = Blade.stiffnessVert()

            KCantileverMin = Blade.stiffnessHoriz()

            # Definition of combined torsion bar and blade and its stiffness
            bladeLength = BladeValues[0]
            TorsionBarAndBlade = CNP.TorsionBarAndBlade(KTorsional, KCantileverMax, bladeLength)

            KCombinedMax = TorsionBarAndBlade.combined_stiffness()

            bladeLength = BladeValues[0]
            TorsionBarAndBlade = CNP.TorsionBarAndBlade(KTorsional, KCantileverMin, bladeLength)

            KCombinedMin = TorsionBarAndBlade.combined_stiffness()

            if KCombinedMax - KCombinedMin > maxDiff and BladeValues[1] > BladeValues[2] and torsionBarValues[0] / 4 > BladeValues[0]:
                if KCombinedMax < 20000 and KCombinedMin > 15000:
                    maxDiff = KCombinedMax - KCombinedMin
                    maxNums = BladeValues[::]
                
print(maxDiff)
print(maxNums)