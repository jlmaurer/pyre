# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


def connect(**kwds):
    """
    Establish a new connection to a database back end

    See the Connection class documentation for information on how to control the connection
    details through the arguments to this function
    """
    from .Connection import Connection
    return Connection(**kwds)


# end of file 
