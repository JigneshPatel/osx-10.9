NAME = bonjour-py
VERSION = 0.3

include ../Makefile.inc

custompatching:
	ed - $(DIR)/setup.py < setup.py.ed

postinstall:
	cp -f $(DIR)/COPYING.txt $(OSL)/$(NAME)-$(VERSION).txt
	cp -f $(NAME).partial $(OSV)/$(NAME)-$(VERSION).partial
