"""Definition of the ProjectType content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from cip.spcontent4 import spcontent4MessageFactory as _

from cip.spcontent4.interfaces import IProjectType
from cip.spcontent4.config import PROJECTNAME

ProjectTypeSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'test',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"New Field"),
            description=_(u"Field description"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ProjectTypeSchema['title'].storage = atapi.AnnotationStorage()
ProjectTypeSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(ProjectTypeSchema, moveDiscussion=False)


class ProjectType(base.ATCTContent):
    """Description of the Example Type"""
    implements(IProjectType)

    meta_type = "ProjectType"
    schema = ProjectTypeSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    test = atapi.ATFieldProperty('test')


atapi.registerType(ProjectType, PROJECTNAME)
