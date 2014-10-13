from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from experts.product import productMessageFactory as _



class IPhoto(Interface):
    """Photo content type"""

    # -*- schema definition goes here -*-
    comments = schema.Text(
        title=_(u"Comments"),
        required=False,
        description=_(u"Comments"),
    )
#
    program = schema.TextLine(
        title=_(u"Program"),
        required=False,
        description=_(u"Program / Project"),
    )
#
    institution = schema.TextLine(
        title=_(u"Institution"),
        required=False,
        description=_(u"Institution"),
    )
#
    photographer = schema.TextLine(
        title=_(u"Photographer"),
        required=False,
        description=_(u"Photographer"),
    )
#
    category = schema.TextLine(
        title=_(u"Category"),
        required=False,
        description=_(u"Category"),
    )
#
    keywords = schema.Text(
        title=_(u"Keywords"),
        required=False,
        description=_(u"Keywords"),
    )
#
    date = schema.Date(
        title=_(u"Date"),
        required=False,
        description=_(u"Date"),
    )
#
    location = schema.TextLine(
        title=_(u"Location"),
        required=False,
        description=_(u"Location"),
    )
#
    image = schema.Bytes(
        title=_(u"Image"),
        required=False,
        description=_(u"Image file"),
    )
#
    description = schema.Text(
        title=_(u"Description"),
        required=False,
        description=_(u"Description"),
    )
#
    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
        description=_(u"Title"),
    )
#
