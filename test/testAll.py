import unittest
import sys
import os

def capitalize(str):
    return str[:1].upper() + str[1:]

def getTestNames():
    # directory walker
    db = {}
    for dirname, dirnames, filenames in os.walk('.'): # (os.path.abspath('.')):
        newDirName = "" if os.path.basename(dirname) == '.' else os.path.basename(dirname) + "."
        #print newDirName
        for filename in filenames:
            if filename.startswith("__"): continue
            if filename.endswith("pyc"): continue
            if filename == "testAll.py": continue
            filenameWithoutExtension = os.path.splitext(filename)[0]
            capitalizedFileName = capitalize(filenameWithoutExtension)
            fromName = newDirName + filenameWithoutExtension
            
            db[capitalizedFileName] = fromName

    importString = ""
    testDbString = "testDb = {"
    for (key, value) in db.items():
        importString += "from %s import %s\n" % (value, key)
        testDbString += '"%s":%s,\n' % (key, key)

    testDbString = testDbString[:-2] + "}\n\n"
        
    result = "%s\n%s" % (importString, testDbString)
    #return importString
    return result

sys.path.append("../src/util")
sys.path.append("../src")

def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestContextSummary))
    test_suite.addTest(unittest.makeSuite(TestGroupUtils))
    return test_suite

if __name__ == "__main__":
    stringToEval = getTestNames()
    exec(stringToEval)
    for i in testDb.keys(): 
        print "Testing: " + i
        testName = testDb[i]
        suite = unittest.TestLoader().loadTestsFromTestCase(testName)
        unittest.TextTestRunner(verbosity=2).run(suite)

    #unittest.TextTestRunner(verbosity=2).run(suite())
    
    