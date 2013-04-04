"""Definition of the Research Paper content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cip.spcontent4.interfaces import IResearchPaper
from cip.spcontent4.config import PROJECTNAME

ResearchPaperSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ResearchPaperSchema['title'].storage = atapi.AnnotationStorage()
ResearchPaperSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(ResearchPaperSchema, moveDiscussion=False)


class ResearchPaper(base.ATCTContent):
    """A content type with Simple Dublin Core metadata fields"""
    implements(IResearchPaper)

    meta_type = "ResearchPaper"
    schema = ResearchPaperSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(ResearchPaper, PROJECTNAME)
