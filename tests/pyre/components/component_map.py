#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


import pyre

class container(pyre.component, family="sample.map"):
    """a component container"""
    map = pyre.map(cast=pyre.properties.str)


def test():
    # build the shell
    s = container(name="map_container")
    # verify that the catalog has three members
    # print(len(s.catalog))
    assert len(s.map) == 3
    # and that the contents were configured properly
    for name, instance in s.map.items():
        # print("tag: {!r}, name: {!r}".format(instance.tag, name))
        assert 'value({})'.format(name) == instance

    return s
    

# main
if __name__ == "__main__":
    test()


# end of file 