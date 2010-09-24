from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from Products.CMFCore.utils import getToolByName

class ProjectView(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/project.pt')

    def Usernames(self, user):
        acl_users = getToolByName(self.context, 'acl_users')
        userid = acl_users.getUserById(user)
        member_name = userid.getProperty('fullname')
        return member_name