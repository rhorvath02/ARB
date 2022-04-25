import CNP
import Conversions as conv
import matplotlib.pyplot as plt

x = []
y = []

# Imports data from Json
jsonValues = conv.processing()

torsionBarValues = jsonValues[0]
BladeValues = jsonValues[1]
units = jsonValues[2]


def bladeStiffnessRange():
    for i in range(0, 91):
        BladeValues[4] = i

        Blade = CNP.Blade(*BladeValues)

        KCantilever = Blade.stiffness()

        x.append(i)
        y.append(KCantilever)


def combinedStiffnessRange():
    for i in range(0, 91):
        BladeValues[4] = i

        TorsionBar = CNP.TorsionBar(*torsionBarValues)

        Blade = CNP.Blade(*BladeValues)

        KTorsional = TorsionBar.stiffness()

        KCantilever = Blade.stiffness()

        bladeLength = BladeValues[0]

        TorsionBarAndBlade = CNP.TorsionBarAndBlade(KTorsional, KCantilever, bladeLength)

        KCombined = TorsionBarAndBlade.combined_stiffness()

        x.append(i)
        y.append(KCombined)
        


def bladeStiffnessVsAngle():
    plt.plot(x, y)

    plt.grid()

    plt.xlabel("Angle of Blade Rotation (degrees)")
    # naming the y axis
    plt.ylabel('Individual Blade Stiffness (Nm/rad)')
    
    # giving a title to my graph
    plt.title('Blade Stiffness vs Angle of Blade Rotation')
    
    # function to show the plot
    plt.show()

def combinedStiffnessVsAngle():
    plt.plot(x, y)

    plt.grid()

    plt.xlabel("Angle of Rotation for each Blade (degrees)")
    # naming the y axis
    plt.ylabel('Combined ARB Stiffness (Nm/rad)')
    
    # giving a title to my graph
    plt.title('Combined ARB Stiffness vs Angle of Blade Rotation')
    
    # function to show the plot
    plt.show()

command = input('"Blade" or "Combined": ').lower()

while command != "blade" and command != "combined":
    print("  Please enter a valid command")
    command = input("Blade or Combined: ").lower()


if command == "blade":
    bladeStiffnessRange()
    bladeStiffnessVsAngle()
elif command == "combined":
    combinedStiffnessRange()
    combinedStiffnessVsAngle()
