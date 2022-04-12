# Blade max stiffness from Solidworks 2236636
# Blade min stiffness from Solidworks 170998

import CNP
import Conversions as conv

# Imports data from Json
jsonValues = conv.processing()

torsionBarValues = jsonValues[0]
BladeValues = jsonValues[1]
units = jsonValues[2]

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

# Formats outputs to make calculations easier to read
KTorsional = str(KTorsional)
KCantileverMax = str(KCantileverMax)
KCantileverMin = str(KCantileverMin)
KCombinedMax = str(KCombinedMax)
KCombinedMin = str(KCombinedMin)

def console_output():

    print("-" * (len(KTorsional) + len(KCantileverMax)))

    print("Stiffness Values".center(len(KTorsional) + len(KCantileverMax)))

    print("-" * (len(KTorsional) + len(KCantileverMax)))

    print("Torsional Stiffness: \n")

    print(KTorsional + str(" N-m/rad" if units == "metric" else " lb-in/rad"))

    print("-" * (len(KTorsional) + len(KCantileverMax)))

    print("Blade Cantilever Stiffness: \n")

    print("Max: " + KCantileverMax +  str(" N/m" if units == "metric" else " lb/in"))

    print("Min: " + KCantileverMin + str(" N/m" if units == "metric" else " lb/in"))

    print("-" * (len(KTorsional) + len(KCantileverMax)))

    print("Combined Stiffness: \n")

    print("Max: " + KCombinedMax + str(" N/m" if units == "metric" else " lb/in"))

    print("Min: " + KCombinedMin + str(" N/m" if units == "metric" else " lb/in"))

    print()

    print("Difference: " + format(float(KCombinedMax)-float(KCombinedMin), ".4f") + str(" N/m" if units == "metric" else " lb/in"))

    print("-" * (len(KTorsional) + len(KCantileverMax)))

    print()

console_output()