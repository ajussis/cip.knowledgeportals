"""Definition of the Project Folder content type
"""

from zope.interface import implements
from Products.CMFCore.utils  import getToolByName

from Products.Archetypes import atapi
from Products.Archetypes.atapi import ReferenceField
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata
from zope.component import getMultiAdapter
from Products.UserField.field import UserField

#from archetypes.referencebrowserwidget.interfaces import IFieldRelation
#from archetypes.referencebrowserwidget import ReferenceBrowserWidget
from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget
from Products.UserAndGroupSelectionWidget.widget import UserAndGroupSelectionWidget
# -*- Message Factory Imported Here -*-
from cip.spcontent4 import spcontent4MessageFactory as _

from cip.spcontent4.interfaces import IProjectFolder
from cip.spcontent4.config import PROJECTNAME


ProjectFolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.DateTimeField(
        'start',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Start date"),
            description=_(u"The startdate of the project"),
        ),
        required=False,
        validators=('isValidDate'),
    ),
    atapi.DateTimeField(
        'end',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"End date"),
            description=_(u"When will the project end"),
        ),
        validators=('isValidDate'),
    ),
    atapi.StringField(name='area',
#        allowed_types=('News Item','Folder'), # specify portal type names here ('Example Type',)
        relationship='projectfolder_area',
        vocabulary="getAreas",
        storage=atapi.AnnotationStorage(),
        widget=atapi.InAndOutWidget(
            label=_(u"Geographical Area"),
            description=_(u"Geographical area of the project"),),
        multiValued=False,
        ),
#    atapi.ReferenceField(
#        'leader',
#        relationship='projectfolder_leader',
#        storage=atapi.AnnotationStorage(),
#        vocabulary="getMembers",
#        enforceVocabulary=True,
#        widget=atapi.StringWidget(
#            label=_(u"Project Leader"),
#            description=_(u"The name of the project leader"),
#        )),
    atapi.StringField(
        'leaderText',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Project leader name"),
            description=_(u"Project leader"),
        )),
    atapi.TextField(
        'financing',
        required=False,
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Financing"),
            description=_(u"The financing sources of the project"),
        )),
    UserField(
        'users',
#        storage=atapi.AnnotationStorage(),
#        widget=UserAndGroupSelectionWidget(
#            label=_(u"Project Members"),
#            description=_(u"Members in of the project which are also members of this portal"),
#            size=9,
#        ),
#        required=False,
#        relationship='projectfolder_members',
#        allowed_types=(), # specify portal type names here ('Example Type',)
        multiValued=True,
#        vocabulary="getMembers",
    ),
#    UserField('users', multiValued=True),
    atapi.TextField(
        'info',
        default_output_type = 'text/x-html-safe',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"More information"),
            description=_(u"More information about the project"),
        ),
    ),
    atapi.ImageField(
        'image',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Project Image"),
            description=_(u"Insert the project's logo or a representative image"),
        ),
        validators=('isNonEmptyFile'),
    ),
))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

ProjectFolderSchema['title'].storage = atapi.AnnotationStorage()
ProjectFolderSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    ProjectFolderSchema,
    folderish=True,
    moveDiscussion=False
)


class ProjectFolder(folder.ATFolder):
    """The container for Sweetpotato Projects"""
    implements(IProjectFolder)

    meta_type = "ProjectFolder"
    schema = ProjectFolderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    image = atapi.ATFieldProperty('image')

    leaderText = atapi.ATFieldProperty('leaderText')

    info = atapi.ATFieldProperty('info')

#    leader = atapi.ATReferenceFieldProperty('leader')

    financing = atapi.ATFieldProperty('financing')

    end = atapi.ATFieldProperty('end')

    start = atapi.ATFieldProperty('start')

    area = atapi.ATFieldProperty('area')

    def getAreas(self):
        dl = ["Europa","Asia","Africa","South America","Central America"]
        return dl

    def getMembers(self):
        users2 = self.acl_users.getUserIds()
#        return memberIds
#        users = self.acl_users.getUsers()
        return users2
#        for user in users:
#            print"Got username:"+user


#    security.declarePublic("getMyItems")
    def getSomething(self):
        buffer=""
        s = ['sdf','sdf']
        # Returns list of site usernames
#        users=self.acl_users.getUserNames()
        # alternative: get user objects#

        return s
#        self.portal_state = getMultiAdapter((self, self.request), name=u'plone_portal_state')



atapi.registerType(ProjectFolder, PROJECTNAME)
