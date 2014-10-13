from zope.interface import Interface
# -*- Additional Imports Here -*-

from zope import schema

from experts.product import productMessageFactory as _

class IDirectory(Interface):
    """Experts directory content type"""

    # -*- schema definition goes here -*-


    surname = schema.TextLine(
		title=_(u"Country"),
		required=False,
		description=_(u""),
	)

	
    title = schema.List(
		title=_(u"Title"),
		required=False,
		description=_(u""),
	)

	
    fname = schema.TextLine(
		title=_(u"First name"),
		required=False,
		description=_(u""),
	)

	
    mname = schema.TextLine(
		title=_(u"Middle names"),
		required=False,
		description=_(u""),
	)

    sex = schema.List(
		title=_(u"Sex"),
		required=False,
		description=_(u""),
	)

	
    position = schema.TextLine(
		title=_(u"Position"),
		required=False,
		description=_(u""),
	)

	
    nationality = schema.TextLine(
		title=_(u"Nationality"),
		required=False,
		description=_(u""),
	)
