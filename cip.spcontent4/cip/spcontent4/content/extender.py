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
            widget = LinesWidget(
                label="Creators (one per line)")),
        MyStringField("pubsubject",
            widget = StringWidget(
                label="Subject")),
        MyStringField("pubpublisher",
            widget = StringWidget(
                label="Publisher name")),
        MyLinesField("pubcontributors",
            widget = LinesWidget(
                label="Contributors (one per line)")),
        MyDateTimeField("pubdate",
            widget = CalendarWidget(
                label="Publication date")),
        MyStringField("pubtype",
            widget = StringWidget(
                label="Type")),
        MyStringField("pubformat",
            widget = StringWidget(
                label="Format")),
        MyStringField("pubidentifier",
            widget = StringWidget(
                label="Identifier")),
        MyStringField("pubsource",
            widget = StringWidget(
                label="Source")),
        MyStringField("publanguage",
            widget = StringWidget(
                label="Language")),
        MyStringField("pubrelation",
            widget = StringWidget(
                label="Relation")),
        MyStringField("pubcoverage",
            widget = StringWidget(
                label="Coverage")),
        MyStringField("pubrights",
            widget = StringWidget(
                label="Rights")),
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
            widget = LinesWidget(
                label="Creators (one per line)")),
        MyStringField("pubsubject",
            widget = StringWidget(
                label="Subject")),
        MyStringField("pubpublisher",
            widget = StringWidget(
                label="Publisher name")),
        MyLinesField("pubcontributors",
            widget = LinesWidget(
                label="Contributors (one per line)")),
        MyDateTimeField("pubdate",
            widget = CalendarWidget(
                label="Publication date")),
        MyStringField("pubtype",
            widget = StringWidget(
                label="Type")),
        MyStringField("pubformat",
            widget = StringWidget(
                label="Format")),
        MyStringField("pubidentifier",
            widget = StringWidget(
                label="Identifier")),
        MyStringField("pubsource",
            widget = StringWidget(
                label="Source")),
        MyStringField("publanguage",
            widget = StringWidget(
                label="Language")),
        MyStringField("pubrelation",
            widget = StringWidget(
                label="Relation")),
        MyStringField("pubcoverage",
            widget = StringWidget(
                label="Coverage")),
        MyStringField("pubrights",
            widget = StringWidget(
                label="Rights")),
        ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
