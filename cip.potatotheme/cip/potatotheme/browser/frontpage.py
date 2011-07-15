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

    def testing(self):
        import pdb; pdb.set_trace()
        
    def latestUpdates(self):
        latest = self.context.portal_catalog.searchResults({'path' : '/'.join(self.context.getPhysicalPath()), 'portal_type':['Folder','File','Event','Gallery Folder','Institution','Link','Document'], 'sort_on':'Date', 'sort_order':'Reverse'})[:4]
        finals = []
        for i in latest:
            section = i.getURL().split('/')[4].capitalize()
            finals.append([i,section,section+'-icon.gif'])
        return finals

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
    
    def activeUsers(self):
        users = self.context.acl_users.getUserIds()
        now = DateTime()
        month = DateTime() - 30
        activelist = []
        for user in users:
            activelist.append([len(self.context.portal_catalog.searchResults(created = { "query": [month, now],"range": "minmax" }, Creator=user)),len(self.context.portal_catalog.searchResults(created = { "query": [month, now],"range": "minmax" }, Creator=user)),user])
        activelist.sort()
        activelist.reverse()
        activelist = activelist[:6]
        finals = []
        for user in activelist:
            try:
                fullname = self.context.portal_membership.getMemberById(user[2]).getProperty("fullname")
            except:
                fullname = "Administrator"
            try:
                img = self.context.portal_membership.getPersonalPortrait(user[2]).absolute_url()
            except:
                img = "defaultUser.gif"
            finals.append([user[0], user[1], fullname, img, '/potato/Members/'+user[2],self.context.portal_membership.getMemberById(user[2]).getProperty("institution")])
        return finals

    def galleries(self):
        return self.context.portal_catalog.searchResults(portal_type="Gallery Folder", sort_on="Date", sort_order="Reverse")[:3]
