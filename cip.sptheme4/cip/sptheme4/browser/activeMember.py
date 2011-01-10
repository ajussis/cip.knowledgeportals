from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot

class ActiveMember(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/mostactives.pt')

    def activemembers(self):
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
#            author_content = len(self.context.author_find_content(userId)) - 1
            author_content = self.get_author_content(userId)
            userLoad.append([userId, author_content])
#        import ipdb; ipdb.set_trace()

        usersSorted = sorted(userLoad, key=lambda user: user[1], reverse=True)
        acl_users = getToolByName(self.context, 'acl_users')

        for userId in usersSorted:
#            userid = acl_users.getUserById(userId)
#            member_name = userid.getProperty('fullname')
            userName = userId[0]
            if userId[1] == -1:
                userId[1] = 0
            contentAll.append([userId[0],userId[1]])
#        import pdb
#        pdb.set_trace()
#        creator = self.context.Creator()
        return contentAll

    def activemembersByName(self):
        """
        """
        buffer = ""
        contentAll = []
        contentlenght = []
        users = self.context.acl_users.getUserIds()
        userLoad = []
        contentAll = []
        for userId in users:
            author_content = self.get_author_content(userId)
            userLoad.append([userId, author_content])
        usersSorted = sorted(userLoad, key=lambda user: user[0], reverse=True)
        acl_users = getToolByName(self.context, 'acl_users')
        for userId in usersSorted:
            if userId[1] == -1:
                userId[1] = 0
            contentAll.append([userId[0],userId[1]])
        return contentAll

    def get_author_content(self, userId, path = None):
        catalog = getToolByName(self.context, 'portal_catalog')
        utils = getToolByName(self.context, 'plone_utils')
        friendly_types = utils.getUserFriendlyTypes()
        found = {}
        if path is None:
            path = getNavigationRoot(self.context)
        content = catalog.searchResults(Creator = userId,
                                        portal_type = friendly_types,
                                        path = path)
        return len(content) - 1

    def activemembers3(self):
        """
        """
        buffer = ""
        contentAll = []
        contentlenght = []
        users = self.context.acl_users.getUserIds()
        userLoad = []
        for userId in users:
            author_content = self.get_author_content(userId)
            if author_content > 19:
                userLoad.append([userId, author_content])
        usersSorted = sorted(userLoad, key=lambda user: user[1], reverse=True)
        for userId in usersSorted:
            userName = userId[0]
            pImg = self.context.portal_membership.getPersonalPortrait(userName).tag()
            kk = pImg.find('" alt')
            returnImg = pImg[10:kk]
            contentAll.append([userId[0],userId[1], returnImg])
        return contentAll