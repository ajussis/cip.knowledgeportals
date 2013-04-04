from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.spcontent4 import spcontent4MessageFactory as _



class IProjectType(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    test = schema.TextLine(
        title=_(u"New Field"),
        required=False,
        description=_(u"Field description"),
    )
#
