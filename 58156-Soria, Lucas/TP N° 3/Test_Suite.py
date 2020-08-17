import unittest
from test_Cajero_automatico1 import Cajero_automatico_Test1
from test_Cajero_automatico2 import Cajero_automatico_Test2
from test_Cajero_automatico3 import Cajero_automatico_Test3
from test_Cajero_automatico4 import Cajero_automatico_Test4


def suite():
    test_suite = unittest.TestSuite()
    # test1
    test_suite.addTest(unittest.makeSuite(Cajero_automatico_Test1))
    # Test2
    test_suite.addTest(unittest.makeSuite(Cajero_automatico_Test2))
    # Test3
    test_suite.addTest(unittest.makeSuite(Cajero_automatico_Test3))
    # Test3
    test_suite.addTest(unittest.makeSuite(Cajero_automatico_Test4))
    return test_suite


if __name__ == '__main__':
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)
