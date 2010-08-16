from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.portlet.static import PloneMessageFactory as _

# Import the base portlet module whose properties we will modify
from plone.portlet.static import static

class IspGalleriesPortlet(static.IStaticPortlet):
    """ Defines a new portlet "grey static" which takes properties of the existing static text portlet. """
    pass

class spGalleriesRenderer(static.Renderer):
    """ Overrides static.pt in the rendering of the portlet. """
    render = ViewPageTemplateFile('spGalleries.pt')

class spGalleriesAssignment(static.Assignment):
    """ Assigner for grey static portlet. """
    implements(IspGalleriesPortlet)

class spGalleriesAddForm(static.AddForm):
    """ Make sure that add form creates instances of our custom portlet instead of the base class portlet. """
    def create(self, data):
        return spGalleriesAssignment(**data)