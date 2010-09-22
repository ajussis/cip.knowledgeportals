Introduction
============

This is a full-blown functional test. The emphasis here is on testing what
the user may input and see, and the system is largely tested as a black box.
We use PloneTestCase to set up this test as well, so we have a full Plone site
to play with. We *can* inspect the state of the portal, e.g. using 
self.portal and self.folder, but it is often frowned upon since you are not
treating the system as a black box. Also, if you, for example, log in or set
roles using calls like self.setRoles(), these are not reflected in the test
browser, which runs as a separate session.

Being a doctest, we can tell a story here.

First, we must perform some setup. We use the testbrowser that is shipped
with Five, as this provides proper Zope 2 integration. Most of the 
documentation, though, is in the underlying zope.testbrower package.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()

The following is useful when writing and debugging testbrowser tests. It lets
us see all error messages in the error_log.

    >>> self.portal.error_log._ignored_exceptions = ()

With that in place, we can go to the portal front page and log in. We will
do this using the default user from PloneTestCase:

    >>> from Products.PloneTestCase.setup import portal_owner, default_password

Because add-on themes or products may remove or hide the login portlet, this test will use the login form that comes with plone.  

    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

Here, we set the value of the fields on the login form and then simulate a
submit click.  We then ensure that we get the friendly logged-in message:

    >>> "You are now logged in" in browser.contents
    True

Finally, let's return to the front page of our site before continuing

    >>> browser.open(portal_url)

-*- extra stuff goes here -*-
The Research Paper content type
===============================

In this section we are tesing the Research Paper content type by performing
basic operations like adding, updadating and deleting Research Paper content
items.

Adding a new Research Paper content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Research Paper' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Research Paper').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Research Paper' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Research Paper Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Research Paper' content item to the portal.

Updating an existing Research Paper content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Research Paper Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Research Paper Sample' in browser.contents
    True

Removing a/an Research Paper content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Research Paper
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Research Paper Sample' in browser.contents
    True

Now we are going to delete the 'New Research Paper Sample' object. First we
go to the contents tab and select the 'New Research Paper Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Research Paper Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Research Paper
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Research Paper Sample' in browser.contents
    False

Adding a new Research Paper content item as contributor
------------------------------------------------

Not only site managers are allowed to add Research Paper content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Research Paper' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Research Paper').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Research Paper' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Research Paper Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Research Paper content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Institutions Holder content type
===============================

In this section we are tesing the Institutions Holder content type by performing
basic operations like adding, updadating and deleting Institutions Holder content
items.

Adding a new Institutions Holder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Institutions Holder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Institutions Holder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Institutions Holder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Institutions Holder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Institutions Holder' content item to the portal.

Updating an existing Institutions Holder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Institutions Holder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Institutions Holder Sample' in browser.contents
    True

Removing a/an Institutions Holder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Institutions Holder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Institutions Holder Sample' in browser.contents
    True

Now we are going to delete the 'New Institutions Holder Sample' object. First we
go to the contents tab and select the 'New Institutions Holder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Institutions Holder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Institutions Holder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Institutions Holder Sample' in browser.contents
    False

Adding a new Institutions Holder content item as contributor
------------------------------------------------

Not only site managers are allowed to add Institutions Holder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Institutions Holder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Institutions Holder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Institutions Holder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Institutions Holder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Institutions Holder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Gallery Folder content type
===============================

In this section we are tesing the Gallery Folder content type by performing
basic operations like adding, updadating and deleting Gallery Folder content
items.

Adding a new Gallery Folder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Gallery Folder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Gallery Folder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Gallery Folder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Gallery Folder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Gallery Folder' content item to the portal.

Updating an existing Gallery Folder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Gallery Folder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Gallery Folder Sample' in browser.contents
    True

Removing a/an Gallery Folder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Gallery Folder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Gallery Folder Sample' in browser.contents
    True

Now we are going to delete the 'New Gallery Folder Sample' object. First we
go to the contents tab and select the 'New Gallery Folder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Gallery Folder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Gallery Folder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Gallery Folder Sample' in browser.contents
    False

Adding a new Gallery Folder content item as contributor
------------------------------------------------

Not only site managers are allowed to add Gallery Folder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Gallery Folder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Gallery Folder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Gallery Folder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Gallery Folder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Gallery Folder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Projects Holder content type
===============================

In this section we are tesing the Projects Holder content type by performing
basic operations like adding, updadating and deleting Projects Holder content
items.

Adding a new Projects Holder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Projects Holder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Projects Holder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Projects Holder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Projects Holder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Projects Holder' content item to the portal.

Updating an existing Projects Holder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Projects Holder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Projects Holder Sample' in browser.contents
    True

Removing a/an Projects Holder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Projects Holder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Projects Holder Sample' in browser.contents
    True

Now we are going to delete the 'New Projects Holder Sample' object. First we
go to the contents tab and select the 'New Projects Holder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Projects Holder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Projects Holder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Projects Holder Sample' in browser.contents
    False

Adding a new Projects Holder content item as contributor
------------------------------------------------

Not only site managers are allowed to add Projects Holder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Projects Holder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Projects Holder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Projects Holder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Projects Holder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Projects Holder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Institution content type
===============================

In this section we are tesing the Institution content type by performing
basic operations like adding, updadating and deleting Institution content
items.

Adding a new Institution content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Institution' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Institution').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Institution' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Institution Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Institution' content item to the portal.

Updating an existing Institution content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Institution Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Institution Sample' in browser.contents
    True

Removing a/an Institution content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Institution
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Institution Sample' in browser.contents
    True

Now we are going to delete the 'New Institution Sample' object. First we
go to the contents tab and select the 'New Institution Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Institution Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Institution
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Institution Sample' in browser.contents
    False

Adding a new Institution content item as contributor
------------------------------------------------

Not only site managers are allowed to add Institution content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Institution' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Institution').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Institution' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Institution Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Institution content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Project Folder content type
===============================

In this section we are tesing the Project Folder content type by performing
basic operations like adding, updadating and deleting Project Folder content
items.

Adding a new Project Folder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Project Folder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Project Folder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Project Folder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Project Folder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Project Folder' content item to the portal.

Updating an existing Project Folder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Project Folder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Project Folder Sample' in browser.contents
    True

Removing a/an Project Folder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Project Folder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Project Folder Sample' in browser.contents
    True

Now we are going to delete the 'New Project Folder Sample' object. First we
go to the contents tab and select the 'New Project Folder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Project Folder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Project Folder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Project Folder Sample' in browser.contents
    False

Adding a new Project Folder content item as contributor
------------------------------------------------

Not only site managers are allowed to add Project Folder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Project Folder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Project Folder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Project Folder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Project Folder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Project Folder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)



