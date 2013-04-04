from zope.interface import Interface, implements
from zope import schema

from cip.sppolicy4 import _
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema

def validateAccept(value):
    if not value == True:
        return False
    return True

class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema

class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    firstname = schema.TextLine(
        title=_(u'label_firstname', default=u'First name'),
        description=_(u'help_firstname',
                      default=u"Fill in your given name."),
        required=True,
        )
    lastname = schema.TextLine(
        title=_(u'label_lastname', default=u'Last name'),
        description=_(u'help_lastname',
                      default=u"Fill in your surname or your family name."),
        required=True,
        )
    gender = schema.Choice(
        title=_(u'label_gender', default=u'Gender'),
        description=_(u'help_gender',
                      default=u"Male / Female?"),
        values = ['Male', 'Female'],
        required=True,
        )
#    birthdate = schema.Date(
#        title=_(u'label_birthdate', default=u'birthdate'),
#        description=_(u'help_birthdate',
#            default=u'Your date of birth, in the format dd-mm-yyyy'),
#        required=False,
#        )
    mobile = schema.TextLine(
        title=_(u'label_mobile', default=u'Mobile'),
        description=_(u'help_mobile',
                      default=u"Fill in your mobile number starting with + and country code."),
        required=False,
        )
    officen = schema.TextLine(
        title=_(u'label_officen', default=u'Office number'),
        description=_(u'help_officen',
                      default=u"Fill in your office number starting with + and country code."),
        required=False,
        )
    skype = schema.TextLine(
        title=_(u'label_skype', default=u'Skype account'),
        description=_(u'help_skype',
                      default=u"Fill in your skype account."),
        required=False,
        )
    country = schema.TextLine(
        title=_(u'label_country', default=u'Country'),
        description=_(u'help_country',
                      default=u"Fill in the country you live in."),
        required=False,
        )
    city = schema.TextLine(
        title=_(u'label_city', default=u'City'),
        description=_(u'help_city',
                      default=u"Fill in the city you live in."),
        required=False,
        )
    institution = schema.TextLine(
        title=_(u'label_institution', default=u'Institution / Organization'),
        description=_(u'help_institution',
                      default=u"Fill in the institution where you work."),
        required=False,
        )
    instadd = schema.TextLine(
        title=_(u'label_instadd', default=u'Institution address'),
        description=_(u'help_instadd',
                      default=u"Fill in the address of the institution where you work."),
        required=False,
        )
    position = schema.TextLine(
        title=_(u'label_position', default=u'Current position'),
        description=_(u'help_instadd',
                      default=u"Fill in the current position."),
        required=False,
        )
    profession = schema.TextLine(
        title=_(u'label_profession', default=u'Profession'),
        description=_(u'help_profession',
                      default=u"Fill in your profession."),
        required=False,
        )
#    newsletter = schema.Bool(
#        title=_(u'label_newsletter', default=u'Subscribe to newsletter'),
#        description=_(u'help_newsletter',
#                      default=u"If you tick this box, we'll subscribe you to "
#                        "our newsletter."),
#        required=False,
#        )
#    accept = schema.Bool(
#        title=_(u'label_accept', default=u'Accept terms of use'),
#        description=_(u'help_accept',
#                      default=u"Tick this box to indicate that you have found,"
#                      " read and accepted the terms of use for this site. "),
#        required=True,
#        constraint=validateAccept,
#        )

    def getInst(self):
        buffer=""
        s = ['sdf','sdf']
        # Returns list of site usernames
#        users=self.acl_users.getUserNames()
        # alternative: get user objects#

        return s
