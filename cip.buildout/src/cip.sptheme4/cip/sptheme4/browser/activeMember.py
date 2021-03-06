from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils  import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot
from datetime import datetime

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
        #import pdb; pdb.set_trace()
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
        lencontent = len(catalog.searchResults(Creator = userId,
                                               portal_type = friendly_types,
                                               path = path)) - 1
        if lencontent < 0:
            lencontent = 0;
        return lencontent

    def activemembers3(self):
        """
        Getting the ten most active members
        """
        buffer = ""
        contentAll = []
        contentlenght = []
        users = self.context.acl_users.getUserIds()
        userLoad = []
        for userId in users:
            userLoad.append([userId, self.get_author_content(userId)])
        usersSorted = sorted(userLoad, key=lambda user: user[1], reverse=True)[:10]
        for userId in usersSorted:
            userName = userId[0]
            pImg = self.context.portal_membership.getPersonalPortrait(userName).tag()
            kk = pImg.find('" alt')
            returnImg = pImg[10:kk]
            contentAll.append([userId[0],userId[1], returnImg])
        return contentAll
        """
        Getting the members that have contributed more than 20 content items
        
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
        """



    def newMembers(self):
        """
        Getting the memberlist in the registration order
        """
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        buffer = ""
        contentAll = []
        contentlenght = []
        users = self.context.acl_users.getUserIds()
        userLoad = []
        contentAll = []
        for userId in users:
            author_content = self.get_author_content(userId)
            memfold = portal_catalog.searchResults({'id':userId})
            for i in memfold:
                km = i.created
            userLoad.append([userId, author_content, km])
        usersSorted = sorted(userLoad, key=lambda user: user[2], reverse=True)
        acl_users = getToolByName(self.context, 'acl_users')
        for userId in usersSorted:
            if userId[1] == -1:
                userId[1] = 0
            contentAll.append([userId[0],userId[1],userId[2]])
        return contentAll


    def allContentItems(self):
        """
            Fetch all the content items except the folders
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        portal_types = ['Document','File','Image','News Item','Event','Link','Institution','b-org Project','Gallery Folder','Discussion Item','Window']
        s = {}
        for n in portal_types:
            content_items = catalog.searchResults(portal_type = n)
            s[n] = len(content_items)
        return s

    def allTotal(self):
        """
            Fetch all the content items except the folders
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        portal_types = ['Document','File','Image','News Item','Event','Link','Institution','b-org Project','Gallery Folder','EasyNewsletter','Discussion Item']
        allItems = catalog.searchResults(portal_type = portal_types)
        return len(allItems)

    def allContentByArea(self):
        """
            Fetch all the content items except the folders
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        portal_types = ['Document','File','Image','News Item','Event','Link','Institution','b-org Project','Gallery Folder','EasyNewsletter','Discussion Item']
        areas = ['germplasm','seedsystem','crop-management','adding-value','use-consumption','institutions','projects-initiatives']
        areas2 = ['Germplasm','Seedsystem','Crop Management','Adding Value','Use Consumption','Institutions','Projects Initiatives']
        s = {}
        mm = {}
        for n in areas:
            folder_path = '/sweetpotato3/' + n
#            print folder_path
            content_items = catalog.searchResults(path={'query':folder_path})
            folders = catalog.searchResults(path={'query':folder_path}, portal_type = 'Folder')
            s[n] = len(content_items) - len(folders)
        z = 0
        for n in areas2:
            aa = areas[z]
            v = s[aa]
            mm[n] = v
            z = z + 1
        return mm


    def allMembers(self):
        """
        The initial member list creation, sorted by first name
        """
        mems = self.context.portal_membership.listMembers()
        mem_infos = []
        for m1 in mems:
            fn = m1.getProperty("firstname").capitalize()
            ln = m1.getProperty("lastname").capitalize()
            id = m1.id
            if fn == '':
                fun = m1.getProperty("fullname")
                fn = fun.split(" ")[0].capitalize()
            if ln == '':
                fun = m1.getProperty("fullname")
                ln = fun.split(" ")[-1].capitalize()
            mem_infos.append([fn, ln, m1.getProperty("institution"), '/author/'+id, self.get_author_content(id), m1.getProperty("location")])
        return sorted(mem_infos, key=lambda user: user[0], reverse=False)

    def sortByContent(self, memberlist):
        """
        Getting the memberlist created in allMembers section. Then sort the list by content created.
        """
        return sorted(memberlist, key=lambda user: user[4], reverse=True)

    def sortByLastname(self, memberlist):
        """
        Getting the memberlist created in allMembers section. Then sort the list by lastname.
        """
        return sorted(memberlist, key=lambda user: user[1], reverse=True)

    def sortByInstitution(self, memberlist):
        """
        Getting the memberlist created in allMembers section. Then sort the list by institution.
        """
        return sorted(memberlist, key=lambda user: user[2], reverse=True)


class ContentReview(BrowserView):
    """Default view of a Project Folder
    """
    __call__ = ViewPageTemplateFile('templates/contentreview.pt')

    def allContentItems(self):
        """
            Fetch all the content items except the folders
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        portal_types = ['Document','File','Image','News Item','Event','Link','Institution','b-org Project','Gallery Folder','Discussion Item','Window']
        s = {}
        for n in portal_types:
            content_items = catalog.searchResults(portal_type = n)
            s[n] = len(content_items)
        return s

    def allTotal(self):
        """
            Fetch all the content items except the folders
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        portal_types = ['Document','File','Image','News Item','Event','Link','Institution','b-org Project','Gallery Folder','EasyNewsletter','Discussion Item']
        allItems = catalog.searchResults(portal_type = portal_types)
        return len(allItems)

    def allContentByArea(self):
        """
            Fetch all the content items except the folders
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        portal_types = ['Document','File','Image','News Item','Event','Link','Institution','b-org Project','Gallery Folder','EasyNewsletter','Discussion Item']
        areas = ['germplasm','seedsystem','crop-management','adding-value','use-consumption','institutions','projects-initiatives']
        areas2 = ['Germplasm','Seedsystem','Crop Management','Adding Value','Use Consumption','Institutions','Projects Initiatives']
        s = {}
        mm = {}
        for n in areas:
            folder_path = '/sweetpotato3/' + n
#            print folder_path
            content_items = catalog.searchResults(path={'query':folder_path})
            folders = catalog.searchResults(path={'query':folder_path}, portal_type = 'Folder')
            s[n] = len(content_items) - len(folders)
        z = 0
        for n in areas2:
            aa = areas[z]
            v = s[aa]
            mm[n] = v
            z = z + 1
        return mm

    def notpublished(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        portal_url_obj = getToolByName(self.context, 'portal_url')
        portal_url = portal_url_obj.getPortalPath()
        folders = ['sweetpotato-introduction','germplasm','seedsystem','crop-management','adding-value','use-consumption','projects-initiatives','institutions']
        folds = []
        for i in folders:
            folds.append('/' + portal_url + '/' + i)
        contents = catalog.searchResults(path={'query':folds}, review_state='private')
        from Products.CMFPlone import Batch
        b_start = self.context.REQUEST.get('b_start', 0)
        b_size = 20
        batch = Batch(contents, b_size, int(b_start), orphan=0)
        return batch
  