# Create new members with properties supplied from a CSV file.
# The script expects a File object with id `users.csv` in the same folder
# it resides.
#
# The format of the CSV needs to be:
#
# password;userid;lastname;firstname;email
#
# created 2006-11-03 by Tom Lazar <tom@tomster.org>, http://tomster.org/
# under a BSD-style licence (i.e. use as you wish but don't sue me)


from Products.CMFCore.utils import getToolByName
users = context['users.csv'].data.split('\n')
regtool = getToolByName(context, 'portal_registration')
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

