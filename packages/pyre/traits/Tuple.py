# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


# externals
from .. import schemata
# superclass
from .Property import Property


# declaration
class Tuple(Property):
    """
    A property that represents tuples
    """


    # public data
    default = ()
    schema = schemata.sequence(schema=schemata.identity)


    # interface
    def coerce(self, value, **kwds):
        """
        Walk {value} through the casting procedure
        """
        # easy enough for me
        return list(super().coerce(value, **kwds))


    # framework support
    def macro(self, model):
        """
        Return my preferred macro processor
        """
        # ask my schema
        return self.schema.macro(model=model)


    # meta-methods
    def __init__(self, schema=schemata.identity, default=default, **kwds):
        # chain up
        super().__init__(default=default, **kwds)
        # save my schema
        self.schema = schemata.sequence(schema=schema)
        # all done
        return


# end of file 
