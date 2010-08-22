"""Definition of the Institution content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from cip.spcontent4 import spcontent4MessageFactory as _

from cip.spcontent4.interfaces import IInstitution
from cip.spcontent4.config import PROJECTNAME

InstitutionSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'headquarters',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Headquarters"),
            description=_(u"Address, City, Country"),
        ),
    ),
    atapi.StringField(
        'website',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Website"),
            description=_(u"Website of the Institution"),
        ),
    ),
    atapi.ReferenceField(
        'area',
        vocabulary="getAreas",
        storage=atapi.AnnotationStorage(),
        widget=atapi.InAndOutWidget(
            label=_(u"Geographical Area"),
            description=_(u"On which parts of the world the institution operates"),
        ),
        relationship='institution_area',
        allowed_types=(), # specify portal type names here ('Example Type',)
        multiValued=False,
    ),
    atapi.TextField(
        'info',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"General Information"),
            description=_(u"More information about the institution"),
        ),
    ),



))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

InstitutionSchema['title'].storage = atapi.AnnotationStorage()
InstitutionSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    InstitutionSchema,
    folderish=True,
    moveDiscussion=False
)


class Institution(folder.ATFolder):
    """Institution Content Type"""
    implements(IInstitution)

    meta_type = "Institution"
    schema = InstitutionSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    info = atapi.ATFieldProperty('info')

    headquarters = atapi.ATFieldProperty('headquarters')

    website = atapi.ATFieldProperty('website')

    area = atapi.ATReferenceFieldProperty('area')

    headquarters = atapi.ATFieldProperty('headquarters')

    def getAreas(self):
        dl = ["Europa","Asia","Africa","South America","Central America"]
        return dl



atapi.registerType(Institution, PROJECTNAME)
