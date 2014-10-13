"""Definition of the Photo content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from cip.spcontent4 import spcontent4MessageFactory as _

from cip.spcontent4.interfaces import IPhoto
from cip.spcontent4.config import PROJECTNAME

PhotoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.ImageField(
        'image',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Image"),
            description=_(u"Image file"),
        ),
        validators=('isNonEmptyFile'),
    ),


    atapi.TextField(
        'description',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Description"),
            description=_(u"Description"),
        ),
    ),


    atapi.StringField(
        'title',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Title"),
            description=_(u"Title"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

PhotoSchema['title'].storage = atapi.AnnotationStorage()
PhotoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(PhotoSchema, moveDiscussion=False)


class Photo(base.ATCTContent):
    """Experts Photo"""
    implements(IPhoto)

    meta_type = "Photo"
    schema = PhotoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    image = atapi.ATFieldProperty('image')

    description = atapi.ATFieldProperty('description')

    title = atapi.ATFieldProperty('title')


atapi.registerType(Photo, PROJECTNAME)
