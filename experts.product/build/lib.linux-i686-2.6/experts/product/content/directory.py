"""Definition of the Directory content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from experts.product.interfaces import IDirectory
from experts.product.config import PROJECTNAME

DirectorySchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

DirectorySchema['title'].storage = atapi.AnnotationStorage()
DirectorySchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(DirectorySchema, moveDiscussion=False)


class Directory(base.ATCTContent):
    """Experts directory content type"""
    implements(IDirectory)

    meta_type = "Directory"
    schema = DirectorySchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Directory, PROJECTNAME)
