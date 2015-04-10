from com.pkrueger.xunit.TestCase import TestCase

__author__ = 'pkrueger'


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1