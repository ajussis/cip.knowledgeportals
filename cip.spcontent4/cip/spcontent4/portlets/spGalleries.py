from plone.memoize.instance import memoize
from plone.memoize import ram
from plone.memoize.compress import xhtml_compress
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.layout.navigation.root import getNavigationRootObject
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements
from zope import schema

from Acquisition import aq_inner
from DateTime.DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.portlets import PloneMessageFactory as _
from plone.app.portlets.cache import render_cachekey
from plone.app.portlets.portlets import base

# Import the base portlet module whose properties we will modify
from plone.portlet.static import static

class IspGalleriesPortlet(IPortletDataProvider):
    """ Defines a new portlet "grey static" which takes properties of the existing static text portlet. """

class spGalleriesRenderer(base.Renderer):
    """ Overrides static.pt in the rendering of the portlet. """
    render = ViewPageTemplateFile('spGalleries.pt')

#    _template = ViewPageTemplateFile('spGalleries.pt')


    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        self.navigation_root_url = portal_state.navigation_root_url()
        self.portal = portal_state.portal()
        self.navigation_root_path = portal_state.navigation_root_path()
        self.navigation_root_object = getNavigationRootObject(self.context, self.portal)

#    @ram.cache(render_cachekey)
#    def render(self):
#        return xhtml_compress(self._template())

    @property
    def available(self):
        return len(self._data())

    def publishedEvents(self):
        return self._data()

    @memoize
    def haveEventsFolder(self):
        return 'events' in self.navigation_root_object.objectIds()

    def allEventsLink(self):
        navigation_root_url = self.navigation_root_url
        if self.have_events_folder():
            return '%s/events' % navigation_root_url
        else:
            return '%s/events_listing' % navigation_root_url

"""    def prev_events_link(self):
        # take care dont use self.portal here since support
        # of INavigationRoot features likely will breake #9246 #9668
        if (self.have_events_folder() and
            'aggregator' in self.navigation_root_object['events'].objectIds() and
            'previous' in self.navigation_root_object['events']['aggregator'].objectIds()):
            return '%s/events/aggregator/previous' % self.navigation_root_url
        elif (self.have_events_folder() and
            'previous' in self.navigation_root_object['events'].objectIds()):
            return '%s/events/previous' % self.navigation_root_url
        return None

    @memoize
    def _data(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        limit = self.data.count
        state = self.data.state
        path = self.navigation_root_path
        return catalog(portal_type='Event',
                       review_state=state,
                       end={'query': DateTime(),
                            'range': 'min'},
                       path=path,
                       sort_on='start',
                       sort_limit=limit)[:limit]
"""
    def getGalleryFolder(self):
        results = catalog.searchResults({'portal_type': 'Event', 'review_state': 'pending'})
        return results


class spGalleriesAssignment(base.Assignment):
    """ Assigner for grey static portlet. """
    implements(IspGalleriesPortlet)

    def __init__(self, count=5, state=('published', )):
        self.count = count
        self.state = state

    @property
    def title(self):
        return _(u"Events")
    
class spGalleriesAddForm(base.AddForm):
    """ Make sure that add form creates instances of our custom portlet instead of the base class portlet. """
#    form_fields = form.Fields(IspGalleries)
    label = _(u"Add Events Portlet")
    description = _(u"This portlet lists upcoming Events.")

    def create(self, data):
        return spGalleriesAssignment(count=data.get('count', 5), state=data.get('state', ('published',)))

#    def create(self, data):
#        return spGalleriesAssignment(**data)




#class EditForm(base.EditForm):
#    form_fields = form.Fields(IEventsPortlet)
#    label = _(u"Edit Events Portlet")
#    description = _(u"This portlet lists upcoming Events.")
