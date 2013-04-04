from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class UploadView(BrowserView):
    """ The Upload View
    """

    template = ViewPageTemplateFile("templates/upload.pt")

    def __call__(self):
        return self.template()
