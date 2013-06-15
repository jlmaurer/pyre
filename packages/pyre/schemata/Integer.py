# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2013 all rights reserved
#


# superclass
from .Type import Type


# declaration
class Integer(Type):
    """
    A type declarator for integers
    """


    # constants
    typename = 'int' # the name of my type


    # interface
    def coerce(self, value, **kwds):
        """
        Attempt to convert {value} into a float
        """
        # get the interpreter to evaluate simple expressions
        if isinstance(value, str): value = eval(value)

        # attempt to 
        try:
            # cast {value} into an integer
            return int(value)
        # if that fails
        except (TypeError, ValueError) as error:
            # complain
            raise self.CastingError(value=value, description=str(error)) from None


    # meta-methods
    def __init__(self, default=int(), **kwds):
        # chain up with my default
        super().__init__(default=default, **kwds)
        # all done
        return


# end of file 
