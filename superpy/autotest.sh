#!/bin/sh
find . -name \*.py | entr -cps '
	black --verbose --line-length 79 $0
	flake8 $0
	pytest
'
