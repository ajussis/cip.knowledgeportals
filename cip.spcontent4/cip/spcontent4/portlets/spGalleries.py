from plone.memoize import ram
from plone.memoize.compress import xhtml_compress
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements
from zope import schema

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.portlets import PloneMessageFactory as _
from plone.app.portlets.cache import render_cachekey
from plone.app.portlets.portlets import base
from Products.CMFCore.utils  import getToolByName

class IGalleriesPortlet(IPortletDataProvider):

    count = schema.Int(title=_(u'Number of items to display'),
                       description=_(u'How many items to list.'),
                       required=True,
                       default=5)

class Assignment(base.Assignment):
    implements(IGalleriesPortlet)

    def __init__(self, count=5):
        self.count = count

    @property
    def title(self):
        return _(u"Latest Galleries")

def _render_cachekey(fun, self):
    if self.anonymous:
        raise ram.DontCache()
    return render_cachekey(fun, self)

class Renderer(base.Renderer):
    _template = ViewPageTemplateFile('spGalleries.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
        self.anonymous = portal_state.anonymous()
        self.navigation_root_url = portal_state.navigation_root_url()
        self.typesToShow = portal_state.friendly_types()
        self.navigation_root_path = portal_state.navigation_root_path()

        plone_tools = getMultiAdapter((context, self.request), name=u'plone_tools')
        self.catalog = plone_tools.catalog()

    @ram.cache(_render_cachekey)
    def render(self):
        return xhtml_compress(self._template())

    @property
    def available(self):
        return len(self._data())

    def recent_items(self):
        return self._data()

    def recently_modified_link(self):
        return '%s/recently_modified' % self.navigation_root_url

    @memoize
    def _data(self):
        context = aq_inner(self.context)
        limit = self.data.count
        path = self.navigation_root_path
        return self.catalog(portal_type=self.typesToShow,
                            path=path,
                            sort_on='modified',
                            sort_order='reverse',
                            sort_limit=limit)[:limit]

class AddForm(base.AddForm):
    form_fields = form.Fields(IGalleriesPortlet)
    label = _(u"Add Galleries Portlet")
    description = _(u"This portlet displays the latest galleries.")

    def create(self, data):
        return Assignment(count=data.get('count', 5))

class EditForm(base.EditForm):
    form_fields = form.Fields(IGalleriesPortlet)
    label = _(u"Edit Galleries Portlet")
    description = _(u"This portlet displays the latest galleries.")