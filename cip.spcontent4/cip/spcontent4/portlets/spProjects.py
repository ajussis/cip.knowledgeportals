import random

from zope.interface import implements
from zope.component import getMultiAdapter

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope import schema
from zope.formlib import form

from plone.memoize.instance import memoize
from plone.memoize import ram
from plone.memoize.compress import xhtml_compress

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget

from Products.ATContentTypes.interface import IATTopic

from plone.portlet.collection import PloneMessageFactory as _

from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile



# Import the base portlet module whose properties we will modify
from plone.portlet.static import static

class IspProjectsPortlet(static.IStaticPortlet):
    """ Defines a new portlet "grey static" which takes properties of the existing static text portlet. """
    pass

class spProjectsRenderer(static.Renderer):
    """ Overrides static.pt in the rendering of the portlet. """
    """Portlet renderer.
    
    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    _template = ViewPageTemplateFile('spProjects.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    # Cached version - needs a proper cache key
    # @ram.cache(render_cachekey)
    # def render(self):
    #     if self.available:
    #         return xhtml_compress(self._template())
    #     else:
    #         return ''

    render = _template

    @property
    def available(self):
        return len(self.results())

    def collection_url(self):
        collection = self.collection()
        if collection is None:
            return None
        else:
            return collection.absolute_url()

    def results(self):
        """ Get the actual result brains from the collection. 
            This is a wrapper so that we can memoize if and only if we aren't
            selecting random items."""
        if self.data.random:
            return self._random_results()
        else:
            return self._standard_results()

    @memoize
    def _standard_results(self):
        results = []
        collection = self.collection()
        if collection is not None:
            results = collection.queryCatalog()
            if self.data.limit and self.data.limit > 0:
                results = results[:self.data.limit]
        return results
        
    # intentionally non-memoized
    def _random_results(self):
        results = []
        collection = self.collection()
        if collection is not None:
            """
            Kids, do not try this at home.
            
            We're poking at the internals of the (lazy) catalog results to avoid
            instantiating catalog brains unnecessarily.
            
            We're expecting a LazyCat wrapping two LazyMaps as the return value from
            Products.ATContentTypes.content.topic.ATTopic.queryCatalog.  The second
            of these contains the results of the catalog query.  We force sorting
            off because it's unnecessary and might result in a different structure of
            lazy objects.
            
            Using the correct LazyMap (results._seq[1]), we randomly pick a catalog index
            and then retrieve it as a catalog brain using the _func method.
            """
            
            results = collection.queryCatalog(sort_on=None)
            limit = self.data.limit and min(len(results), self.data.limit) or 1
            try:
                results = [results._seq[1]._func(i) for i in random.sample(results._seq[1]._seq, limit)]
            except AttributeError, IndexError:
                # This handles the cases where the lazy objects returned by the catalog
                # are structured differently than expected.
                results = []
        return results
        
    @memoize
    def collection(self):
        """ get the collection the portlet is pointing to"""
        
        collection_path = self.data.target_collection
        if not collection_path:
            return None

        if collection_path.startswith('/'):
            collection_path = collection_path[1:]
        
        if not collection_path:
            return None

        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        portal = portal_state.portal()
        return portal.restrictedTraverse(collection_path, default=None)


class spProjectsAssignment(static.Assignment):
    """ Assigner for grey static portlet. """
    implements(IspProjectsPortlet)

class spProjectsAddForm(static.AddForm):
    """ Make sure that add form creates instances of our custom portlet instead of the base class portlet. """
    def create(self, data):
        return spGalleriesAssignment(**data)



