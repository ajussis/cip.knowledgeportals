## Script (Python) "getMemberById"
##parameters=userid=''
##title=get User by Proxy
##
context.plone_log('userid=')
context.plone_log(userid)
return context.portal_membership.getMemberById(userid);