from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot
from datetime import datetime

class FrontpageView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/frontpage.pt')

    def testing(self):
        import pdb; pdb.set_trace()
        
    def latestUpdates(self):
        pubpath = (self.context.portal_url.getPortalPath()+'/germplasm/')
        return self.context.portal_catalog.searchResults(sort_on="Date", sort_order="reverse")[:5]
