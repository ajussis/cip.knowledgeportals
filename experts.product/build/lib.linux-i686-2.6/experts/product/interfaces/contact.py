from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from experts.product import productMessageFactory as _



class IContact(Interface):
    """Media and communication contact"""

    # -*- schema definition goes here -*-
    surname = schema.TextLine(
        title=_(u"Surname"),
        required=False,
        description=_(u"Field description"),
    )
#
    first = schema.TextLine(
        title=_(u"First name"),
        required=False,
        description=_(u"Field description"),
    )
#
    middle = schema.TextLine(
        title=_(u"Middle name"),
        required=False,
        description=_(u"Field description"),
    )
#
    position = schema.TextLine(
        title=_(u"Position"),
        required=False,
        description=_(u"Field description"),
    )
#
    roles = schema.Text(
        title=_(u"Role(s)"),
        required=False,
        description=_(u"Field description"),
    )
#
    category = schema.TextLine(
        title=_(u"Category"),
        required=False,
        description=_(u"Field description"),
    )
#
    keywords = schema.Text(
        title=_(u"Keywords"),
        required=False,
        description=_(u"Field description"),
    )
#
    coverage = schema.TextLine(
        title=_(u"Coverage"),
        required=False,
        description=_(u"Field description"),
    )
#
    pobox = schema.TextLine(
        title=_(u"P.O Box"),
        required=False,
        description=_(u"Field description"),
    )
#
    town = schema.TextLine(
        title=_(u"Town"),
        required=False,
        description=_(u"Field description"),
    )
#
    postcode = schema.TextLine(
        title=_(u"Post code"),
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
    telephone = schema.TextLine(
        title=_(u"Telephone - fixed"),
        required=False,
        description=_(u"Field description"),
    )
#
    cellphone = schema.TextLine(
        title=_(u"Telephone- cellular"),
        required=False,
        description=_(u"Field description"),
    )
#
    fax = schema.TextLine(
        title=_(u"Fax"),
        required=False,
        description=_(u"Field description"),
    )
#
    email = schema.TextLine(
        title=_(u"Email"),
        required=False,
        description=_(u"Field description"),
    )
#
    facebook = schema.TextLine(
        title=_(u"Facebook"),
        required=False,
        description=_(u"Field description"),
    )
#
    twitter = schema.TextLine(
        title=_(u"Twitter"),
        required=False,
        description=_(u"Field description"),
    )
#
    website = schema.TextLine(
        title=_(u"Website"),
        required=False,
        description=_(u"Field description"),
    )
#
    datest = schema.Date(
        title=_(u"Date established"),
        required=False,
        description=_(u"Field description"),
    )
#
    keyed = schema.TextLine(
        title=_(u"Keyed by"),
        required=False,
        description=_(u"Field description"),
    )
#
    notes = schema.Text(
        title=_(u"Notes"),
        required=False,
        description=_(u"Field description"),
    )
#
