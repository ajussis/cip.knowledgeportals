from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName

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
            author_content = len(self.context.author_find_content(userId)) - 1
            userLoad.append([userId, author_content])
#        import ipdb; ipdb.set_trace()

        usersSorted = sorted(userLoad, key=lambda user: user[1], reverse=True)
        acl_users = getToolByName(self.context, 'acl_users')

        for userId in usersSorted:
#            userid = acl_users.getUserById(userId)
#            member_name = userid.getProperty('fullname')
            userName = userId[0]
            pImg = self.context.portal_membership.getPersonalPortrait(userName).tag()
            kk = pImg.find('" alt')
            returnImg = pImg[10:kk]
            if userId[1] == -1:
                userId[1] = 0
            contentAll.append([userId[0],userId[1], returnImg])
#        import pdb
#        pdb.set_trace()
#        creator = self.context.Creator()
        return contentAll
