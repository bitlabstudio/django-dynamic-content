Django Dynamic Content
======================

A reusable Django app that allows to place dynamic content into templates.

Usually you would use a CMS like `django-cms <https://www.django-cms.org>`_ for
this scenario, which also has very useful static placeholders as of version 3,
but sometimes you have a small project that doesn't need a fully blown CMS. In
this usecase a simple model with content that can be edited via the admin and
which instances can be placed in templates would be nice to have.

As this app grows, we might add frontend editing ability in the future.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-dynamic-content

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-dynamic-content.git#egg=dynamic_content

Add ``dynamic_content`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'dynamic_content',
		'hvad',
		'ckeditor',
    )

Please check out the ckeditor docs for installation and configuration:
https://github.com/django-ckeditor/django-ckeditor

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load dynamic_content_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate dynamic_content


Usage
-----

Just put this into your template:

.. code-block:: html

    {% load dynamic_content_tags %}
    {% get_content "FOOTER_INFO" default="Foobar!" as footer %}
	{{ footer.content|linebreaks }}
	{{ footer.content_html|safe }}

Of course you are not forced to use both content fields (html and non-html).


Templatetags
------------

get_content
+++++++++++

Usage: ``{% get_content "<content_identifier" [default="Default text"] as <variable_name> %}``

This is an assignment tag that simply fetches the content from the database
based on the given unique content identifier.

If no object with the given identifier is found, a new one will be created.
If you pass in a ``default`` text, the new object will be created with that
text.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-dynamic-content
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
