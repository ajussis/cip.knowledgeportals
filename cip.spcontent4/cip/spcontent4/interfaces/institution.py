from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.spcontent4 import spcontent4MessageFactory as _


class IInstitution(Interface):
    """Institution Content Type"""

    # -*- schema definition goes here -*-
    info = schema.TextLine(
        title=_(u"New Field"),
        required=False,
        description=_(u"Field description"),
    )
#
    headquarters = schema.TextLine(
        title=_(u"Headquarters"),
        required=False,
        description=_(u"Address, City, Country"),
    )
#
    website = schema.TextLine(
        title=_(u"Website"),
        required=False,
        description=_(u"Website of the Institution"),
    )
#
    area = schema.Object(
        title=_(u"Geographical Area"),
        required=False,
        description=_(u"On which parts of the world the institution operates"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
    headquarters = schema.TextLine(
        title=_(u"Headquarters address"),
        required=False,
        description=_(u"Address, City, Country"),
    )
#
