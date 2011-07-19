from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot
from datetime import datetime
from DateTime import DateTime

class FrontpageView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/frontpage.pt')


    def latestDiscussion(self):
        conversations = self.context.portal_catalog.searchResults(sort_on="Date", sort_order="Reverse", portal_type="PloneboardConversation")[:4]
        infos = []
        for i in conversations: 
            cob = i.getObject()
            try:
                userId = cob.getOwner().getUserId()
                fullname = self.context.portal_membership.getMemberById(userId).getProperty("fullname")
            except:
                fullname = "Administrator"
            try:
                img = self.context.portal_membership.getPersonalPortrait(userId).absolute_url()
            except:
                img = "generalPortrait.jpg"
            infos.append([cob.title, fullname, img, cob.getNumberOfComments()-1, cob.absolute_url()])
        return infos