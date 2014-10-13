"""Definition of the Photo content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from experts.product import productMessageFactory as _

from experts.product.interfaces import IPhoto
from experts.product.config import PROJECTNAME

PhotoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.TextField(
        'comments',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Comments"),
            description=_(u"Comments"),
        ),
    ),


    atapi.StringField(
        'program',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Program"),
            description=_(u"Program / Project"),
        ),
    ),


    atapi.StringField(
        'institution',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Institution"),
            description=_(u"Institution"),
        ),
    ),


    atapi.StringField(
        'photographer',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Photographer"),
            description=_(u"Photographer"),
        ),
    ),


    atapi.StringField(
        'category',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Category"),
            description=_(u"Category"),
        ),
    ),


    atapi.TextField(
        'keywords',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Keywords"),
            description=_(u"Keywords"),
        ),
    ),


    atapi.DateTimeField(
        'date',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Date"),
            description=_(u"Date"),
        ),
        validators=('isValidDate'),
    ),


    atapi.StringField(
        'location',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Location"),
            description=_(u"Location"),
        ),
    ),


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
        'caption',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Caption"),
            description=_(u"Caption"),
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
    """Photo content type"""
    implements(IPhoto)

    meta_type = "Photo"
    schema = PhotoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    comments = atapi.ATFieldProperty('comments')

    program = atapi.ATFieldProperty('program')

    institution = atapi.ATFieldProperty('institution')

    photographer = atapi.ATFieldProperty('photographer')

    category = atapi.ATFieldProperty('category')

    keywords = atapi.ATFieldProperty('keywords')

    date = atapi.ATFieldProperty('date')

    location = atapi.ATFieldProperty('location')

    image = atapi.ATFieldProperty('image')

    # description = atapi.ATFieldProperty('description')

    title = atapi.ATFieldProperty('title')


atapi.registerType(Photo, PROJECTNAME)
