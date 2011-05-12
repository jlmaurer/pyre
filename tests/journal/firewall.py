#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


"""
Verify that firewall channels by the same name share a common state
"""


def test():
    # access the package
    import journal
    # build a firewall channel
    firewall = journal.firewall("journal.test1")
    # verify that it is off by default
    assert firewall.active == True
    # enable it
    firewall.active = False

    # access the same channel through another object
    clone = journal.firewall("journal.test1")
    # verify that it is now on
    assert clone.active == False

    # build a firewall channel with a different name
    another = journal.firewall("journal.test2")
    # verify that it is off by default, to make sure that there is no crosstalk between channels
    assert another.active == True

    # all done
    return


# main
if __name__ == "__main__":
    test()


# end of file 
