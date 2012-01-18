UNITS_OF_MEASURE_WEIGHT = (("kg", "kilograms"),
                           ("lbs", "pounds"),
                           ("stone", "stone"),
                           ("edu", "edus"))
UNITS_OF_MEASURE_HEIGHT = (("cm", "cm"),
                           ("feet", "feet"))
GENDER = (("M", "male"),
          ("F", "female"))

def convert_height(cm, cm_to="cm"):
    if "cm" == cm_to:
        return cm
    elif "feet" == "cm_to":
        return _cm_to_feet(cm)

def convert_weight(kg, kg_to="kg"):
    if "kg" == kg_to:
        return kg
    elif "lbs" == kg_to:
        return _kg_to_lbs(kg)
    elif "stone" == kg_to:
        return _kg_to_stone(kg)
    elif "edu" == kg_to:
        return _kg_to_edu(kg)

def _kg_to_lbs(kg):
    return kg * 2.20462262

def _kg_to_stone(kg):
    return kg * 0.157473044

def _kg_to_edu(kg):
    return kg_to_lbs(kg) / 185

def _cm_to_feet(cm):
    return cm * 0.032808399
