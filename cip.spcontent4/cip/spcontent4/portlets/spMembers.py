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

class IMembersPortlet(IPortletDataProvider):

    count = schema.Int(title=_(u'Number of items to display'),
                       description=_(u'How many items to list.'),
                       required=True,
                       default=5)

class Assignment(base.Assignment):
    implements(IMembersPortlet)

    def __init__(self, count=5):
        self.count = count

    @property
    def title(self):
        return _(u"most Active Members")

def _render_cachekey(fun, self):
    if self.anonymous:
        raise ram.DontCache()
    return render_cachekey(fun, self)

class Renderer(base.Renderer):
    _template = ViewPageTemplateFile('spMembers.pt')

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
        return not self.anonymous and len(self._data())
    
    def mostactivemembers(self):
        """
        """
        buffer = ""
        contentAll = []
        # Returns list of site usernames
        #users = self.context.acl_users.getUserNames()
        contentlenght = []
        users = self.context.acl_users.getUserIds()

#        for userId in users:
#            author_content = len(self.context.author_find_content(userId))
#            pImg = self.context.portal_membership.getPersonalPortrait(userId).tag()
#            kk = pImg.find('" alt')
#            returnImg = pImg[10:kk]
#            contentAll.append([userId,author_content, returnImg])
#            print contentAll"""

        userLoad = []
        contentAll = []
        for userId in users:
            author_content = len(self.context.author_find_content(userId))
            userLoad.append([userId, author_content])
#        import ipdb; ipdb.set_trace()
        sorted(userLoad, key=lambda user: user[1], reverse=True)
        usersAll = []
        usersAll = userLoad[:5]
        for userId in usersAll:
            userName = userId[0]
            pImg = self.context.portal_membership.getPersonalPortrait(userName).tag()
            kk = pImg.find('" alt')
            returnImg = pImg[10:kk]
            contentAll.append([userId[0],userId[1], returnImg])
#        import pdb
#        pdb.set_trace()
#        creator = self.context.Creator()
        return contentAll

        # alternative: get user objects
        #users = context.acl_users.getUsers()

        #mt = getToolByName(self.context, 'portal_membership')
        #if mt.isAnonymousUser(): # the user has not logged in
        #    return "ei oo kuule"
        #else:
        #    member = mt.getAuthenticatedMember()
        #    username = member.getUserName()
        return contentAll


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
    form_fields = form.Fields(IMembersPortlet)
    label = _(u"Add Recent Portlet")
    description = _(u"This portlet displays recently modified content.")

    def create(self, data):
        return Assignment(count=data.get('count', 5))

class EditForm(base.EditForm):
    form_fields = form.Fields(IMembersPortlet)
    label = _(u"Edit Recent Portlet")
    description = _(u"This portlet displays recently modified content.")
