from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
from kss.core.tests.base import KSSLayer, KSSViewTestCase 


@onsetup
def setup_product():
    """Set up additional products and ZCML required to test this product.

    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """

    # Load the ZCML configuration for this package and its dependencies

    fiveconfigure.debug_mode = True
    import collective.portlet.explore
    zcml.load_config('configure.zcml', collective.portlet.explore)
    fiveconfigure.debug_mode = False

    # We need to tell the testing framework that these products
    # should be available. This can't happen until after we have loaded
    # the ZCML.

    ztc.installPackage('collective.portlet.explore')

# The order here is important: We first call the deferred function and then
# let PloneTestCase install it during Plone site setup

setup_product()
ptc.setupPloneSite(products=['collective.portlet.explore'])

class TestCase(ptc.PloneTestCase):
    """Base class used for test cases
    """

    def afterSetUp(self):
        self.setRoles(('Manager',))


class KSSTestCase(TestCase, KSSViewTestCase):
    class layer(KSSLayer, TestCase.layer):
        pass