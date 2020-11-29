MANAGE=./manage.py

server:
	$(MANAGE) runserver

migrate:
	$(MANAGE) migrate

test:
	$(MANAGE) test
