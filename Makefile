PROJECT_NAME=PhotoPlanet
PYTHONPATH=$(CURDIR):$(CURDIR)/$(PROJECT_NAME)

MANAGE= PYTHONPATH=$(PYTHONPATH) python manage.py

runserver:
	$(MANAGE) runserver --settings=PhotoPlanet.settings.base
