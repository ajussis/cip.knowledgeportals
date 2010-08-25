from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from cip.spcontent4 import spcontent4MessageFactory as _


class IGalleryFolder(Interface):
    """Folder to hold images and show them in gallery view"""

    # -*- schema definition goes here -*-
    area = schema.TextLine(
        title=_(u"Gallery Area"),
        required=True,
        description=_(u"Field description"),
    )
#
