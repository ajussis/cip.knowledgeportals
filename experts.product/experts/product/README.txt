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
The Media content type
===============================

In this section we are tesing the Media content type by performing
basic operations like adding, updadating and deleting Media content
items.

Adding a new Media content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Media' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Media').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Media' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Media Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Media' content item to the portal.

Updating an existing Media content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Media Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Media Sample' in browser.contents
    True

Removing a/an Media content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Media
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Media Sample' in browser.contents
    True

Now we are going to delete the 'New Media Sample' object. First we
go to the contents tab and select the 'New Media Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Media Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Media
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Media Sample' in browser.contents
    False

Adding a new Media content item as contributor
------------------------------------------------

Not only site managers are allowed to add Media content items, but
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

We select 'Media' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Media').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Media' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Media Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Media content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Portfolio content type
===============================

In this section we are tesing the Portfolio content type by performing
basic operations like adding, updadating and deleting Portfolio content
items.

Adding a new Portfolio content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Portfolio' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Portfolio').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Portfolio' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Portfolio Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Portfolio' content item to the portal.

Updating an existing Portfolio content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Portfolio Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Portfolio Sample' in browser.contents
    True

Removing a/an Portfolio content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Portfolio
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Portfolio Sample' in browser.contents
    True

Now we are going to delete the 'New Portfolio Sample' object. First we
go to the contents tab and select the 'New Portfolio Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Portfolio Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Portfolio
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Portfolio Sample' in browser.contents
    False

Adding a new Portfolio content item as contributor
------------------------------------------------

Not only site managers are allowed to add Portfolio content items, but
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

We select 'Portfolio' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Portfolio').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Portfolio' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Portfolio Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Portfolio content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The CIP Portfolio content type
===============================

In this section we are tesing the CIP Portfolio content type by performing
basic operations like adding, updadating and deleting CIP Portfolio content
items.

Adding a new CIP Portfolio content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'CIP Portfolio' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CIP Portfolio').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CIP Portfolio' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CIP Portfolio Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'CIP Portfolio' content item to the portal.

Updating an existing CIP Portfolio content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New CIP Portfolio Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New CIP Portfolio Sample' in browser.contents
    True

Removing a/an CIP Portfolio content item
--------------------------------

If we go to the home page, we can see a tab with the 'New CIP Portfolio
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New CIP Portfolio Sample' in browser.contents
    True

Now we are going to delete the 'New CIP Portfolio Sample' object. First we
go to the contents tab and select the 'New CIP Portfolio Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New CIP Portfolio Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New CIP Portfolio
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New CIP Portfolio Sample' in browser.contents
    False

Adding a new CIP Portfolio content item as contributor
------------------------------------------------

Not only site managers are allowed to add CIP Portfolio content items, but
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

We select 'CIP Portfolio' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CIP Portfolio').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CIP Portfolio' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CIP Portfolio Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new CIP Portfolio content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Media Contact content type
===============================

In this section we are tesing the Media Contact content type by performing
basic operations like adding, updadating and deleting Media Contact content
items.

Adding a new Media Contact content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Media Contact' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Media Contact').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Media Contact' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Media Contact Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Media Contact' content item to the portal.

Updating an existing Media Contact content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Media Contact Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Media Contact Sample' in browser.contents
    True

Removing a/an Media Contact content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Media Contact
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Media Contact Sample' in browser.contents
    True

Now we are going to delete the 'New Media Contact Sample' object. First we
go to the contents tab and select the 'New Media Contact Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Media Contact Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Media Contact
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Media Contact Sample' in browser.contents
    False

Adding a new Media Contact content item as contributor
------------------------------------------------

Not only site managers are allowed to add Media Contact content items, but
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

We select 'Media Contact' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Media Contact').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Media Contact' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Media Contact Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Media Contact content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Contact content type
===============================

In this section we are tesing the Contact content type by performing
basic operations like adding, updadating and deleting Contact content
items.

Adding a new Contact content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Contact' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Contact').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Contact' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Contact Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Contact' content item to the portal.

Updating an existing Contact content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Contact Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Contact Sample' in browser.contents
    True

Removing a/an Contact content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Contact
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Contact Sample' in browser.contents
    True

Now we are going to delete the 'New Contact Sample' object. First we
go to the contents tab and select the 'New Contact Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Contact Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Contact
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Contact Sample' in browser.contents
    False

