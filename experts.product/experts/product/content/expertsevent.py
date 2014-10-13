"""Definition of the Experts Event content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from experts.product import productMessageFactory as _

from experts.product.interfaces import IExpertsEvent
from experts.product.config import PROJECTNAME

ExpertsEventSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'venue',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Location"),
            description=_(u"Town and country"),
        ),
    ),


    atapi.StringField(
        'location',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Location"),
            description=_(u"Town and country"),
        ),
    ),


    atapi.DateTimeField(
        'startdate',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Start Date"),
            description=_(u""),
        ),
        validators=('isValidDate'),
    ),


    atapi.DateTimeField(
        'enddate',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"End Date"),
            description=_(u""),
        ),
        validators=('isValidDate'),
    ),


    atapi.StringField(
        'eventtype',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Event Type"),
            description=_(u"Workshop/Conference/Training/Meeting"),
        ),
    ),


    atapi.StringField(
        'project',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Project / Programme"),
            description=_(u""),
        ),
    ),


    atapi.TextField(
        'partners',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Partners"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'location',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Location"),
            description=_(u"Town and Country"),
        ),
    ),


    atapi.TextField(
        'organizers',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Organizer(s)"),
            description=_(u""),
        ),
    ),


    atapi.TextField(
        'contact',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Contact"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'url',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"URL"),
            description=_(u""),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ExpertsEventSchema['title'].storage = atapi.AnnotationStorage()
ExpertsEventSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(ExpertsEventSchema, moveDiscussion=False)


class ExpertsEvent(base.ATCTContent):
    """Sweetpotato experts event"""
    implements(IExpertsEvent)

    meta_type = "ExpertsEvent"
    schema = ExpertsEventSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    venue = atapi.ATFieldProperty('venue')

    location = atapi.ATFieldProperty('location')

    startdate = atapi.ATFieldProperty('startdate')

    enddate = atapi.ATFieldProperty('enddate')

    eventtype = atapi.ATFieldProperty('eventtype')

    project = atapi.ATFieldProperty('project')

    partners = atapi.ATFieldProperty('partners')

    location = atapi.ATFieldProperty('location')

    organizers = atapi.ATFieldProperty('organizers')

    contact = atapi.ATFieldProperty('contact')

    url = atapi.ATFieldProperty('url')

    schema.moveField('venue',after = 'partners')

atapi.registerType(ExpertsEvent, PROJECTNAME)
