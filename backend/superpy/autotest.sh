#!/bin/sh
find . -name \*.py | entr -cp pytest
