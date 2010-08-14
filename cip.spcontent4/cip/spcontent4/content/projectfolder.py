"""Definition of the Project Folder content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from cip.spcontent4 import spcontent4MessageFactory as _

from cip.spcontent4.interfaces import IProjectFolder
from cip.spcontent4.config import PROJECTNAME

ProjectFolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.TextField(
        'financing',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Financing"),
            description=_(u"The financing sources of the project"),
        ),
        required=True,
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


    atapi.DateTimeField(
        'start',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Start date"),
            description=_(u"The startdate of the project"),
        ),
        required=True,
        validators=('isValidDate'),
    ),


    atapi.ReferenceField(
        'area',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ReferenceWidget(
            label=_(u"Geographical Area"),
            description=_(u"Geographical area of the project"),
        ),
        required=True,
        relationship='projectfolder_area',
        allowed_types=(), # specify portal type names here ('Example Type',)
        multiValued=False,
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
    financing = atapi.ATFieldProperty('financing')

    end = atapi.ATFieldProperty('end')

    start = atapi.ATFieldProperty('start')

    area = atapi.ATReferenceFieldProperty('area')


atapi.registerType(ProjectFolder, PROJECTNAME)
