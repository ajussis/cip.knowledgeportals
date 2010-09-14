from plone.theme.interfaces import IDefaultPloneLayer
from plone.portlets.interfaces import IPortletManager
from zope.interface import Interface
from plone.app.portlets.interfaces import IColumn

class ICollectiveCarouselLayer(Interface):
    """ A layer specific to collective.carousel
    """

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "Custom Theme" theme, this interface must be its layer
       (in sptheme4/viewlets/configure.zcml).
    """

class IThemeSweetpotato(IPortletManager):
 """A description goes here    """


