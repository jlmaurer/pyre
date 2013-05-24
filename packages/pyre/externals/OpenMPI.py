# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


# superclass
from .MPI import MPI


# the openmpi package manager
class OpenMPI(MPI, family='pyre.externals.openmpi'):
    """
    The package manager for OpenMPI packages
    """


# end of file 