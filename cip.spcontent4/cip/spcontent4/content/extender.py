from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import ISchemaExtender
from Products.Archetypes.public import StringWidget
from Products.Archetypes.public import LinesWidget
from Products.Archetypes.public import CalendarWidget
from Products.ATContentTypes.interface import IATFile, IATLink

from Products.Archetypes.public import BooleanField
from Products.Archetypes.public import StringField
from Products.Archetypes.public import LinesField
from Products.Archetypes.public import DateTimeField
from archetypes.schemaextender.field import ExtensionField

class MyStringField(ExtensionField, StringField):
    """A trivial field."""

class MyLinesField(ExtensionField, LinesField):
    """A trivial field."""

class MyDateTimeField(ExtensionField, DateTimeField):
    """A trivial field."""

class LinkExtender(object):
    adapts(IATLink)
    implements(ISchemaExtender)

    fields = [
        MyLinesField("pubcreators",
            widget = LinesWidget(label="Creators (one per line)",
                                 description="An entity primarily responsible for making the content of the resource. Examples of a Creator include a person, an organization, or a service. Typically the name of the Creator should be used to indicate the entity."),),
        MyStringField("pubsubject",
            widget = StringWidget(
                label="Subject",
                description="The topic of the content of the resource. Typically, a Subject will be expressed as keywords or key phrases or classification codes that describe the topic of the resource. Recommended best practice is to select a value from a controlled vocabulary or formal classification scheme.")),
        MyStringField("pubpublisher",
            widget = StringWidget(
                label="Publisher",
                description="The entity responsible for making the resource available. Examples of a Publisher include a person, an organization, or a service. Typically, the name of a Publisher should be used to indicate the entity.")),
        MyLinesField("pubcontributors",
            widget = LinesWidget(
                label="Contributors (one per line)",
                description="An entity responsible for making contributions to the content of the resource. Examples of a Contributor include a person, an organization or a service. Typically, the name of a Contributor should be used to indicate the entity.")),
        MyDateTimeField("pubdate",
            widget = CalendarWidget(
                label="Publication date",
                description="A date associated with an event in the life cycle of the resource. Typically, Date will be associated with the creation or availability of the resource. ")),
        MyStringField("pubtype",
            widget = StringWidget(
                label="Type",
                description="The nature or genre of the content of the resource. Type includes terms describing general categories, functions, genres, or aggregation levels for content. Recommended best practice is to select a value from a controlled vocabulary (for example, the DCMIType vocabulary ).")),
        MyStringField("pubformat",
            widget = StringWidget(
                label="Format",
                description="The physical or digital manifestation of the resource. Typically, Format may include the media-type or dimensions of the resource. Examples of dimensions include size and duration. Format may be used to determine the software, hardware or other equipment needed to display or operate the resource.")),
        MyStringField("pubidentifier",
            widget = StringWidget(
                label="Identifier",
                description="An unambiguous reference to the resource within a given context. Recommended best practice is to identify the resource by means of a string or number conforming to a formal identification system. Examples of formal identification systems include the Uniform Resource Identifier (URI) (including the Uniform Resource Locator (URL), the Digital Object Identifier (DOI) and the International Standard Book Number (ISBN).")),
        MyStringField("pubsource",
            widget = StringWidget(
                label="Source",
                description="A Reference to a resource from which the present resource is derived. The present resource may be derived from the Source resource in whole or part. Recommended best practice is to reference the resource by means of a string or number conforming to a formal identification system")),
        MyStringField("publanguage",
            widget = StringWidget(
                label="Language",
                description="A language of the intellectual content of the resource. Recommended best practice for the values of the Language element is defined by RFC 3066 [RFC 3066, http://www.ietf.org/rfc/ rfc3066.txt] which, in conjunction with ISO 639 [ISO 639, http://www.oasis- open.org/cover/iso639a.html]), defines two- and three-letter primary language tags with optional subtags. Examples include en or eng for English, akk for Akkadian, and en-GB for English used in the United Kingdom.")),
        MyStringField("pubrelation",
            widget = StringWidget(
                label="Relation",
                description="A reference to a related resource. Recommended best practice is to reference the resource by means of a string or number conforming to a formal identification system.")),
        MyStringField("pubcoverage",
            widget = StringWidget(
                label="Coverage",
                description="The extent or scope of the content of the resource. Coverage will typically include spatial location (a place name or geographic co-ordinates), temporal period (a period label, date, or date range) or jurisdiction (such as a named administrative entity). Recommended best practice is to select a value from a controlled vocabulary (for example, the Thesaurus of Geographic Names [Getty Thesaurus of Geographic Names, http://www. getty.edu/research/tools/vocabulary/tgn/]). Where appropriate, named places or time periods should be used in preference to numeric identifiers such as sets of co-ordinates or date ranges.")),
        MyStringField("pubrights",
            widget = StringWidget(
                label="Rights",
                description="Information about rights held in and over the resource. Typically a Rights element will contain a rights management statement for the resource, or reference a service providing such information. Rights information often encompasses Intellectual Property Rights (IPR), Copyright, and various Property Rights. If the rights element is absent, no assumptions can be made about the status of these and other rights with respect to the resource.")),
        ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
    

class FileExtender(object):
    adapts(IATFile)
    implements(ISchemaExtender)

    fields = [
        MyLinesField("pubcreators",
            widget = LinesWidget(label="Creators (one per line)",
                                 description="An entity primarily responsible for making the content of the resource. Examples of a Creator include a person, an organization, or a service. Typically the name of the Creator should be used to indicate the entity."),),
        MyStringField("pubsubject",
            widget = StringWidget(
                label="Subject",
                description="The topic of the content of the resource. Typically, a Subject will be expressed as keywords or key phrases or classification codes that describe the topic of the resource. Recommended best practice is to select a value from a controlled vocabulary or formal classification scheme.")),
        MyStringField("pubpublisher",
            widget = StringWidget(
                label="Publisher",
                description="The entity responsible for making the resource available. Examples of a Publisher include a person, an organization, or a service. Typically, the name of a Publisher should be used to indicate the entity.")),
        MyLinesField("pubcontributors",
            widget = LinesWidget(
                label="Contributors (one per line)",
                description="An entity responsible for making contributions to the content of the resource. Examples of a Contributor include a person, an organization or a service. Typically, the name of a Contributor should be used to indicate the entity.")),
        MyDateTimeField("pubdate",
            widget = CalendarWidget(
                label="Publication date",
                description="A date associated with an event in the life cycle of the resource. Typically, Date will be associated with the creation or availability of the resource. ")),
        MyStringField("pubtype",
            widget = StringWidget(
                label="Type",
                description="The nature or genre of the content of the resource. Type includes terms describing general categories, functions, genres, or aggregation levels for content. Recommended best practice is to select a value from a controlled vocabulary (for example, the DCMIType vocabulary ).")),
        MyStringField("pubformat",
            widget = StringWidget(
                label="Format",
                description="The physical or digital manifestation of the resource. Typically, Format may include the media-type or dimensions of the resource. Examples of dimensions include size and duration. Format may be used to determine the software, hardware or other equipment needed to display or operate the resource.")),
        MyStringField("pubidentifier",
            widget = StringWidget(
                label="Identifier",
                description="An unambiguous reference to the resource within a given context. Recommended best practice is to identify the resource by means of a string or number conforming to a formal identification system. Examples of formal identification systems include the Uniform Resource Identifier (URI) (including the Uniform Resource Locator (URL), the Digital Object Identifier (DOI) and the International Standard Book Number (ISBN).")),
        MyStringField("pubsource",
            widget = StringWidget(
                label="Source",
                description="A Reference to a resource from which the present resource is derived. The present resource may be derived from the Source resource in whole or part. Recommended best practice is to reference the resource by means of a string or number conforming to a formal identification system")),
        MyStringField("publanguage",
            widget = StringWidget(
                label="Language",
                description="A language of the intellectual content of the resource. Recommended best practice for the values of the Language element is defined by RFC 3066 [RFC 3066, http://www.ietf.org/rfc/ rfc3066.txt] which, in conjunction with ISO 639 [ISO 639, http://www.oasis- open.org/cover/iso639a.html]), defines two- and three-letter primary language tags with optional subtags. Examples include en or eng for English, akk for Akkadian, and en-GB for English used in the United Kingdom.")),
        MyStringField("pubrelation",
            widget = StringWidget(
                label="Relation",
                description="A reference to a related resource. Recommended best practice is to reference the resource by means of a string or number conforming to a formal identification system.")),
        MyStringField("pubcoverage",
            widget = StringWidget(
                label="Coverage",
                description="The extent or scope of the content of the resource. Coverage will typically include spatial location (a place name or geographic co-ordinates), temporal period (a period label, date, or date range) or jurisdiction (such as a named administrative entity). Recommended best practice is to select a value from a controlled vocabulary (for example, the Thesaurus of Geographic Names [Getty Thesaurus of Geographic Names, http://www. getty.edu/research/tools/vocabulary/tgn/]). Where appropriate, named places or time periods should be used in preference to numeric identifiers such as sets of co-ordinates or date ranges.")),
        MyStringField("pubrights",
            widget = StringWidget(
                label="Rights",
                description="Information about rights held in and over the resource. Typically a Rights element will contain a rights management statement for the resource, or reference a service providing such information. Rights information often encompasses Intellectual Property Rights (IPR), Copyright, and various Property Rights. If the rights element is absent, no assumptions can be made about the status of these and other rights with respect to the resource.")),
        ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
