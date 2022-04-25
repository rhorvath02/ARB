import json

# Takes input from the Json file and processes it, returning [[Torsion Bar Values], [Blade Values], [Output Units]] in the order each
# set of values appears in the Json file

def processing():

    f = open("Properties.json", "r")

    processing = json.load(f)

    f.close()

    torsionBarData = processing["TorsionBar"]

    BladeData = processing["Blade"]

    units = processing["Units"]

    torsionValues = []
    for item in torsionBarData.values():
        torsionValues.append(item)
    
    BladeValues = []
    for item in BladeData.values():
        BladeValues.append(item)
    
    inputUnits = units.get("InputUnits")
    outputUnits = units.get("OutputUnits")
    
    if inputUnits != outputUnits:
        if inputUnits == "metric":

            # Converts list of torsion bar values from metric to imperial
            for i in range(len(torsionValues)):
                torsionValues[i] *= 39.3701
            for i in range(len(torsionValues) - 2, len(torsionValues)):
                torsionValues[i] *= 1.450377377 * 10**-4
            
            # Converts list of blade values from metric to imperial
            for i in range(len(BladeValues)):
                BladeValues[i] *= 39.3701
            for i in range(len(BladeValues) - 2, len(BladeValues)):
                BladeValues[i] *= 1.450377377 * 10**-4

            return torsionValues, BladeValues, units.get("OutputUnits")

        else:

            # Converts list of torsion bar values from imperial to metric
            for i in range(len(torsionValues)-2):
                torsionValues[i] *= 0.0254
            for i in range(len(torsionValues) - 2, len(torsionValues)):
                torsionValues[i] *= 6894.7572932

            # Converts list of blade values from imperial to metric
            for i in range(len(BladeValues)-2):
                BladeValues[i] *= 0.0254
            for i in range(len(BladeValues) - 2, len(BladeValues)):
                BladeValues[i] *= 6894.7572932

            return torsionValues, BladeValues, units.get("OutputUnits")
    
    else:
        return torsionValues, BladeValues, units.get("OutputUnits")
