from plone.app.layout.viewlets.content import DocumentBylineViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class DocumentBylineViewlet(DocumentBylineViewlet):
    render = ViewPageTemplateFile("templates/document_byline.pt")
