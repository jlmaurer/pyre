# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# for my metaclass
import pyre


# the singleton that owns the global state
class Chronicler(metaclass=pyre.patterns.singleton):
    """
    The manager of the journal global state
    """


    # public data
    notes = None
    device = None
    verbosity = 1


    # metamethods
    def __init__(self, verbosity=verbosity, device=device, notes=notes, **kwds):
        # chain up
        super().__init__(**kwds)

        # the default verbosity
        self.verbosity = verbosity

        # the global metadata; can't be empty
        self.notes = notes if notes is not None else {
            "application": "journal",  # this key is required; applications should override
            }

        # if whoever initialized the journal did not expressed an opinion regarding the device
        if device is None:
            # grab the console
            from .Console import Console as cout
            # and instantiate it
            device = cout()
        # attach it
        self.device = device

        # all done
        return


# end of file
