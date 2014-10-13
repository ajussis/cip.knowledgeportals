from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from experts.product import productMessageFactory as _



class ICIPPortfolio(Interface):
    """CIP Investment Portfolio"""

    # -*- schema definition goes here -*-
    country = schema.TextLine(
        title=_(u"Country"),
        required=False,
        description=_(u"Field description"),
    )
#
    region_ = schema.TextLine(
        title=_(u"Region"),
        required=False,
        description=_(u"Field description"),
    )
#
    project = schema.TextLine(
        title=_(u"Project/Programme Name"),
        required=False,
        description=_(u"Field description"),
    )
#
    donor = schema.TextLine(
        title=_(u"Donor"),
        required=False,
        description=_(u"Field description"),
    )
#
    donorcode = schema.TextLine(
        title=_(u"Donor Code"),
        required=False,
        description=_(u"Field description"),
    )
#
    region = schema.TextLine(
        title=_(u"Region/State/Zone/Province"),
        required=False,
        description=_(u"Field description"),
    )
#
    locality = schema.TextLine(
        title=_(u"Locality"),
        required=False,
        description=_(u"Field description"),
    )
#
    seed = schema.TextLine(
        title=_(u"Sweetpotato Seed Systems"),
        required=False,
        description=_(u"Field description"),
    )
#
    production = schema.TextLine(
        title=_(u"Sweetpotato Production"),
        required=False,
        description=_(u"Field description"),
    )
#
    nutrition = schema.TextLine(
        title=_(u"Sweetpotato Nutrition"),
        required=False,
        description=_(u"Field description"),
    )
#
    postharvest = schema.TextLine(
        title=_(u"Sweetpotato Post Harvest"),
        required=False,
        description=_(u"Field description"),
    )
#
    trade = schema.TextLine(
        title=_(u"Sweetpotato Trade and Marketing"),
        required=False,
        description=_(u"Field description"),
    )
#
    advocacy = schema.TextLine(
        title=_(u"Sweetpotato Advocacy and Capacity Building"),
        required=False,
        description=_(u"Field description"),
    )
#
    ickm = schema.TextLine(
        title=_(u"Sweetpotato ICKM"),
        required=False,
        description=_(u"Field description"),
    )
#
    period = schema.TextLine(
        title=_(u"Period"),
        required=False,
        description=_(u"Field description"),
    )
#
    status = schema.TextLine(
        title=_(u"Status"),
        required=False,
        description=_(u"Field description"),
    )
#
    amount = schema.TextLine(
        title=_(u"Amount"),
        required=False,
        description=_(u"Field description"),
    )
#
    country = schema.TextLine(
        title=_(u"Country"),
        required=False,
        description=_(u"Field description"),
    )
#
    region = schema.TextLine(
        title=_(u"Region"),
        required=False,
        description=_(u"Field description"),
    )
#
    project = schema.TextLine(
        title=_(u"Project/Programme"),
        required=False,
        description=_(u"Field description"),
    )
#
    donorcode = schema.TextLine(
        title=_(u"Donor Code"),
        required=False,
        description=_(u"Field description"),
    )
#
    region = schema.TextLine(
        title=_(u"Region/State/Zone/Province"),
        required=False,
        description=_(u"Field description"),
    )
#
    locality = schema.TextLine(
        title=_(u"Locality"),
        required=False,
        description=_(u"Field description"),
    )
#
    seed = schema.TextLine(
        title=_(u"Sweetpotato Seed Systems"),
        required=False,
        description=_(u"Field description"),
    )
#
    production = schema.TextLine(
        title=_(u"Sweetpotato Production"),
        required=False,
        description=_(u"Field description"),
    )
#
    nutrition = schema.TextLine(
        title=_(u"Sweetpotato Nutrition"),
        required=False,
        description=_(u"Field description"),
    )
#
    harvest = schema.TextLine(
        title=_(u"Sweetpotato Post Harvest"),
        required=False,
        description=_(u"Field description"),
    )
#
    trade = schema.TextLine(
        title=_(u"Sweetpotato Trade and Marketing"),
        required=False,
        description=_(u"Field description"),
    )
#
    advocacy = schema.TextLine(
        title=_(u"Sweetpotato Advocacy and Capacity Building"),
        required=False,
        description=_(u"Field description"),
    )
#
    ickm = schema.TextLine(
        title=_(u"Sweetpotato ICKM"),
        required=False,
        description=_(u"Field description"),
    )
#
    period = schema.TextLine(
        title=_(u"Period"),
        required=False,
        description=_(u"Field description"),
    )
#
    status = schema.TextLine(
        title=_(u"Status"),
        required=False,
        description=_(u"Field description"),
    )
#
    amount = schema.TextLine(
        title=_(u"Amount US$"),
        required=False,
        description=_(u"Field description"),
    )
#