Adding a new Contact content item as contributor
------------------------------------------------

Not only site managers are allowed to add Contact content items, but
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

We select 'Contact' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Contact').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Contact' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Contact Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Contact content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Experts Event content type
===============================

In this section we are tesing the Experts Event content type by performing
basic operations like adding, updadating and deleting Experts Event content
items.

Adding a new Experts Event content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Experts Event' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Experts Event').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Experts Event' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Experts Event Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Experts Event' content item to the portal.

Updating an existing Experts Event content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Experts Event Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Experts Event Sample' in browser.contents
    True

Removing a/an Experts Event content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Experts Event
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Experts Event Sample' in browser.contents
    True

Now we are going to delete the 'New Experts Event Sample' object. First we
go to the contents tab and select the 'New Experts Event Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Experts Event Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Experts Event
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Experts Event Sample' in browser.contents
    False

Adding a new Experts Event content item as contributor
------------------------------------------------

Not only site managers are allowed to add Experts Event content items, but
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

We select 'Experts Event' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Experts Event').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Experts Event' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Experts Event Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Experts Event content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Directory content type
===============================

In this section we are tesing the Directory content type by performing
basic operations like adding, updadating and deleting Directory content
items.

Adding a new Directory content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Directory' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Directory').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Directory' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Directory Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Directory' content item to the portal.

Updating an existing Directory content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Directory Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Directory Sample' in browser.contents
    True

Removing a/an Directory content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Directory
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Directory Sample' in browser.contents
    True

Now we are going to delete the 'New Directory Sample' object. First we
go to the contents tab and select the 'New Directory Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Directory Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Directory
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Directory Sample' in browser.contents
    False

Adding a new Directory content item as contributor
------------------------------------------------

Not only site managers are allowed to add Directory content items, but
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

We select 'Directory' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Directory').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Directory' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Directory Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Directory content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Photo content type
===============================

In this section we are tesing the Photo content type by performing
basic operations like adding, updadating and deleting Photo content
items.

Adding a new Photo content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Photo' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Photo').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Photo' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Photo Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Photo' content item to the portal.

Updating an existing Photo content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Photo Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Photo Sample' in browser.contents
    True

Removing a/an Photo content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Photo
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Photo Sample' in browser.contents
    True

Now we are going to delete the 'New Photo Sample' object. First we
go to the contents tab and select the 'New Photo Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Photo Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Photo
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Photo Sample' in browser.contents
    False

Adding a new Photo content item as contributor
------------------------------------------------

Not only site managers are allowed to add Photo content items, but
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

We select 'Photo' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Photo').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Photo' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Photo Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Photo content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Media Contact content type
===============================

In this section we are tesing the Media Contact content type by performing
basic operations like adding, updadating and deleting Media Contact content
items.

Adding a new Media Contact content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Media Contact' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Media Contact').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Media Contact' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Media Contact Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Media Contact' content item to the portal.

Updating an existing Media Contact content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Media Contact Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Media Contact Sample' in browser.contents
    True

Removing a/an Media Contact content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Media Contact
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Media Contact Sample' in browser.contents
    True

Now we are going to delete the 'New Media Contact Sample' object. First we
go to the contents tab and select the 'New Media Contact Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Media Contact Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Media Contact
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Media Contact Sample' in browser.contents
    False

Adding a new Media Contact content item as contributor
------------------------------------------------

Not only site managers are allowed to add Media Contact content items, but
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

We select 'Media Contact' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Media Contact').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Media Contact' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Media Contact Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Media Contact content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Experts Event content type
===============================

In this section we are tesing the Experts Event content type by performing
basic operations like adding, updadating and deleting Experts Event content
items.

Adding a new Experts Event content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Experts Event' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Experts Event').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Experts Event' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Experts Event Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Experts Event' content item to the portal.

Updating an existing Experts Event content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Experts Event Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Experts Event Sample' in browser.contents
    True

Removing a/an Experts Event content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Experts Event
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Experts Event Sample' in browser.contents
    True

Now we are going to delete the 'New Experts Event Sample' object. First we
go to the contents tab and select the 'New Experts Event Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Experts Event Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Experts Event
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Experts Event Sample' in browser.contents
    False

Adding a new Experts Event content item as contributor
------------------------------------------------

Not only site managers are allowed to add Experts Event content items, but
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

We select 'Experts Event' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Experts Event').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Experts Event' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Experts Event Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Experts Event content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)



