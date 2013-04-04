"""Definition of the Institutions Holder content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cip.spcontent4.interfaces import IInstitutionsHolder
from cip.spcontent4.config import PROJECTNAME

InstitutionsHolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

InstitutionsHolderSchema['title'].storage = atapi.AnnotationStorage()
InstitutionsHolderSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    InstitutionsHolderSchema,
    folderish=True,
    moveDiscussion=False
)


class InstitutionsHolder(folder.ATFolder):
    """Folder to contain institutions"""
    implements(IInstitutionsHolder)

    meta_type = "InstitutionsHolder"
    schema = InstitutionsHolderSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(InstitutionsHolder, PROJECTNAME)
