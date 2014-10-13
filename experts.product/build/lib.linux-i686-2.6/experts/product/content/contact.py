"""Definition of the Contact content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from experts.product import productMessageFactory as _

from experts.product.interfaces import IContact
from experts.product.config import PROJECTNAME

ContactSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'surname',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Surname"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'first',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"First name"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'middle',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Middle name"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'position',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Position"),
            description=_(u"Field description"),
        ),
    ),


    atapi.TextField(
        'roles',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Role(s)"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'category',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Category"),
            description=_(u"Field description"),
        ),
    ),


    atapi.TextField(
        'keywords',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Keywords"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'coverage',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Coverage"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'pobox',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"P.O Box"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'town',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Town"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'postcode',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Post code"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'country',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Country"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'telephone',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Telephone - fixed"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'cellphone',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Telephone- cellular"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'fax',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Fax"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'email',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Email"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'facebook',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Facebook"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'twitter',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Twitter"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'website',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Website"),
            description=_(u"Field description"),
        ),
    ),


    atapi.DateTimeField(
        'datest',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Date established"),
            description=_(u"Field description"),
        ),
        validators=('isValidDate'),
    ),


    atapi.StringField(
        'keyed',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Keyed by"),
            description=_(u"Field description"),
        ),
    ),


    atapi.TextField(
        'notes',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Notes"),
            description=_(u"Field description"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ContactSchema['title'].storage = atapi.AnnotationStorage()
ContactSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(ContactSchema, moveDiscussion=False)


class Contact(base.ATCTContent):
    """Media and communication contact"""
    implements(IContact)

    meta_type = "Contact"
    schema = ContactSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    surname = atapi.ATFieldProperty('surname')

    first = atapi.ATFieldProperty('first')

    middle = atapi.ATFieldProperty('middle')

    position = atapi.ATFieldProperty('position')

    roles = atapi.ATFieldProperty('roles')

    category = atapi.ATFieldProperty('category')

    keywords = atapi.ATFieldProperty('keywords')

    coverage = atapi.ATFieldProperty('coverage')

    pobox = atapi.ATFieldProperty('pobox')

    town = atapi.ATFieldProperty('town')

    postcode = atapi.ATFieldProperty('postcode')

    country = atapi.ATFieldProperty('country')

    telephone = atapi.ATFieldProperty('telephone')

    cellphone = atapi.ATFieldProperty('cellphone')

    fax = atapi.ATFieldProperty('fax')

    email = atapi.ATFieldProperty('email')

    facebook = atapi.ATFieldProperty('facebook')

    twitter = atapi.ATFieldProperty('twitter')

    website = atapi.ATFieldProperty('website')

    datest = atapi.ATFieldProperty('datest')

    keyed = atapi.ATFieldProperty('keyed')

    notes = atapi.ATFieldProperty('notes')


atapi.registerType(Contact, PROJECTNAME)
