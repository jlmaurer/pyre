#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


"""
Verify that decimal conversions work as  expected
"""


def test():
    import decimal
    import pyre.schemata

    # create a descriptor
    descriptor = pyre.schemata.decimal

    # check
    assert descriptor.coerce("1.20") == decimal.Decimal("1.20")

    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    test()


# end of file 