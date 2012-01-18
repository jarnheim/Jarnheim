"""Set up the testing stuff for this project."""

import unittest
import doctest
import util

def suite():
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(util))
    return suite
