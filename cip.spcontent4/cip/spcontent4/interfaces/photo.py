from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.spcontent4 import spcontent4MessageFactory as _



class IPhoto(Interface):
    """Experts Photo"""

    # -*- schema definition goes here -*-
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
