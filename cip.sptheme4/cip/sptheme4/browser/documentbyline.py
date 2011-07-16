from plone.app.layout.viewlets.content import DocumentBylineViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName


class DocumentBylineViewlet(DocumentBylineViewlet):
    render = ViewPageTemplateFile("templates/document_byline.pt")

    def getUserImage(self, userName):
        pImg = self.context.portal_membership.getPersonalPortrait(userName).tag()
        cutImg = pImg.find('" alt')
        returnImg = pImg[10:cutImg]
        return returnImg

    def Usernames(self, user):
        acl_users = getToolByName(self.context, 'acl_users')
        member_name = acl_users.getUserById(user)

        if member_name is not None:
            member_name = member_name.getProperty('fullname')
        return member_name