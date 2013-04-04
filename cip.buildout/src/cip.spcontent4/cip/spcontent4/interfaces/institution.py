from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.spcontent4 import spcontent4MessageFactory as _


class IInstitution(Interface):
    """Institution Content Type"""

    # -*- schema definition goes here -*-
    image = schema.Bytes(
        title=_(u"Institution Logo"),
        required=False,
        description=_(u"Logo or representative image of the institution"),
    )
#
    email = schema.TextLine(
        title=_(u"Email"),
        required=False,
        description=_(u"Contact email address of the institution"),
    )
#
    number = schema.TextLine(
        title=_(u"Telephone"),
        required=False,
        description=_(u"Institution contact telephone number"),
    )
#
    city = schema.TextLine(
        title=_(u"City"),
        required=False,
        description=_(u"City of the headquarters"),
    )
#
    country = schema.TextLine(
        title=_(u"Country"),
        required=False,
        description=_(u"Country of the headquarters"),
    )
#
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
