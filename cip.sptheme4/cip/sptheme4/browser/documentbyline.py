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