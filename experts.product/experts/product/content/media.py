"""Definition of the Media content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from experts.product import productMessageFactory as _

from experts.product.interfaces import IMedia
from experts.product.config import PROJECTNAME

MediaSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'surname',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Surname"),
            description=_(u""),
        ),
    ),

	
    atapi.StringField(
        'firstname',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"First name"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'middlename',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Middle name"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'position',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Position"),
            description=_(u""),
        ),
    ),


    atapi.TextField(
        'roles',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Role(s)"),
            description=_(u""),
        ),
    ),



    atapi.TextField(
        'keywords',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Keywords"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'coverage',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Coverage"),
            description=_(u"Continental/Regional/National"),
        ),
    ),


    atapi.StringField(
        'pobox',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"P.O Box"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'town',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Town"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'postcode',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Post code"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'country',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Country"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'fixed',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Telephone - fixed"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'cellphone',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Telephone - cellular"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'fax',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Fax"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'email',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Email"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'facebook',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Facebook"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'twitter',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Twitter"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'website',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Website"),
            description=_(u""),
        ),
    ),


    atapi.DateTimeField(
        'datest',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Date established"),
            description=_(u""),
        ),
        validators=('isValidDate'),
    ),


    atapi.StringField(
        'keyedby',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Keyed by"),
            description=_(u""),
        ),
    ),


    atapi.TextField(
        'notes',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Notes"),
            description=_(u""),
        ),
    ),
	


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

MediaSchema['title'].storage = atapi.AnnotationStorage()
MediaSchema['description'].storage = atapi.AnnotationStorage()

MediaSchema['title'].widget.label = 'Media house'
# MediaSchema['description'].widget.visible['view'] = 'invisible'
# MediaSchema['description'].widget.visible['edit'] = 'invisible'

schemata.finalizeATCTSchema(MediaSchema, moveDiscussion=False)


class Media(base.ATCTContent):
    """Media Contact"""
    implements(IMedia)

    meta_type = "Media"
    schema = MediaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    surname = atapi.ATFieldProperty('surname')

    firstname = atapi.ATFieldProperty('firstname')

    middlename = atapi.ATFieldProperty('middlename')

    position = atapi.ATFieldProperty('position')

    roles = atapi.ATFieldProperty('roles')

    keywords = atapi.ATFieldProperty('keywords')

    coverage = atapi.ATFieldProperty('coverage')

    pobox = atapi.ATFieldProperty('pobox')

    town = atapi.ATFieldProperty('town')

    postcode = atapi.ATFieldProperty('postcode')

    country = atapi.ATFieldProperty('country')

    fixed = atapi.ATFieldProperty('fixed')

    cellphone = atapi.ATFieldProperty('cellphone')

    fax = atapi.ATFieldProperty('fax')

    email = atapi.ATFieldProperty('email')

    facebook = atapi.ATFieldProperty('facebook')

    twitter = atapi.ATFieldProperty('twitter')

    website = atapi.ATFieldProperty('website')

    datest = atapi.ATFieldProperty('datest')

    keyedby = atapi.ATFieldProperty('keyedby')

    notes = atapi.ATFieldProperty('notes')
	

atapi.registerType(Media, PROJECTNAME)
