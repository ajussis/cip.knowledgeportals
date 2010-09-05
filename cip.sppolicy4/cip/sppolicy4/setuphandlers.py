from cStringIO import StringIO

from zope.component import getUtility
from zope.component import getMultiAdapter
from zope.app.container.interfaces import INameChooser

from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignmentMapping, ILocalPortletAssignmentManager
from plone.portlet.collection.collection import Assignment
from plone.app.portlets.portlets import navigation

from Products.CMFPlone.utils import _createObjectByType
from Products.CMFCore.utils import getToolByName

def updateCatalog(context, clear=True):
    portal = context.getSite()
    logger = context.getLogger('cip.sppolicy updateCatalog')
    logger.info('Updating catalog (with clear=%s) so items in profiles/default/structure are indexed...' % clear )
    catalog = portal.portal_catalog
    err = catalog.refreshCatalog(clear=clear)
    if not err:
        logger.info('...done.')
    else:
        logger.warn('Could not update catalog.')

#def deletePloneFolders(p):
#    """Delete the standard Plone stuff that we don't need
#    """
#    # Delete standard Plone stuff..
#    existing = p.objectIds()
#    itemsToDelete = ['Members', 'news', 'events']
#    for item in itemsToDelete:
#        if item in existing:
#            p.manage_delObjects(item)

"""def createCompany(request, site, username, title, email, passwd=None):
 
    prepareMemberProperties(site)

    # portal_registrations manages new user creation
    regtool = getToolByName(site, 'portal_registration')

    # Default password to the username
    # ... don't do this on the production server!
    if passwd == None:
        passwd = username

    # Only lowercase allowed
    username = username.lower()

    # Username must be ASCII string
    # or Plone will choke when the user tries to log in
    username = str(username)

    def is_ascii(s):
        for c in s:
            if not ord(c) < 128:
                return False

        return True

    if not is_ascii(username):
        """ """
        IStatusMessage(request).addStatusMessage(_(u"Username must contain only characters a-z"), "error")
        return None

    # This is minimum required information set
    # to create a working member
    properties = {

        'username' : username,

        # Full name must be always as utf-8 encoded
        'fullname' : title.encode("utf-8"),
        'email' : email,
    }

    try:
        # addMember() returns MemberData object
        member = regtool.addMember(username, passwd, properties=properties)
    except ValueError, e:
        # Give user visual feedback what went wrong
        IStatusMessage(request).addStatusMessage(_(u"Could not create the user:") + unicode(e), "error")
        return None"""

def createGroups(portal):
    gr = portal.portal_groups
    group_ids = ['germplasm','seedsystem','addingvalue','cropmanagement','useconsumption']
    for testGroup in group_ids:
        if not testGroup in gr.getGroupIds():
            gr.addGroup(testGroup)

def importPAS(portal):
    users_here = ['jussi;jussi;Jussi;Savolainen;ajussis@gmail.com','john;john1;John;Smith;john@mail.com','jens;jens;Jens;Riis;jens@mail.com','charles;charles;Charles;Day;charles@mail.com','michael;michael;Michael;Johnson;michael@mail.com','barbara;barbara;Barbara;Macintosh;barbara@mail.com','adelayde;adelayde;Adelayde;Rivas;adelayde@mailcom','vanessa;vanessa;Vanessa;Lopez;vanessa@mail.com']
#    users = users_here.data.split('\n')
    users = users_here
# add members to group
#    portal_groups = portal.portal_groups
# Add user to group "companies"
#portal_groups = site.portal_groups
#portal_groups.addPrincipalToGroup(member.getUserName(), "companies")
    regtool = getToolByName(portal, 'portal_registration')
    index = 1
    imported_count = 0
    for user in users:
        tokens = user.split(';')
        if len(tokens) == 5:
            passwd, id, last, first, email = tokens
            properties = {
                'username' : id,
                'fullname' : '%s %s' % (first, last),
                'email' : email,
            }
            try:
                regtool.addMember(id, passwd, properties=properties)
                print "Successfully added %s %s (%s) with email %s" % (first, last, id, email)
                imported_count += 1
            except ValueError, e:
                print "Couldn't add %s: %s" % (id, e)
        else:
            print "Could not parse line %d because it had the following contents: '%s'" % (index, user)
        index += 1
    print "Imported %d users (from %d lines of CSV)" % (imported_count, index)

