map = {"miles": 1,
       "meters": 1609.34,
       "yards": 1760
       }


def convert(fromUnit, toUnit, value):
    if fromUnit == "miles" and toUnit == "yards":
        result = value * 1760
        return result

    elif fromUnit == "miles" and toUnit == "meters":
        result = value * 1609.344
        return result

    elif fromUnit == "yards" and toUnit == "miles":
        result = value / 1760
        return result

    elif fromUnit == "yards" and toUnit == "meters":
        result = value * 0.9144
        return result

    elif fromUnit == "meters" and toUnit == "miles":
        result = value / 1609.344
        return result

    elif fromUnit == "meters" and toUnit == "yards":
        result = value / 0.9144
        return result

    elif fromUnit == toUnit:
        return value

    else:
        raise ConversionNotPossible("Units not convertable")


class ConversionNotPossible(ValueError):
    pass
