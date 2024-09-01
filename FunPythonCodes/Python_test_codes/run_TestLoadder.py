import os
import unittest


if __name__ == '__main__':

    suite = unittest.defaultTestLoader.discover("D:\Source codes\Python_20240809\FunPythonCodes\Test_Cases",
                                                pattern='test_*.py')
    unittest.main(defaultTest='suite', verbosity=2)

