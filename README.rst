Django-Extauth - External authentication/authorization support for Django
=========================================================================
.. image:: https://badge.fury.io/py/django-extauth.svg
    :target: https://badge.fury.io/py/django-extauth

This Django app replaces the standard Django’s user module and auth
system with a thin wrapper over an external auth system. This way, you
can manage users and their permissions in a centralized way, and use a
single log in page for all your services.

Requirements
------------

- Python 3.6+. **Python 2 is not supported, and won’t ever get supported.**
- Django 1.10+

Installation
------------

.. code:: python

    pip install django_extauth

Configuration
-------------

settings.py
~~~~~~~~~~~

.. code:: python

    INSTALLED_APPS += ['django_extauth']

    AUTH_USER_MODEL = 'django_extauth.User'

    EXTAUTH_BACKEND = 'django_extauth.contrib.dummy'

Backends
--------

Existing:

- dummy - always sets request.user to a “dummy” user with full admin access
- `gitlab`_

Planned:

- oidc - OpenID Connect

.. _gitlab: https://github.com/LEW21/django-extauth/tree/master/django_extauth/contrib/gitlab
