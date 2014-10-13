from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from experts.product import productMessageFactory as _



class IExpertsEvent(Interface):
    """Sweetpotato experts event"""

    # -*- schema definition goes here -*-
    venue = schema.TextLine(
        title=_(u"Location"),
        required=False,
        description=_(u"Town and country"),
    )
#
    location = schema.TextLine(
        title=_(u"Location"),
        required=False,
        description=_(u"Town and country"),
    )
#
    startdate = schema.Date(
        title=_(u"Start Date"),
        required=False,
        description=_(u"Field description"),
    )
#
    enddate = schema.Date(
        title=_(u"End Date"),
        required=False,
        description=_(u"Field description"),
    )
#
    eventtype = schema.TextLine(
        title=_(u"Event Type"),
        required=False,
        description=_(u"Workshop/Conference/Training/Meeting"),
    )
#
    project = schema.TextLine(
        title=_(u"Project / Programme"),
        required=False,
        description=_(u"Field description"),
    )
#
    partners = schema.Text(
        title=_(u"Partners"),
        required=False,
        description=_(u"Field description"),
    )
#
    location = schema.TextLine(
        title=_(u"Location"),
        required=False,
        description=_(u"Town and Country"),
    )
#
    organizers = schema.Text(
        title=_(u"Organizer(s)"),
        required=False,
        description=_(u"Field description"),
    )
#
    contact = schema.Text(
        title=_(u"Contact"),
        required=False,
        description=_(u"Field description"),
    )
#
    url = schema.TextLine(
        title=_(u"URL"),
        required=False,
        description=_(u"Field description"),
    )
#
