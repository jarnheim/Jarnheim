from django.test import TestCase
import Jarnheim.util as util

class TestConversions( TestCase ):
    def test_kg_to_lbs(self):
        """Test conversion from kg to lbs"""
        lbs = util._kg_to_lbs(1)
        self.assertEqual(lbs, 2.20462262, "Incorrect conversion result")

    def test_kg_to_lbs_error(self):
        """Bad number input in _kg_to_lbs"""
        self.assertRaises(TypeError, util._kg_to_lbs, 'a')

    def test_kg_to_stone(self):
        """Test conversion from kg to stone"""
        stone = util._kg_to_stone(1)
        self.assertEqual(stone, 0.157473044, "Incorrect conversion result")

    def test_kg_to_stone_error(self):
        """Bad input should raise an error"""
        self.assertRaises(TypeError, "baaa")

    def test_kg_to_edu(self):
        """Test conversion from kg to edu"""
        edu = util._kg_to_edu(1)
        self.assertEqual(edu, (2.20462262/185), "Incorrect conversion result")

    def test_kg_to_edu_error(self):
        """Bad input to _kg_to_edu should raise an exception"""
        self.assertRaises(TypeError, "ba")

    def test_convert_weight(self):
        """Test convert weight from kg to kg, lbs, stone, or edu"""
        units = (("kg", 1),
                 ("lbs", 2.20462262),
                 ("stone", 0.157473044),
                 ("edu", (2.20462262/185)))
        for unit in units:
            new_weight = util.convert_weight(1, unit[0])
            self.assertEqual(new_weight, unit[1],
                             "Incorrect conversion result from kg to " + unit[0])

    def test_convert_height(self):
        """Test height conversion from cm to cm or feet"""
        units = (('cm', 1),
                 ('feet', 0.032808399))
        for unit in units:
            new_height = util.convert_height(1, unit[0])
            self.assertEqual(new_height, unit[1],
                             "Incorrect conversion result from cm to " + unit[0])

    def test_convert_height_bad_input(self):
        """Test that passing in bad input to util.convert_height raises an appropriate exception."""
        self.assertRaisesRegexp(util.BadUnitOfMeasureException,
                                r"A bad unit of measure was passed in.\w*",
                                util.convert_height,
                                1, "bad")
        self.assertRaises(TypeError, util.convert_height, "a")

    def test_convert_weight_bad_input(self):
        """Test that passing in bad input to util.convert_weight raises an appropriate exception."""
        self.assertRaisesRegexp(util.BadUnitOfMeasureException,
                                r"A bad unit of measure was passed in.\w*",
                                util.convert_weight,
                                1, "bad")
        self.assertRaises(TypeError,
                          util.convert_weight,
                          'a')

    def test_cm_to_feet(self):
        """Test convert cm to feet"""
        feet = util._cm_to_feet(1)
        self.assertEqual(feet, 0.032808399, "Incorrect conversion result")
