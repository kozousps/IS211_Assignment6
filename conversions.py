def convertCelsiusToKelvin(celsius):
    """
    Takes in a float representing a Celsius measurement,
    and returns that temperature converted into Kelvins"
    """
    if celsius < -273.15:
        raise OutOfRangeError('Celsius must be more than -273.15')
    else:
        kelvin = celsius + 273.15
        return kelvin


def convertCelsiusToFahrenheit(celsius):
    """
    Takes in a float representing a Celsius measurement,
    and returns that temperature converted into Fahrenheit
    """
    if celsius < -273.15:
        raise OutOfRangeError('Celsius must be more than -273.15')
    else:
        fahrenheit = celsius * 1.8 + 32
        return fahrenheit


def convertFahrenheitToKelvin(fahrenheit):
    """
    Takes in a float representing a Fahrenheit measurement,
    and returns that temperature converted into Kelvins
    """
    if fahrenheit < -459.67:
        raise OutOfRangeError('Fahrenheit must be more than -459.67')
    else:
        kelvin = (fahrenheit + 459.67) / 1.8
        return kelvin


def convertFahrenheitToCelsius(fahrenheit):
    """
    Takes in a float representing a Fahrenheit measurement,
    and returns that temperature converted into Celsius
    """
    if fahrenheit < -459.67:
        raise OutOfRangeError('Fahrenheit must be more than -459.67')
    else:
        celsius = (fahrenheit - 32) / 1.8
        return celsius


def convertKelvinToCelsius(kelvin):
    """
    Takes in a float representing a Kelvin measurement,
    and returns that temperature converted into Celsius
    """
    if kelvin < 0:
        raise OutOfRangeError('Kelvin must be more than 0')
    else:
        celsius = kelvin - 273.15
        return celsius


def convertKelvinToFahrenheit(kelvin):
    """
    Takes in a float representing a Kelvin measurement,
    and returns that temperature converted into Fahrenheit
    """
    if kelvin < 0:
        raise OutOfRangeError('Kelvin must be more than 0')
    else:
        fahrenheit = kelvin * 1.8 - 459.67
        return fahrenheit


class OutOfRangeError(ValueError):
    pass
