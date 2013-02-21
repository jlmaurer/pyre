#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


"""
Check that float conversions work as expected
"""


def test():
    import pyre.schemata

    # create a descriptor
    descriptor = pyre.schemata.float

    # casts
    # successful
    assert 1.2 == descriptor.coerce(1.2)
    assert 1.2 == descriptor.coerce("1.2")
    # failures
    try:
        descriptor.coerce(test)
        assert False
    except descriptor.CastingError as error:
        assert str(error) == "float() argument must be a string or a number"
        
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    test()


# end of file 