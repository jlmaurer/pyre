# -*- Makefile -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2015 all rights reserved
#

# project defaults
include pyre.def
# package name
PACKAGE = externals
# the python modules
EXPORT_PYTHON_MODULES = \
    Category.py \
    Library.py \
    MPI.py \
    MPICH.py \
    OpenMPI.py \
    Package.py \
    Python.py \
    Tool.py \
    __init__.py

# standard targets
all: export

export:: export-package-python-modules

live: live-package-python-modules

# end of file
