"""Definition of the Gallery Folder content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from cip.spcontent4 import spcontent4MessageFactory as _

from cip.spcontent4.interfaces import IGalleryFolder
from cip.spcontent4.config import PROJECTNAME

GalleryFolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'area',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Gallery Area"),
            description=_(u"Field description"),
        ),
        required=True,
    ),


))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

GalleryFolderSchema['title'].storage = atapi.AnnotationStorage()
GalleryFolderSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    GalleryFolderSchema,
    folderish=True,
    moveDiscussion=False
)


class GalleryFolder(folder.ATFolder):
    """Folder to hold images and show them in gallery view"""
    implements(IGalleryFolder)

    meta_type = "GalleryFolder"
    schema = GalleryFolderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    area = atapi.ATFieldProperty('area')


atapi.registerType(GalleryFolder, PROJECTNAME)
