##########################
Packaginator Sentry Server
##########################


************
Installation
************

#. ``git clone https://github.com/cartwheelweb/packaginator-sentry``
#. ``cd packaginator-sentry``
#. Create a virtualenv in your preferred way (eg. using ``mkvirtualenv``).
#. ``pip install -r requirements.txt``
#. Edit ``src/local_settings.py`` with the text editor of your choice. You will
   want to add the ``SENTRY_KEY`` setting as well as proper database settings.
#. ``src/manage.py syncdb``
#. For local testing: ``src/manage.py runserver``; for production: Set up your
   webserver.