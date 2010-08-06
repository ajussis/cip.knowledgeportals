from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
ztc.installProduct('collective.googleanalytics')
@onsetup
def setup_sweetpotato_policy():
    """Set up the additional products required for the Optilux site
    policy.
    The @onsetup decorator causes the execution of this body to be
    deferred
    until the setup of the Plone site testing layer.
    """
    # Load the ZCML configuration for the optilux.policy package.
    fiveconfigure.debug_mode = True
    import cip.sppolicy
    zcml.load_config('configure.zcml', cip.sppolicy)
    fiveconfigure.debug_mode = False
    # We need to tell the testing framework that these products
    # should be available. This can't happen until after we have loaded
    # the ZCML.
    ztc.installPackage('cip.sppolicy')
# The order here is important: We first call the (deferred) function
# which installs the products we need for the Optilux package. Then,
# we let PloneTestCase set up this product on installation.
setup_sweetpotato_policy()
ptc.setupPloneSite(products=['cip.sppolicy'])
class SweetpotatoPolicyTestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package. If
    necessary,
    we can put common utility or setup code in here.
    """

