#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


"""
Verify that the metadata associated with node are maintained properly
"""


def test():
    import pyre.filesystem

    # build a virtual filesystem
    root = pyre.filesystem.virtual()
    # and a couple of nodes
    root['home/users'] = root.folder()
    root['home/users/mga'] = root.folder()

    # check their uris
    assert root['home/users'].uri == '/home/users'
    assert root['home/users/mga'].uri == '/home/users/mga'

    # all done
    return root


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    test()


# end of file 
