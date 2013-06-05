import unittest
import sys

sys.path.append("../src/util")
sys.path.append("../src")

from testContextSummary import TestContextSummary as T1
from util.testGroupUtils import TestGroupUtils as T2

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(T1)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main()
    
    suite = unittest.TestLoader().loadTestsFromTestCase(T2)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main()
    
    