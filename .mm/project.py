# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


def requirements():
    """
    Build a dictionary with the external dependencies of the {pyre} project
    """

    # build the package instances
    packages = [
        Package(name='cuda', optional=True),
        Package(name='gsl', optional=True),
        Package(name='libpq', optional=True),
        Package(name='mpi', optional=True),
        Package(name='python', optional=False),
        ]

    # build a dictionary and return it
    return { package.name: package for package in packages }


# end of file 
