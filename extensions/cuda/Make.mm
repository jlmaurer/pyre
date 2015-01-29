# -*- Makefile -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2015 all rights reserved
#

# project defaults
include cuda.def
# package name
PACKAGE =
# the module
MODULE = cuda
# get the cuda support
include cuda/default.def
# and build a python module
include std-pythonmodule.def
# use a tmp directory that knows the name of the module
PROJ_TMPDIR = $(BLD_TMPDIR)/$(PROJECT)/$(PACKAGE)/$(MODULE)
# point to the location of my libraries
PROJ_LCXX_LIBPATH=$(BLD_LIBDIR)
# link against these
PROJ_LIBRARIES = -ljournal
# the sources
PROJ_SRCS = \
    discover.cc \
    exceptions.cc \
    metadata.cc

# end of file
