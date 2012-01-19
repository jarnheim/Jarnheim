UNITS_OF_MEASURE_WEIGHT = (("kg", "kilograms"),
                           ("lbs", "pounds"),
                           ("stone", "stone"),
                           ("edu", "edus"))
UNITS_OF_MEASURE_HEIGHT = (("cm", "cm"),
                           ("feet", "feet"))
GENDER = (("M", "male"),
          ("F", "female"))

class UtilityException(Exception):
    """Base exception class for this module"""
    def __str__(self):
        return self.__unicode__()

class BadUnitOfMeasureException(UtilityException):
    """Exception raised for an invalid unit of measure

    Attributes:
      uom: The unit of measure that was passed in
      valid_units: The units of measure that would have been valid
    """
    def __init__(self, uom, valid_units):
        print_units = [x[0] for x in valid_units]
        
        self.expr = uom
        self.msg = "A bad unit of measure was passed in. "
        self.msg += "'%s' was found. " % self.expr
        self.msg += "Valid units were: %s" % str(print_units)

    def __unicode__(self):
        return self.msg

def convert_height(cm, cm_to="cm"):
    """Convert height from cm to another unit of measure.
    Valid options are under UNITS_OF_MEASURE_HEIGHT.

    >>> convert_height(1)
    1.0
    >>> convert_height(1, "feet")
    0.032808399000000002
    """
    if "cm" == cm_to:
        # Calculation added in to catch type errors and force float
        return cm + 1 - 1.0
    elif "feet" == cm_to:
        return _cm_to_feet(cm)
    else:
        raise BadUnitOfMeasureException(cm_to, UNITS_OF_MEASURE_HEIGHT)

def convert_weight(kg, kg_to="kg"):
    """Convert weight from kg to another unit of measure.
    Valid options are under UNITS_OF_MEASURE_WEIGHT.

    >>> convert_weight(1)
    1.0
    >>> convert_weight(1, 'kg')
    1.0
    >>> convert_weight(1, 'lbs')
    2.2046226199999999
    """
    if "kg" == kg_to:
        #Calculation added in to catch type errors and force float
        return kg + 1 - 1.0
    elif "lbs" == kg_to:
        return _kg_to_lbs(kg)
    elif "stone" == kg_to:
        return _kg_to_stone(kg)
    elif "edu" == kg_to:
        return _kg_to_edu(kg)
    else:
        raise BadUnitOfMeasureException(kg_to,
                                        UNITS_OF_MEASURE_WEIGHT)

def _kg_to_lbs(kg):
    """Convert kg to lbs

    >>> _kg_to_lbs(1)
    2.2046226199999999
    """
    return kg * 2.20462262

def _kg_to_stone(kg):
    """Convert kg to stone

    >>> _kg_to_stone(1)
    0.15747304400000001
    """
    return kg * 0.157473044

def _kg_to_edu(kg):
    """Convert kg to edu

    >>> _kg_to_edu(1)
    0.011916879027027026
    """
    return _kg_to_lbs(kg) / 185

def _cm_to_feet(cm):
    """Convert cm to feet

    >>> _cm_to_feet(1)
    0.032808399000000002
    """
    return cm * 0.032808399


    
