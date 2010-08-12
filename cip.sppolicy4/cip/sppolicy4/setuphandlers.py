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

def importPAS(portal):
    users_here = 'jussi;jussi;Jussi;Savolainen;ajussis@gmail.com'
    users = users_here.data.split('\n')
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
    return printed

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
            'title': 'Marker assisted selection',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'wevil-resistance',
            'title': 'Wevil resistance',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    germplasm_children = [
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
            'title': 'Pre-breeding',
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
            'title': 'Research Methods and Tools',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'training-communication',
            'title': 'Training and Communication',
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
            'title': 'Rapid multiplication techniques',
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
            'title': 'Root based',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]


    seedProgation_children= [
        {   'id': 'seed-biology',
            'title': 'Seed biology',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'foundation-seed',
            'title': 'Foundation seed',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': foundationSeed_children,
            },
        {   'id': 'field-multiplication',
            'title': 'Field multiplication',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': fieldMultiplication_children,
            },
        {   'id': 'vine-handling',
            'title': 'Vine handling',
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
            'title': 'Self-supply',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'informal-supply',
            'title': 'Informal supply',
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
            'title': '1, 2, 3 system',
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
            'title': 'On farm',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': onFarm2_children,
            },
        {   'id': 'supply-driven',
            'title': 'Supply driven',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': supplyDriven_children,
            },
        {   'id': 'demand-driven',
            'title': 'Demand driven',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': demandDriven_children,
	    },
        {   'id': 'commercial-formal',
            'title': 'Commercial formal',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
	    },
        {   'id': 'quality-control',
            'title': 'Quality control',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
	    },
        {   'id': 'policy-legal-frameworks',
            'title': 'Policy & legal frameworks',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
	    },
        {   'id': 'gender-in-seed-systems',
            'title': 'Gender in seed systems',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
	    },
        ]

    caseStudies_children = [
        {   'id': 'farmers-seed-acquisition',
            'title': 'Farmers seed acquisition',
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
            'title': 'Seed system organization',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': seedSystemOrganization_children,
            },
        {   'id': 'case-studies',
            'title': 'Case studies',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': caseStudies_children,
            },
        {   'id': 'research-methods-tools',
            'title': 'Research methods & tools',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'training-communication-material',
            'title': 'Training & communication material',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]


    socio_children = [
        {   'id': 'Farming-strategies',
            'title': 'Farming strategies',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'Cultural-aspects',
            'title': 'Cultural aspects',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'Returns-on-investment',
            'title': 'Returns on investment',
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
            'title': 'Plant phenology',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'maturity-indicators',
            'title': 'Maturity indicators',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
    ]

    soil_children = [
        {   'id': 'nutrient-requirements',
            'title': 'Nutrient requirements',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'oraganic-fertilizers',
            'title': 'Oraganic fertilizers',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'inorganic-fertilizers',
            'title': 'Inorganic fertilizers',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
    ]

    agronomy_children = [
        {   'id': 'site-selection',
            'title': 'Site selection',
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
            'title': 'Seed vines and vareity selection',
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
            'title': 'Crop rotation',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'weed-management',
            'title': 'Weed management',
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
            'title': 'Inset pests',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'vertebrate-pests',
            'title': 'Vertebrate pests',
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
            'title': 'Other pests',
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
            'title': 'Soil fertility management',
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
            'title': 'Socio-economic issues',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': socio_children,
            },
        {   'id': 'case-studies',
            'title': 'Case studies',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'research-methods-tools',
            'title': 'Research methods & tools',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'training-communication-material',
            'title': 'Training & communication material',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
    ]

    africa_children = [
        {   'id': 'ssa',
            'title': 'SSA',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing'
            },
        {   'id': 'ea',
            'title': 'EA',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing'
            },
        {   'id': 'wa',
            'title': 'WA',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'sa',
            'title': 'SA',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    global_children = [
        {   'id': 'test-project',
            'title': 'Global Project',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        ]

    projects_children = [
        {   'id': 'global',
            'title': 'Global',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': global_children,
            },
        {   'id': 'africa',
            'title': 'Africa',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': africa_children,
            },
        {   'id': 'latin-america',
            'title': 'Latin America',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'north-america',
            'title': 'North America',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'asia',
            'title': 'Asia',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },

    ]


    top_folders = [
        {   'id': 'sweetpotato-introduction',
            'title': 'Sweetpotato introduction',
            'description': '',
            'type': 'Folder',
            'layout': 'frontpage',
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
        {   'id': 'value-adding',
            'title': 'Value Adding',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'use-consumption',
            'title': 'Use and Consumption',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'institutions',
            'title': 'Institutions',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            },
        {   'id': 'projects-initiatives',
            'title': 'Projects and Initiatives',
            'description': '',
            'type': 'Folder',
            'layout': 'folder_listing',
            'children': projects_children,
            },
        ]
    createObjects(parent=portal, children=top_folders)

def createObjects(parent, children):
    """This will create new objects, or modify existing ones if id's and type
    match.
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

def disableDocument(portal):
    portal_types = getToolByName(portal, 'portal_types')
    document_fti = getattr(portal_types, 'Document')
    document_fti.global_allow = False

def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    portal = context.getSite()

    if context.readDataFile('cip.sppolicy4_various.txt') is None:
        return

    # Add additional setup code here
#    deletePloneFolders(portal)
#    disableDocument(portal)
    createFolderStructure(portal)
#    importPAS(portal)


