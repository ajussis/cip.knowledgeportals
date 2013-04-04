from plone.app.layout.viewlets import ViewletBase
from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from datetime import date
from plone.app.portlets.cache import render_cachekey
from plone.memoize import ram
from Products.Five.browser import BrowserView

# Sample code for a basic viewlet (In order to use it, you'll have to):
# - Un-comment the following useable piece of code (viewlet python class).
# - Rename the viewlet template file ('browser/viewlet.pt') and edit the
#   following python code accordingly.
# - Edit the class and template to make them suit your needs.
# - Make sure your viewlet is correctly registered in 'browser/configure.zcml'.
# - If you need it to appear in a specific order inside its viewlet manager,
#   edit 'profiles/default/viewlets.xml' accordingly.
# - Restart Zope.
# - If you edited any file in 'profiles/default/', reinstall your package.
# - Once you're happy with your viewlet implementation, remove any related
#   (unwanted) inline documentation  ;-p

#class MyViewlet(ViewletBase):
#    render = ViewPageTemplateFile('viewlet.pt')
#
#    def update(self):
#        self.computed_value = 'any output'

class FrontpageProjectsView(BrowserView):
    """ View for the projects front page
    """
    __call__ = ViewPageTemplateFile('templates/frontpage_projects.pt')

    def projects(self):
        pros = self.context.portal_catalog.searchResults(portal_type="Project Folder")

        return pros

    def featuredProjects(self):
        pros = self.context.portal_catalog.searchResults(portal_type="Project Folder")
        featured = []
        for i in pros:
            obj = i.getObject()
            if obj.getFeaturedproject() is True:
                featured.append(i)
        return featured

"""
portal = app.sweetpotato3
pros = portal.portal_catalog.searchResults(portal_type="Project Folder")
featured = []
for i in pros:
    print i.Title
    obj = i.getObject()
    if obj.getFeaturedproject() is True:
        featured.append(i)
        print "This is featured"
    else:
        print "This is not featured"

p = pros[0]
b = p.getObject()
b.getFeaturedproject
b.getFinancing

p1 = pros[1]
b1 = p1.getObject()
b1.getFeaturedproject
b1.getFinancing
"""


class FooterViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/footer.pt')

    def update(self):
        self.year = date.today().year

class SiteActionsViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/site_actions.pt')

    def update(self):
        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')
        self.site_actions = context_state.actions('site_actions')

class NavigationViewlet(ViewletBase):

    _template = ViewPageTemplateFile('templates/navigation.pt')

    @ram.cache(render_cachekey)
    def render(self):
        return xhtml_compress(self._template())
