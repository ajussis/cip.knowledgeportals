from Products.CMFCore.utils import getToolByName

def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('cip.potatotheme_various.txt') is None:
        return

    # Set frontpage template

    portal_url = getToolByName(context, "portal_url")
    portal = portal_url.getPortalObject()
    
    

    # Add additional setup code here
