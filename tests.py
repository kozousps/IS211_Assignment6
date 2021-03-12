import unittest
import conversions
import conversions_refactored


class KnownValues(unittest.TestCase):
    known_values = ((0.00, 32.00, 273.15),
                    (50.00, 122.00, 323.15),
                    (100.00, 212.00, 373.15),
                    (140.00, 284.00, 413.15),
                    (300.00, 572.00, 573.15),
                    (500.00, 932.00, 773.15),
                    (-50.00, -58.00, 223.15),
                    (-100.00, -148.00, 173.15),
                    (-180.00, -292.00, 93.15),
                    (-273.15, -459.67, 0.00)
                    )

    def test_convertCelsiusToKelvin(self):
        """convertCelsiusToKelvin should give known results with known input"""
        for celsius, fahrenheit, kelvin in self.known_values:
            result = round(conversions.convertCelsiusToKelvin(celsius), 2)
            self.assertEqual(kelvin, result)

    def test_convertCelsiusToFahrenheit(self):
        """
        convertCelsiusToFahrenheit should give known results
        with known input
        """
        for celsius, fahrenheit, kelvin in self.known_values:
            result = round(conversions.convertCelsiusToFahrenheit(celsius), 2)
            self.assertEqual(fahrenheit, result)

    def test_convertFahrenheitToKelvin(self):
        """
        convertFahrenheitToKelvin should give known results
        with known input
        """
        for celsius, fahrenheit, kelvin in self.known_values:
            result = round(conversions
                           .convertFahrenheitToKelvin(fahrenheit), 2)
            self.assertEqual(kelvin, result)

    def test_convertFahrenheitToCelsius(self):
        """
        convertFahrenheitToCelsius should give known results
        with known input
        """
        for celsius, fahrenheit, kelvin in self.known_values:
            result = round(conversions
                           .convertFahrenheitToCelsius(fahrenheit), 2)
            self.assertEqual(celsius, result)

    def test_convertKelvinToCelsius(self):
        """
        convertFahrenheitToCelsius should give known results
        with known input
        """
        for celsius, fahrenheit, kelvin in self.known_values:
            result = round(conversions
                           .convertKelvinToCelsius(kelvin), 2)
            self.assertEqual(celsius, result)

    def test_convertKelvinToFahrenheit(self):
        """
        convertCelsiusToFahrenheit should give known results
        with known input
        """
        for celsius, fahrenheit, kelvin in self.known_values:
            result = round(conversions.convertKelvinToFahrenheit(kelvin), 2)
            self.assertEqual(fahrenheit, result)


class TempBadInput(unittest.TestCase):
    def test_cel_too_small(self):
        """Celsius input fails below -273.15"""
        self.assertRaises(conversions.OutOfRangeError,
                          conversions.convertCelsiusToFahrenheit,
                          -273.16
                          )

    def test_far_too_small(self):
        """Fahrenheit input fails below -459.67"""
        self.assertRaises(conversions.OutOfRangeError,
                          conversions.convertFahrenheitToCelsius,
                          -459.68
                          )

    def test_kel_too_small(self):
        """Kelvin input fails below 0"""
        self.assertRaises(conversions.OutOfRangeError,
                          conversions.convertKelvinToCelsius,
                          -0.01
                          )


class KnownDistances(unittest.TestCase):
    def test_convertMilesToYards(self):
        """convertMilesToYards should give known results with known input"""
        expected = 1760
        result = conversions_refactored.convert("miles", "yards", 1)
        self.assertAlmostEqual(expected, result, places=2)

    def test_convertMilesToMeters(self):
        """convertMilesToMeters should give known results with known input"""
        expected = 8046.72
        result = conversions_refactored.convert("miles", "meters", 5)
        self.assertAlmostEqual(expected, result, places=2)

    def test_convertYardsToMiles(self):
        """convertYardsToMiles should give known results with known input"""
        expected = 0.57
        result = conversions_refactored.convert("yards", "miles", 1000)
        self.assertAlmostEqual(expected, result, places=2)

    def test_convertYardsToMeters(self):
        """convertYardsToMeters should give known results with known input"""
        expected = 1828.8
        result = conversions_refactored.convert("yards", "meters", 2000)
        self.assertAlmostEqual(expected, result, places=2)

    def test_convertMetersToMiles(self):
        """convertMetersToMiles should give known results with known input"""
        expected = 0.62
        result = conversions_refactored.convert("meters", "miles", 1000)
        self.assertAlmostEqual(expected, result, places=2)

    def test_convertMetersToYards(self):
        """convertMetersToYards should give known results with known input"""
        expected = 2187.23
        result = conversions_refactored.convert("meters", "yards", 2000)
        self.assertAlmostEqual(expected, result, places=2)

    def test_convertSameUnit(self):
        """convertSameUnit should return result same with input"""
        expected = 2000
        result = conversions_refactored.convert("meters", "meters", 2000)
        self.assertAlmostEqual(expected, result, places=2)


class DistBadInput(unittest.TestCase):
    def test_nonconvertable(self):
        """Input not convertable"""
        self.assertRaises(conversions_refactored.ConversionNotPossible)


if __name__ == '__main__':
    unittest.main()
