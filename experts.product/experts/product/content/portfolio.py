"""Definition of the Portfolio content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from experts.product import productMessageFactory as _

from experts.product.interfaces import IPortfolio
from experts.product.config import PROJECTNAME

PortfolioSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'country',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Country"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'region',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Region"),
            description=_(u""),
        ),
    ),


#    atapi.StringField(
#        'title',
#        storage=atapi.AnnotationStorage(),
#        widget=atapi.StringWidget(
#            label=_(u"Project/Programme name"),
#            description=_(u""),
#        ),
#    ),


    atapi.StringField(
        'donor_',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Donor"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'donor',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Donor Code"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'zone',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Region/State/Zone/Province"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'locality',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Locality"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'seedsystem',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Sweetpotato Seed Systems"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'production',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Sweetpotato Production"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'nutrition',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Sweetpotato Nutrition"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'postharvest',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Sweetpotato Post Harvest"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'trade',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Sweetpotato Trade and Marketing"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'advocacy',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Sweetpotato Advocacy and Capacity Building"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'ickm',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Sweetpotato ICKM"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'period',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Period"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'status',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Status"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'amount',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Amount"),
            description=_(u""),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

PortfolioSchema['title'].storage = atapi.AnnotationStorage()
PortfolioSchema['description'].storage = atapi.AnnotationStorage()

PortfolioSchema['title'].widget.label = 'Project/Programme name'
# PortfolioSchema['title'].widget.visible['edit'] = 'invisible'

PortfolioSchema['description'].widget.visible['view'] = 'invisible'
PortfolioSchema['description'].widget.visible['edit'] = 'invisible'

schemata.finalizeATCTSchema(PortfolioSchema, moveDiscussion=False)


class Portfolio(base.ATCTContent):
    """CIP Investment Portfolio"""
    implements(IPortfolio)

    meta_type = "Portfolio"
    schema = PortfolioSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    country = atapi.ATFieldProperty('country')

    region = atapi.ATFieldProperty('region')

#    title = atapi.ATFieldProperty('title')

    donor_ = atapi.ATFieldProperty('donor_')

    donor = atapi.ATFieldProperty('donor')

    zone = atapi.ATFieldProperty('zone')

    locality = atapi.ATFieldProperty('locality')

    seedsystem = atapi.ATFieldProperty('seedsystem')

    production = atapi.ATFieldProperty('production')

    nutrition = atapi.ATFieldProperty('nutrition')

    postharvest = atapi.ATFieldProperty('postharvest')

    trade = atapi.ATFieldProperty('trade')

    advocacy = atapi.ATFieldProperty('advocacy')

    ickm = atapi.ATFieldProperty('ickm')

    period = atapi.ATFieldProperty('period')

    status = atapi.ATFieldProperty('status')

    amount = atapi.ATFieldProperty('amount')


atapi.registerType(Portfolio, PROJECTNAME)
