from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.spcontent4 import spcontent4MessageFactory as _


class IProjectFolder(Interface):
    """The container for Sweetpotato Projects"""

    # -*- schema definition goes here -*-
    image = schema.Bytes(
        title=_(u"Project Image"),
        required=False,
        description=_(u"Insert the project's logo or a representative image"),
    )
#
    leaderText = schema.TextLine(
        title=_(u"Leader (not a member of portal)"),
        required=False,
        description=_(u"Fill this field only if the project leader is not a member in this portal"),
    )
#
    info = schema.Text(
        title=_(u"More information"),
        required=False,
        description=_(u"More information about the project"),
    )
#
    leader = schema.TextLine(
        title=_(u"Project Leader"),
        required=False,
        description=_(u"The name of the project leader"),
    )
#
    financing = schema.Text(
        title=_(u"Financing"),
        required=True,
        description=_(u"The financing sources of the project"),
    )
#
    end = schema.Date(
        title=_(u"End date"),
        required=False,
        description=_(u"When will the project end"),
    )

    start = schema.Date(
        title=_(u"Start"),
        required=True,
        description=_(u"The startdate of the project"),
    )

    area = schema.Object(
        title=_(u"Geographical Area"),
        required=True,
        description=_(u"Geographical area of the project"),
        schema=Interface, # specify the interface(s) of the addable types here
    )
#
