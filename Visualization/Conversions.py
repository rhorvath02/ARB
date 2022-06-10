import json

# Takes input from the Json file and processes it, returning [[Torsion Bar Values], [Blade Values], [Output Units]] in the order each
# set of values appears in the Json file

def processing():

    f = open("Properties.json", "r")

    processing = json.load(f)

    f.close()

    TB_in = processing["TorsionBar"]

    blade_in = processing["Blade"]

    units = processing["Units"]

    TB_val = [x for x in TB_in.values()]
    
    blade_val = [x for x in blade_in.values()]
    
    inputUnits, outputUnits = units.get("InputUnits"), units.get("OutputUnits")
    
    if inputUnits != outputUnits:
        if inputUnits == "metric":

            # Converts list of torsion bar values from metric to imperial

            TB_conv_geo = [x * 39.3701 for x in TB_val[:-2]]

            print(TB_conv_geo)

            TB_conv_const = [x * 1.450377377 * 10**-4 for x in TB_val[-2:]]

            # Converts list of blade values from metric to imperial

            blade_conv_geo = [x * 39.3701 for x in blade_val[:-2]]

            blade_conv_const = [x * 1.450377377 * 10**-4 for x in blade_val[-2:]]

        else:

            # Converts list of torsion bar values from imperial to metric

            TB_conv_geo = [x * 0.0254 for x in TB_val[:-2]]

            TB_conv_const = [x * 6894.76 for x in TB_val[-2:]]

            # Converts list of blade values from imperial to metric

            blade_conv_geo = [x * 0.0254 for x in blade_val[:-2]]

            blade_conv_const = [x * 6894.76 for x in blade_val[-2:]]

        TB_val = TB_conv_geo + TB_conv_const

        blade_val = blade_conv_geo + blade_conv_const

    return TB_val, blade_val, units.get("OutputUnits")