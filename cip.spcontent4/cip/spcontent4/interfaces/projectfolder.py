from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.spcontent4 import spcontent4MessageFactory as _


class IProjectFolder(Interface):
    """The container for Sweetpotato Projects"""

    # -*- schema definition goes here -*-
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