def createFolderStructure(portal):
    """Define which objects we want to create in the site.
    """
    importance_children = [
        {   'id': 'statistics',
            'title': 'Statistics',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'nutritional-facts',
            'title': 'Nutritional facts',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    sweetpotatoIntroduction_children = [
        {   'id': 'importance',
            'title': 'Importance',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': importance_children,
            },
        {   'id': 'how-to-grow-it',
            'title': 'How to grow it',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'history',
            'title': 'History',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'biology',
            'title': 'Biology',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'photos',
            'title': 'Photos',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    cipGenebank_children = [
        {   'id': 'germplasm-collection',
            'title': 'Germplasm Collection',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'germplasm-ordering',
            'title': 'Germplasm Ordering',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    pqsCollection_children = [
        {   'id': 'available-germplasm',
            'title': 'Available Germplasm',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    germplasmCollection_children = [
        {   'id': 'cip-genebank',
            'title': 'CIP Genebank',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': cipGenebank_children,
            },
        {   'id': 'pqs-collection',
            'title': 'PQS Collection',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': pqsCollection_children,
            },
        ]

    germplasmExchange_children = [
        {   'id': 'virus-cleaning-testing',
            'title': 'Virus Cleaning and Testing',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'germplasm-exchange',
            'title': 'Germplasm Exchange Protocols',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'policy-legal-issues',
            'title': 'Policy and Legal Issues',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    preBreeding_children = [
        {   'id': 'available-material',
            'title': 'Available Material',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'results-from-trials',
            'title': 'Results from Trials',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]


    availableMaterial_children = [
        {   'id': 'released-varieties',
            'title': 'Released Varieties',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    breedingObjectives_children = [
        {   'id': 'drought-resistence',
            'title': 'Drought Resistence',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'virus-resistence',
            'title': 'Virus Resistence',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'unsweet',
            'title': 'Unsweet',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'animal-feed',
            'title': 'Animal Feed',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            }
        ]

    breeding_children = [
        {   'id': 'available-material',
            'title': 'Available Material',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': availableMaterial_children,
            },
        {   'id': 'results-from-trials',
            'title': 'Results From Trials',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'breeding-objectives',
            'title': 'Breeding Objectives',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': breedingObjectives_children,
            }
        ]

    farmersVarieties_children = [
        {   'id': 'variety-preferences',
            'title': 'Variety Preferences',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'selection-practices',
            'title': 'Selection Practices',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    biotechnology_children = [
        {   'id': 'marker-assisted-selection',
            'title': 'Marker Assisted Selection',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'wevil-resistance',
            'title': 'Wevil Resistance',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    gp_children = [
        {   'id': 'test-ntoicia',
            'title': 'Native potato takes center stage at photo exhibit in Lima',
            'description': 'Fertile Legacy, a photo exhibition celebrating the power and beauty of native Andean potatoes opened on August 10th in Lima, Peru. The exhibition features a sample of the exquisite variety of potatoes available in Peru, Bolivia, and Ecuador, and presents a graphic story of the tubers journey from field to table',
            'type': 'News Item',
            'layout': 'newsitem_view',
            },
        {   'id': 'test-ntoicia2',
            'title': 'Ahipa - A nutrient rich crop for a hungry world ',
            'description': 'The International Potato Center (CIP) has launched a project to enhance the nutrient-rich yam bean in an effort to improve health, food security and the sustainability of farming systems in Central and West Africa. Ahipa is the name the Inca gave to the highly nutritious legume root produced by the American yam bean (Pachyrhizus spp.) ',
            'type': 'News Item',
            'layout': 'newsitem_view',
            },
        ]

    germplasm_children = [
        {   'id': 'news',
            'title': 'Germplasm News',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_summary_view',
            'children': gp_children,
            },
        {   'id': 'germplasm-collection',
            'title': 'Germplasm Collection',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': germplasmCollection_children,
            },
        {   'id': 'germplasm-exchange',
            'title': 'Germplasm Exchange',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': germplasmExchange_children,
            },
        {   'id': 'pre-breeding',
            'title': 'Pre-Breeding',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': preBreeding_children,
            },
        {   'id': 'breeding',
            'title': 'Breeding',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': breeding_children,
            },
        {   'id': 'farmers-varieties',
            'title': 'Farmers Varieties',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': farmersVarieties_children,
            },
        {   'id': 'biotechnology',
            'title': 'Biotechnology',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': biotechnology_children,
            },
        {   'id': 'research-methods',
            'title': 'Research Methods & Tools',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'training-communication',
            'title': 'Training & Communication Material',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    foundationSeed_children = [
        {   'id': 'in-vitro',
            'title': 'In Vitro',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'iroponics',
            'title': 'Iroponics',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'screenhouse',
            'title': 'Screenhouse',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
	    }
        ]

    fieldMultiplication_children = [
        {   'id': 'root-vine',
            'title': 'Root & Vine',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'rapid-multiplication-techniques',
            'title': 'Rapid Multiplication Techniques',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    onFarm_children = [
        {   'id': 'vine-conservation',
            'title': 'Vine Conservation',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'root-based',
            'title': 'Root Based',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]


    seedProgation_children= [
        {   'id': 'seed-biology',
            'title': 'Seed Biology',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'foundation-seed',
            'title': 'Foundation Seed',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': foundationSeed_children,
            },
        {   'id': 'field-multiplication',
            'title': 'Field Multiplication',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': fieldMultiplication_children,
            },
        {   'id': 'vine-handling',
            'title': 'Vine Handling',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'on-farm',
            'title': 'On Farm',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': onFarm_children,
            },
        ]

    onFarm2_children = [
        {   'id': 'self-supply',
            'title': 'Self-Supply',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'informal-supply',
            'title': 'Informal Supply',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    supplyDriven_children = [
        {   'id': 'truck-chuck',
            'title': 'Truck & Chuck',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': '1-2-3-system',
            'title': '1, 2, 3 System',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    demandDriven_children = [
        {   'id': 'voucher-system',
            'title': 'Voucher system',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    seedSystemOrganization_children = [
        {   'id': 'on-farm',
            'title': 'On Farm',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': onFarm2_children,
            },
        {   'id': 'supply-driven',
            'title': 'Supply Driven',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': supplyDriven_children,
            },
        {   'id': 'demand-driven',
            'title': 'Demand Driven',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': demandDriven_children,
	    },
        {   'id': 'commercial-formal',
            'title': 'Commercial Formal',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
	    },
        {   'id': 'quality-control',
            'title': 'Quality Control',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
	    },
        {   'id': 'policy-legal-frameworks',
            'title': 'Policy & Legal Frameworks',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
	    },
        {   'id': 'gender-in-seed-systems',
            'title': 'Gender In Seed Systems',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
	    },
        ]

    caseStudies_children = [
        {   'id': 'farmers-seed-acquisition',
            'title': 'Farmers Seed Acquisition',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]


    seedsystem_children = [
        {   'id': 'seed-propagation',
            'title': 'Seed Propagation',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': seedProgation_children,
            },
        {   'id': 'seed-system-organization',
            'title': 'Seed System Organization',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': seedSystemOrganization_children,
            },
        {   'id': 'case-studies',
            'title': 'Case Studies',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': caseStudies_children,
            },
        {   'id': 'research-methods-tools',
            'title': 'Research Methods & Tools',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'training-communication-material',
            'title': 'Training & Communication Material',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]


    socio_children = [
        {   'id': 'Farming-strategies',
            'title': 'Farming Strategies',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'Cultural-aspects',
            'title': 'Cultural Aspects',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'Returns-on-investment',
            'title': 'Returns on Investment',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
    ]

    harvesting_children = [
        {   'id': 'time',
            'title': 'Time',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'method',
            'title': 'Method',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
    ]
    physiology_children = [
        {   'id': 'plant-phenology',
            'title': 'Plant Phenology',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'maturity-indicators',
            'title': 'Maturity Indicators',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
    ]

    soil_children = [
        {   'id': 'nutrient-requirements',
            'title': 'Nutrient Requirements',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'oraganic-fertilizers',
            'title': 'Oraganic Fertilizers',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'inorganic-fertilizers',
            'title': 'Inorganic Fertilizers',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
    ]

    agronomy_children = [
        {   'id': 'site-selection',
            'title': 'Site Selection',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'land-preparation',
            'title': 'Land Preparation',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'seed-vines-and-vareity-selection',
            'title': 'Seed Vines & Vareity Selection',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'planting',
            'title': 'Planting',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'inter-cropping',
            'title': 'Inter-cropping',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'crop-rotation',
            'title': 'Crop Rotation',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'weed-management',
            'title': 'Weed Management',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
    ]

    deseases_children = [
        {   'id': 'viruses',
            'title': 'Viruses',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'fungal',
            'title': 'Fungal',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'bacterial',
            'title': 'Bacterial',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
    ]

    pests_children = [
        {   'id': 'inset-pests',
            'title': 'Insect Pests',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'vertebrate-pests',
            'title': 'Vertebrate Pests',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'nematodes',
            'title': 'Nematodes',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'millipedes',
            'title': 'Millipedes',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'other-pests',
            'title': 'Other Pests',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
    ]

    crop_children = [
        {   'id': 'introduction',
            'title': 'Introduction',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'pests',
            'title': 'Pests',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': pests_children,
            },
        {   'id': 'deseases',
            'title': 'Deseases',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': deseases_children,
            },
        {   'id': 'agronomy',
            'title': 'Agronomy',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': agronomy_children,
            },
        {   'id': 'soil-fertility-management',
            'title': 'Soil Fertility Management',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': soil_children,
            },
        {   'id': 'physiology',
            'title': 'Physiology',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': physiology_children,
            },
        {   'id': 'harvesting',
            'title': 'Harvesting',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': harvesting_children,
            },
        {   'id': 'socio-economic-issues',
            'title': 'Socio-Economic Issues',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': socio_children,
            },
        {   'id': 'case-studies',
            'title': 'Case Studies',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'research-methods-tools',
            'title': 'Research Methods & Tools',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'training-communication-material',
            'title': 'Training & Communication Material',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
    ]

    africa_children = [
        {   'id': 'sub-saharan-africa',
            'title': 'Sub-Saharan Africa',
            'description': '',
            'type': 'Projects Holder',
            'layout': 'projectFolder'
            },
        {   'id': 'east-africa',
            'title': 'East Africa',
            'description': '',
            'type': 'Projects Holder',
            'layout': 'projectFolder'
            },
        {   'id': 'west-africa',
            'title': 'West Africa',
            'description': '',
            'type': 'Projects Holder',
            'layout': 'projectFolder',
            },
        {   'id': 'south-africa',
            'title': 'South Africa',
            'description': '',
            'type': 'Projects Holder',
            'layout': 'projectFolder',
            },
        ]

    test_project_children = [
        {   'id': 'news',
            'title': 'First News from Sasha Project',
            'description': 'This is the first news item',
            'type': 'News Item',
            'layout': 'newsitem_view'
            },
        {   'id': 'news2',
            'title': 'Second News from Sasha Project',
            'description': 'This is the news item from',
            'type': 'News Item',
            'layout': 'newsitem_view'
            },
        {   'id': 'folderone',
            'title': 'Updates',
            'description': 'Here you can find Global Project Test documents',
            'type': 'Folder',
            'layout': 'folder_listing'
            },
        {   'id': 'internal-project',
            'title': 'Agenda',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'accounting',
            'title': 'Accounting',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'history',
            'title': 'A history of the project',
            'description': '',
            'type': 'Document',
            'layout': 'document_view',
            },
        {   'id': 'presentation',
            'title': 'Presentation of the personal',
            'description': '',
            'type': 'Document',
            'layout': 'document_view',
            },
        ]

    global_children = [
        {   'id': 'test-project',
            'title': 'Sasha Project',
            'description': '',
            'type': 'Project Folder',
            'layout': 'projectFolder',
            'children': test_project_children,
            },
        {   'id': 'test-project2',
            'title': 'A project working on global scale',
            'description': '',
            'type': 'Project Folder',
            'layout': 'projectFolder',
            },
        {   'id': 'test-project3',
            'title': 'Global Project Another test',
            'description': '',
            'type': 'Project Folder',
            'layout': 'projectFolder',
            },
        ]

    projects_children = [
        {   'id': 'global',
            'title': 'Global',
            'description': '',
            'type': 'Projects Holder',
            'layout': 'folder_listing',
            'children': global_children,
            },
        {   'id': 'africa',
            'title': 'Africa',
            'description': '',
            'type': 'Projects Holder',
            'layout': 'folder_listing',
            'children': africa_children,
            },
        {   'id': 'latin-america',
            'title': 'Latin America',
            'description': '',
            'type': 'Projects Holder',
            'layout': 'folder_listing',
            },
        {   'id': 'north-america',
            'title': 'North America',
            'description': '',
            'type': 'Projects Holder',
            'layout': 'folder_listing',
            },
        {   'id': 'asia',
            'title': 'Asia',
            'description': '',
            'type': 'Projects Holder',
            'layout': 'folder_listing',
            },
        ]

    impact_children = [
        {   'id': 'impact-on-food-security',
            'title': 'Impact on Food Security',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'nutritional-impact',
            'title': 'Nutritional Impact',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'economic-impact',
            'title': 'Economic Impact',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    consumption_children = [
        {   'id': 'consumer-assessment',
            'title': 'Consumer Assessment',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'consumption-patterns',
            'title': 'Consumption Patterns',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'impact-studies',
            'title': 'Impact Studies',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': impact_children,
            },
        ]

    nutritional_children = [
        {   'id': 'nutritional-value',
            'title': 'Nutritional Value',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'processing-and-nutrition-retension',
            'title': 'Processing and Nutrition Retension',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'food-quality',
            'title': 'Food Quality and Safety',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'recommmended-intakes',
            'title': 'Recommended Intakes',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    consumptions_children = [
        {   'id': 'food-frequency',
            'title': 'Food Frequency Question',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': '24-hour-recall',
            'title': '24 Hour Recall',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    research_children = [
        {   'id': 'consumption-studies',
            'title': 'Consumption Studies',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': consumptions_children,
            },
        ]

    training_children = [
        {   'id': 'nutritional-benefits',
            'title': 'Nutritional Benefits',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'food-preparation-training',
            'title': 'Food Preparation Training',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'recipe-booklets',
            'title': 'Recipe Booklets',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'iec-materials',
            'title': 'IEC Materials',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'photos',
            'title': 'Photos',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    silage_children = [
        {   'id': 'making-and-conservation',
            'title': 'Making and Conservation',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'nutrient-values',
            'title': 'Nutrient Values in Silage',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'additives-in-silage',
            'title': 'Additives in Silage',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    animalfeed_children = [
        {   'id': 'use-of-dual-purpose',
            'title': 'Use of Dual-purpose Varieties',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'silage',
            'title': 'Silage',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': silage_children,
            },
        {   'id': 'feeding-trials',
            'title': 'Feeding Trials',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    useconsumption_children = [
        {   'id': 'nutritional-information',
            'title': 'Nutritional Information',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': nutritional_children,
            },
        {   'id': 'consumption-studies',
            'title': 'Consumption Studies',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': consumption_children,
            },
        {   'id': 'use-as-animal-feed',
            'title': 'Use as Animal Feed',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': animalfeed_children,
            },
        {   'id': 'case-studies',
            'title': 'Case Studies',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
           },
        {   'id': 'research-methods-and-tools',
            'title': 'Research Methods and Tools',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': research_children,
            },
        {   'id': 'training-and-communication',
            'title': 'Training and Communication',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': training_children,
            },
        ]


    demandcreation_children = [
        {   'id': 'campaigns',
            'title': 'Campaigns',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'niche-markets',
            'title': 'Niche Markets',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'conventional-consumers',
            'title': 'Conventional Consumers',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    demand_children = [
        {   'id': 'consumer-peferences',
            'title': 'Consumer Preferences',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'demand-creation',
            'title': 'Demand Creation',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': demandcreation_children,
            },
        ]

    productdevelopment_children = [
        {   'id': 'flour',
            'title': 'Flour',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'chips',
            'title': 'Chips',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'biscuits',
            'title': 'Biscuits',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'bread',
            'title': 'Bread',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'cakes',
            'title': 'Cakes',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'juice',
            'title': 'Juice',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'sweetpotato-leaves',
            'title': 'Sweetpotato Leaves',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'advanced-products',
            'title': 'Advanced Products',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'packaging',
            'title': 'Packaging',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    postharvestissues_children = [
        {   'id': 'insect-pests',
            'title': 'Insect Pests',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'disease',
            'title': 'Disease',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'physiology',
            'title': 'Physiology',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    postharvest_children = [
        {   'id': 'cleaning',
            'title': 'Cleaning & Curing',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'grading',
            'title': 'Grading',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'transport',
            'title': 'Transport',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'storage',
            'title': 'Storage',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'post-harvest',
            'title': 'Post-harvest Issues',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': postharvestissues_children,
            },
        {   'id': 'packaging',
            'title': 'Packaging',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    vaintro_children = [
        {   'id': 'value-chain-approach-to-sp',
            'title': 'Value Chain Approach to Sweetpotato',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]


    valueadding_children = [
        {   'id': 'introduction',
            'title': 'Introduction',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': vaintro_children,
            },
        {   'id': 'port-harvest-handling',
            'title': 'Post-harvest Handling',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': postharvest_children,
            },
        {   'id': 'product-development',
            'title': 'Product development',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': productdevelopment_children,
            },
        {   'id': 'demand',
            'title': 'Demand',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': demand_children,
           },
        {   'id': 'case-studies',
            'title': 'Case Studies',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'research-methods',
            'title': 'Research Methods & Tools',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'training-communication',
            'title': 'Training & Communication Material',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    instint_children = [
        {   'id': 'cips',
            'title': 'International Center of Potato',
            'description': 'International Center of Potato International Center of Potato International Center of Potato International Center of Potato International Center of Potato International Center of Potato',
            'type': 'Institution',
            'layout': 'institutionView',
            },
        {   'id': 'cips2',
            'title': 'Another International Institute',
            'description': 'Another International InstituteAnother International Institute Another International Institute Another International Institute Another International Institute Another International Institute Another International Institute ',
            'type': 'Institution',
            'layout': 'institutionView',
            },
        ]

    institMap_children = [
        {   'id': 'cips',
            'title': 'International Center of Potato',
            'description': 'International Center of Potato International Center of Potato International Center of Potato International Center of Potato International Center of Potato International Center of Potato',
            'type': 'Institution',
            'layout': 'folder_listing_institution',
            },
        {   'id': 'cips2',
            'title': 'Another International Institute',
            'description': 'Another International InstituteAnother International Institute Another International Institute Another International Institute Another International Institute Another International Institute Another International Institute ',
            'type': 'Institution',
            'layout': 'folder_listing_institution',
            },
        ]

    institutions_children = [
        {   'id': 'international-research',
            'title': 'International Research',
            'description': '',
            'type': 'Institutions Holder',
            'layout': 'folder_listing_institutions',
            'children': instint_children,
            },
        {   'id': 'national-research',
            'title': 'National Research',
            'description': '',
            'type': 'Institutions Holder',
            'layout': 'folder_listing_institutions',
            },
        {   'id': 'ngo',
            'title': 'NGO',
            'description': '',
            'type': 'Institutions Holder',
            'layout': 'folder_listing_institutions',
            },
        {   'id': 'private-sector',
            'title': 'Private Sector',
            'description': '',
            'type': 'Institutions Holder',
            'layout': 'folder_listing_institutions',
            },
        {   'id': 'institution-maps',
            'title': 'Institution Maps',
            'description': '',
            'type': 'TTGoogleMapCategoryContainer',
            'layout': 'base_view',
             'children': institMap_children,
             },
        ]

    about_children = [
        {   'id': 'about-this-portal',
            'title': 'About This Portal',
            'description': '',
            'type': 'Document',
            'layout' : 'document_view',
            },
        ]

    top_folders = [
        {   'id': 'fp-introduction',
            'title': 'Welcome to Sweetpotato Knowledge Portal',
            'description': '',
            'type': 'Document',
            'layout' : 'document_view',
            },
        {   'id': 'sweetpotato-introduction',
            'title': 'Sweetpotato introduction',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': sweetpotatoIntroduction_children,
            },
        {   'id': 'germplasm',
            'title': 'Germplasm',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': germplasm_children,
            },
        {   'id': 'seedsystem',
            'title': 'Seed System',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': seedsystem_children,
            },
        {   'id': 'crop-management',
            'title': 'Crop Management',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': crop_children,
            },
        {   'id': 'adding-value',
            'title': 'Adding value',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': valueadding_children,
            },
        {   'id': 'use-consumption',
            'title': 'Use and Consumption',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': useconsumption_children,
            },
        {   'id': 'institutions',
            'title': 'Institutions',
            'description': 'There are several institutions and organizations globally which work closely with the sweetpotato. Here you can find a listing of these categorized by international research, national research, NGOs and private sector.',
            'type': 'TTGoogleMap',
            'layout': 'TTGoogleMapView2',
            'children': institutions_children,
            },
        {   'id': 'projects-initiatives',
            'title': 'Projects and Initiatives',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing_projectmain',
            'children': projects_children,
            },
        {   'id': 'about',
            'title': 'About This Portal',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': about_children,
            },
        ]

    createObjects(parent=portal, children=top_folders)

def createObjects(parent, children):
    """This will create new objects, or modify existing ones if id's and type
    match. In total 191.
    """
    parent.plone_log("Creating %s in %s" % (children, parent))
    existing = parent.objectIds()
    parent.plone_log("Existing ids: %s" % existing)
    for new_object in children:
        if new_object['id'] in existing:
            parent.plone_log("%s exists, skipping" % new_object['id'])
        else:
            _createObjectByType(new_object['type'], parent, \
                id=new_object['id'], title=new_object['title'], \
                description=new_object['description'])
        parent.plone_log("Now to modify the new_object...")
        obj = parent.get(new_object['id'], None)
        if obj is None:
            parent.plone_log("can't get new_object %s to modify it!" % new_object['id'])
        else:
            if obj.Type() != new_object['type']:
                parent.plone_log("types don't match!")
            else:
                obj.setLayout(new_object['layout'])
                obj.reindexObject()
                children = new_object.get('children',[])
                if len(children) > 0:
                    createObjects(obj, children)

def setupPortlets(site, out):
    # Register some portlets for this club's context.
    # Copied mostly from plone.portlets' README doctests.
    right = getUtility(IPortletManager, name='plone.rightcolumn')
    left = getUtility(IPortletManager, name='plone.leftcolumn')
    rightColumnInThisContext = getMultiAdapter((site, right), IPortletAssignmentMapping)
    leftColumnInThisContext = getMultiAdapter((site, left), IPortletAssignmentMapping)


    urltool  = getToolByName(site, 'portal_url')

    projectCollectionPortlet = Assignment(header=u"Latest Projects 2",
                                          limit=2,
                                          target_collection = '/'.join(urltool.getRelativeContentPath(site.gpProjects)),
                                          random=False,
                                          show_more=True,
                                          show_dates=False)

#    webmasterPortlet = Assignment(header=u"Control Panel",)

    def saveAssignment(mapping, assignment):
        chooser = INameChooser(mapping)
        mapping[chooser.chooseName(None, assignment)] = assignment

    saveAssignment(leftColumnInThisContext, projectCollectionPortlet)
#    saveAssignment(leftColumnInThisContext, webmasterPortlet)

def setSecuritySettings(portal):
    from plone.app.controlpanel.security import SecurityControlPanelAdapter
    settings = SecurityControlPanelAdapter(portal)
    settings.set_enable_self_reg(True)
    settings.set_allow_anon_views_about(True)
    settings.set_enable_user_folders(True)
    settings.set_enable_user_pwd_choice(True)


def setupAddableTypes(portal):
    # make root folder
    existing = portal.keys()
    if 'rootfolder' not in existing:
        portal.invokeFactory('Folder', id='rootfolder', title='Home')
        portal.rootfolder.setConstrainTypesMode(1) # restrict what this folder can contain
        portal.rootfolder.setImmediatelyAddableTypes(['Folder'])
    #    portal.setLocallyAllowedTypes(['Folder'])
        portal.rootfolder.setLayout('frontpage')
        portal.rootfolder.reindexObject()

def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    portal = context.getSite()

    if context.readDataFile('cip.sppolicy4_various.txt') is None:
        return

    existing = portal.keys()

    if 'gpNews' not in existing:
        _createObjectByType('Topic', portal, id='gpNews', title='Latest on Germplasm',
                            description='Show the latest objects from Germplasm Category')
        theCollection = portal.gpNews
        theCollection.setLimitNumber(True)
        theCollection.setItemCount(4)
        path_crit = theCollection.addCriterion('path','ATRelativePathCriterion')
        path_crit.setRelativePath('../germplasm')
        theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
        theCriteria.setReversed('getId')
        type_crit = theCollection.addCriterion('Type','ATPortalTypeCriterion')
        type_crit.setValue(['News Item', 'Document', 'Folder'])

    if 'ssNews' not in existing:
        _createObjectByType('Topic', portal, id='ssNews', title='Latest on Seedsystem',
                            description='Show the latest objects from Germplasm Category')
        theCollection = portal.ssNews
        theCollection.setLimitNumber(True)
        theCollection.setItemCount(4)
        path_crit = theCollection.addCriterion('path','ATRelativePathCriterion')
        path_crit.setRelativePath('../seedsystem')
        theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
        theCriteria.setReversed('getId')
        type_crit = theCollection.addCriterion('Type','ATPortalTypeCriterion')
        type_crit.setValue(['News Item', 'Document', 'Folder'])

    if 'cmnNews' not in existing:
        _createObjectByType('Topic', portal, id='cmnNews', title='Latest on Crop Management',
                            description='Show the latest objects from Crop Management Category')
        theCollection = portal.cmnNews
        theCollection.setLimitNumber(True)
        theCollection.setItemCount(4)
        path_crit = theCollection.addCriterion('path','ATRelativePathCriterion')
        path_crit.setRelativePath('../crop-management')
        theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
        theCriteria.setReversed('getId')
        type_crit = theCollection.addCriterion('Type','ATPortalTypeCriterion')
        type_crit.setValue(['News Item', 'Document', 'Folder'])

    if 'vaNews' not in existing:
        _createObjectByType('Topic', portal, id='vaNews', title='Latest on Crop Management',
                            description='Show the latest objects from Crop Management Category')
        theCollection = portal.vaNews
        theCollection.setLimitNumber(True)
        theCollection.setItemCount(4)
        path_crit = theCollection.addCriterion('path','ATRelativePathCriterion')
        path_crit.setRelativePath('../adding-value')
        theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
        theCriteria.setReversed('getId')
        type_crit = theCollection.addCriterion('Type','ATPortalTypeCriterion')
        type_crit.setValue(['News Item', 'Document', 'Folder'])

    if 'ucNews' not in existing:
        _createObjectByType('Topic', portal, id='ucNews', title='Latest on Crop Management',
                            description='Show the latest objects from Crop Management Category')
        theCollection = portal.ucNews
        theCollection.setLimitNumber(True)
        theCollection.setItemCount(4)
        path_crit = theCollection.addCriterion('path','ATRelativePathCriterion')
        path_crit.setRelativePath('../use-consumption')
        theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
        theCriteria.setReversed('getId')
        type_crit = theCollection.addCriterion('Type','ATPortalTypeCriterion')
        type_crit.setValue(['News Item', 'Document', 'Folder'])

    if 'gpProjects' not in existing:
        _createObjectByType('Topic', portal, id='gpProjects', title='Latest Proejcts',
                            description='Show the latest Sweetpotato Projects')
        theCollection = portal.gpProjects
        theCollection.setLimitNumber(True)
        theCollection.setItemCount(4)
        theCriteria = theCollection.addCriterion('effective','ATSortCriterion')
        theCriteria.setReversed('getId')
        type_crit = theCollection.addCriterion('Type','ATPortalTypeCriterion')
        type_crit.setValue('Project Folder')


    # Add additional setup code here
#    deletePloneFolders(portal)
#    disableDocument(portal)
    out = StringIO()
    createFolderStructure(portal)
    setupPortlets(portal, out)
    setupAddableTypes(portal)
    setSecuritySettings(portal)
    createGroups(portal)
    importPAS(portal)