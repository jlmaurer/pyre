# -*- Makefile -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2015 all rights reserved
#


# project defaults
include opal.def
# package name
PACKAGE = html
# the python modules
EXPORT_PYTHON_MODULES = \
    __init__.py

# standard targets
all: export

export:: export-package-python-modules

live: live-package-python-modules

# end of file
