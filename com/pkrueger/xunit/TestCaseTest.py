from com.pkrueger.xunit.TestCase import TestCase
from com.pkrueger.xunit.WasRun import WasRun

__author__ = 'pkrueger'


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert test.wasRun
TestCaseTest("testRunning").run()