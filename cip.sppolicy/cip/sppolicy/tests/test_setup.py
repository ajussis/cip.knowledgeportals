import unittest
from cip.sppolicy.tests.base import SweetpotatoPolicyTestCase
class TestSetup(SweetpotatoPolicyTestCase):
    def test_portal_title(self):
        self.assertEquals("Sweetpotato Knowledge Portal", self.portal.getProperty('title'))
    def test_portal_description(self):
        self.assertEquals("Welcome to Sweetpotato Knowledge Portal", self. portal.getProperty('description'))
    def test_collectivegoogleanalytics_installed(self):
        self.failUnless('collective.googleanalytics' in self.types.objectIds())

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite