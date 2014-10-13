"""Definition of the Directory content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from experts.product import productMessageFactory as _

from experts.product.interfaces import IDirectory
from experts.product.config import PROJECTNAME

DirectorySchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
	# personal data label
    atapi.StringField(
		'personal',
		storage=atapi.AnnotationStorage(),
		widget=atapi.LabelWidget(
			label=_(u"Personal data"),
		),
	),

    atapi.StringField(	
        'surname',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Surname"),
            description=_(u""),
        ),
    ),

    # title multiselect
	atapi.LinesField(
		'title_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.MultiSelectionWidget(
			label = _(u"Title"),
			format='checkbox',
		),
		multivalued=1,
		vocabulary = ['Prof.','Dr.','Mr.','Mrs.','Ms.'],
	),

    atapi.StringField(
        'fname',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"First name"),
            description=_(u""),
        ),
    ),

    atapi.StringField(
        'mname',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Middle names"),
            description=_(u""),
        ),
    ),

    # sex radios
    atapi.LinesField(
		'sex',
		storage=atapi.AnnotationStorage(),
		widget=atapi.SelectionWidget(
			label = _(u"Sex"),
			format='radio',
		),
		multivalued=1,
		vocabulary = ['Male','Female'],
	),
 
    atapi.StringField(
        'position',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Position"),
            description=_(u""),
        ),
    ),

    atapi.StringField(
        'nationality',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Nationality"),
            description=_(u""),
        ),
    ),

    # languages multiselect	
    atapi.LinesField(
		'languages',
		storage=atapi.AnnotationStorage(),
		widget=atapi.MultiSelectionWidget(
			label = _(u"Working Languages"),
			format='checkbox',
		),
		multivalued=1,
		vocabulary = ['English','French','Portuguese','Spanish','Swahili'],
	),

    atapi.LinesField(
		'keywords',
		storage=atapi.AnnotationStorage(),
		widget=atapi.LinesWidget(
			label=_(u"Keywords that best describe your professional background and skills"),
		),
	),

    atapi.StringField(
		'location',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Location"),
		),
	),

	atapi.StringField(
		'pobox',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"P.O Box"),
		),
	),

    atapi.StringField(
		'postcode',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Post Code"),
		),
	),

    atapi.StringField(
		'city',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"City/Town"),
		),
	),

    atapi.StringField(
		'country',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Country"),
		),
	),

    atapi.StringField(
		'general',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Telephone(General)"),
		),
	),

    atapi.StringField(
		'direct',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Telephone(Direct)"),
		),
	),
	
    atapi.StringField(
		'cellular',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Cellular"),
		),
	),

    atapi.StringField(
		'fax',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Fax"),
		),
	),

	atapi.StringField(
		'email',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Email"),
		),
	),

    atapi.StringField(
		'website',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Website"),
		),
	),

	atapi.StringField(
		'blog',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Blog"),
		),
	),

	# Your education and qualifications label
    atapi.StringField(
		'edulabel',
		storage=atapi.AnnotationStorage(),
		widget=atapi.LabelWidget(
			label=_(u"Your education and qualifications"),
		),
	),

    atapi.LinesField(
		'education',
		storage=atapi.AnnotationStorage(),
		widget=atapi.LinesWidget(
			label=_(u"Qualification / Field of specialization / Year / University or College"),
		),
	),

	# your specific specialization and areas of competence label

    atapi.StringField(
		'special',
		storage=atapi.AnnotationStorage(),
		widget=atapi.LabelWidget(
			label=_(u"Your specific specialization and areas of competence"),
			description=_(u"You may select more than one"),
		),
	),

    atapi.LinesField(
		'working',
		storage=atapi.AnnotationStorage(),
		widget=atapi.MultiSelectionWidget(
			label=_(u"Specific specialization and working experience"),
			format='checkbox',
			description=_(u"You may select more than one"),
		),
		multivalued=1,
		vocabulary = ['Breeding','Seed Systems','Agronomy','Pests and diseases','Nutrition','Economics','Postharvest','Agribusiness','Product development','Food science and technology','Marketing','Policy','Monitoring and evaluation','Project management','Information, communication and knowledge management','Legal issues','Training and education'],
	),

    # specific specialization and training experience
    atapi.StringField(
		'special_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.LabelWidget(
			label=_(u"Your training experience(s)"),
			description=_(u"Please indicate areas in which you have been involved in sweetpotato training - you may select more than one"),
		),
	),

    atapi.LinesField(
		'training',
		storage=atapi.AnnotationStorage(),
		widget=atapi.MultiSelectionWidget(
			label=_(u"Specific specialization and training experience"),
			format='checkbox',
			description=_(u"Please specify the training courses you have conducted/facilitated"),
		),
		multivalued=1,
		vocabulary = ['Adult learning','Origin and importance of sweetpotato','Varietal selection and characteristics','Nutrition','Seed systems','Production and management','Pest and disease management','Harvesting and postharvest management','Marketing, entrepreneurship and value addition','Processing and utilisation','Gender and diversity','Monitoring and Evaluation','Dissemination and uptake'],
	),

	# your organization label

    atapi.StringField(
		'orglabel',
		storage=atapi.AnnotationStorage(),
		widget=atapi.LabelWidget(
			label=_(u"Your organization"),
		),
	),

    atapi.StringField(
		'name',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Name"),
		),
	),

    atapi.StringField(
		'acronym',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Acronym"),
		),
	),

    atapi.StringField(
		'address',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Address"),
		),
	),

	atapi.StringField(
		'location_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Location"),
		),
	),

    atapi.StringField(
		'pobox_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"P.O Box"),
		),
	),

    atapi.StringField(
		'postcode_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Post code"),
		),
	),

    atapi.StringField(
		'city_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"City/Town"),
		),
	),

    atapi.StringField(
		'country_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Country"),
		),
	),

    atapi.StringField(
		'general_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Telephone(General)"),
		),
	),

    atapi.StringField(
		'direct_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Telephone(Direct)"),
		),
	),

    atapi.StringField(
		'cellular_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Cellular"),
		),
	),

    atapi.StringField(
		'fax_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Fax"),
		),
	),

    atapi.StringField(
		'email_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Email"),
		),
	),

    atapi.StringField(
		'website_',
		storage=atapi.AnnotationStorage(),
		widget=atapi.StringWidget(
			label=_(u"Website"),
		),
	),

    atapi.LinesField(
		'organization',
		storage=atapi.AnnotationStorage(),
		widget=atapi.MultiSelectionWidget(
			label=_(u"Type of organization"),
			format='checkbox',
			description=_(u"Tick as applies"),
		),
		multivalued=1,
		vocabulary=['Government department','Parastatal or agency','Regional / Sub-regional organization','International organization','Training / Education institution','Research Institution','Extension','Development / Donor organization','Association','Non-governmental organization','Community based organization','Private company','Consultancy'],
	),

    # level of operation and main function label
    atapi.StringField(
		'geoglabel',
		storage=atapi.AnnotationStorage(),
		widget=atapi.LabelWidget(
			label=_(u"Your geographic level of operation and main functions"),
			description=_(u"You may select more than one"),
		),
	),

    atapi.LinesField(
		'operation',
		storage=atapi.AnnotationStorage(),
		widget=atapi.MultiSelectionWidget(
			label=_(u"Level of operation"),
			format='checkbox',
			description=_(u"Tick as applies"),
		),
		multivalued=1,
		vocabulary=['International','Pan African','Regional/Sub-regional','National'],
	),

    atapi.LinesField(
		'functions',
		storage=atapi.AnnotationStorage(),
		widget=atapi.MultiSelectionWidget(
			label=_(u"Main functions"),
			format='checkbox',
			description=_(u"Tick as applies"),
		),
		multivalued=1,
		vocabulary=['Research','Education and training','Advocacy','Extension','Planning and policy development','Development work','Technical assistance','Information, communication and knowledge management services'],
	),

	# relevant publications label
    atapi.LinesField(
		'publications',
		storage=atapi.AnnotationStorage(),
		widget=atapi.LinesWidget(
			label=_(u"Relevant publications"),
			description=_(u"Maximum of 5 starting with MOST RECENT"),
		),
	),
	
	
	
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

DirectorySchema['title'].storage = atapi.AnnotationStorage()
DirectorySchema['description'].storage = atapi.AnnotationStorage()

DirectorySchema['description'].widget.visible['view'] = 'invisible'
DirectorySchema['description'].widget.visible['edit'] = 'invisible'

DirectorySchema['title'].widget.label = 'Full name'

schemata.finalizeATCTSchema(DirectorySchema, moveDiscussion=False)


class Directory(base.ATCTContent):
    """Experts directory content type"""
    implements(IDirectory)

    meta_type = "Directory"
    schema = DirectorySchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    personal = atapi.ATFieldProperty('personal')
	
    surname = atapi.ATFieldProperty('surname')
	
    title_ = atapi.ATFieldProperty('title_')

    fname = atapi.ATFieldProperty('fname')

    mname = atapi.ATFieldProperty('mname')

    sex = atapi.ATFieldProperty('sex')
	
    position = atapi.ATFieldProperty('position')

    nationality = atapi.ATFieldProperty('nationality')

    languages = atapi.ATFieldProperty('languages')

    keywords = atapi.ATFieldProperty('keywords')

    location = atapi.ATFieldProperty('location')

    pobox = atapi.ATFieldProperty('pobox')

    postcode = atapi.ATFieldProperty('postcode')

    city = atapi.ATFieldProperty('city')

    country = atapi.ATFieldProperty('country')

    general = atapi.ATFieldProperty('general')

    direct = atapi.ATFieldProperty('direct')

    cellular = atapi.ATFieldProperty('cellular')

    fax = atapi.ATFieldProperty('fax')

    email = atapi.ATFieldProperty('email')

    website = atapi.ATFieldProperty('website')

    blog = atapi.ATFieldProperty('blog')

    edulabel = atapi.ATFieldProperty('edulabel')

    education = atapi.ATFieldProperty('education')

    special = atapi.ATFieldProperty('special')

    working = atapi.ATFieldProperty('working')

    special_ = atapi.ATFieldProperty('special_')

    training = atapi.ATFieldProperty('training')

    orglabel = atapi.ATFieldProperty('orglabel')

    name = atapi.ATFieldProperty('name')

    acronym = atapi.ATFieldProperty('acronym')

    address = atapi.ATFieldProperty('address')

    location_ = atapi.ATFieldProperty('location_')

    pobox_ = atapi.ATFieldProperty('pobox_')

    postcode_ = atapi.ATFieldProperty('postcode_')

    city_ = atapi.ATFieldProperty('city_')

    country_ = atapi.ATFieldProperty('country_')

    general_ = atapi.ATFieldProperty('general_')

    direct_ = atapi.ATFieldProperty('direct_')

    cellular_ = atapi.ATFieldProperty('cellular_')

    fax_ = atapi.ATFieldProperty('fax_')

    email_ = atapi.ATFieldProperty('email_')

    website_ = atapi.ATFieldProperty('website_')

    organization = atapi.ATFieldProperty('organization')

    geoglabel = atapi.ATFieldProperty('geoglabel')

    operation = atapi.ATFieldProperty('opertation')

    functions = atapi.ATFieldProperty('functions')

    publications = atapi.ATFieldProperty('publications')
   
DirectorySchema.moveField("personal", before="title")
DirectorySchema.moveField("title_",after="personal")
atapi.registerType(Directory, PROJECTNAME)
