from sum import sum

import tempfile
import unittest

class SumTestCase(unittest.TestCase):

    tmpfilepath = "hiya.txt"

    def setUp(self):
        with open(self.tmpfilepath, "w") as f:
            f.write("15\n")
            f.write("2\n")

    def retrieveSum(self):
        with open(self.tmpfilepath, "r") as f:
             d = int(f.readlines()[-1])
             return d
        
    #mock
    def testSum(self):
        expected = 17
        print("Expected sum: ", expected)
        sum(self.tmpfilepath)
        actual = self.retrieveSum()
        print("Actual sum: ", actual)
        self.assertFalse(actual != expected, "Summed numbers incorrectly")

s = SumTestCase()
s.setUp()
s.testSum()