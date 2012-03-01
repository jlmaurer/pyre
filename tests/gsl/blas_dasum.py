#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


"""
Exercise {dasum}
"""


def test():
    # externals
    import gsl
    import math
    # a value
    x = -3
    # make a couple of vectors
    v = gsl.vector(shape=10).fill(x)
    # compute the dot product
    assert gsl.blas.dasum(v) ==  v.shape * abs(x)
    # all done
    return


# main
if __name__ == "__main__":
    test()


# end of file 
