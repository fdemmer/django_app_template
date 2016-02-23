Django app template
===================

Read up on Django startproject templates in the official documentation [1]_.

The latest version of the template can be found on github [2]_.


About
-----

Basis for this template was the Django 1.9 standard template.
A few things were added or modified.

- based on Django 1.9.1 template

- added commented samples for: model, model admin and generic view

- added app-level urls.py

- added place holder for app-level templates directory


Usage
-----

This assumes, you already have a virtualenv with Django and created a 
Django project structure.

To create a new app called "bar" run startapp either directly from
the latest archive from github::

    python -m django startapp --template=https://github.com/fdemmer/django_app_template/archive/master.zip bar

Or from a local copy (with new django module/command example)::

    python -m django startapp --template=master.zip foo


.. [1] https://docs.djangoproject.com/en/1.9/ref/django-admin/#startapp
.. [2] https://github.com/fdemmer/django_app_template
