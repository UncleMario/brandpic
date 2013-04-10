#!/bin/sh

sudo -u postgres dropdb brandpic
sudo -u postgres createdb brandpic
python manage.py syncdb --settings brandpic.localsettings
python manage.py runserver --settings brandpic.localsettings
