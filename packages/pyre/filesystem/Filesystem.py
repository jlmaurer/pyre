# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


# externals
import weakref # for {vnodes}, the weak key dictionary
# base class
from .Folder import Folder


# declaration
class Filesystem(Folder):
    """
    The base class for representing filesystems

    A filesystem is a special {Folder} that maintains an association between the {Nodes} it
    contains and {Info} objects that are dependent on the specific filesystem type and capture
    what the filesystem knows about them.
    """


    # types
    from .Info import Info as metadata


    # interface
    def info(self, node):
        """
        Look up and return the available metadata associated with {node}
        """
        # let the exceptions through, for now
        return self.vnodes[node]


    def open(self, node, **kwds):
        """
        Open the file associated with {node}
        """
        # i don't know how to do it
        raise NotImplementedError(
            "class {.__name__!r} must implement 'open'".format(type(self)))


    # implementation details
    def attach(self, node, uri, metadata=None, **kwds):
        """
        Maintenance for the {vnode} table. Filesystems that maintain more elaborate metadata
        about their nodes must override to build their info structures.
        """
        # build an {info} structure if necessary
        meta = metadata if metadata is not None else self.metadata(uri=uri, **kwds)
        # attach it to my vnode table
        self.vnodes[node] = meta
        # and return the info node
        return meta


    # meta methods
    def __init__(self, metadata=None, **kwds):
        # chain up to make me a valid node with me as the filesystem
        super().__init__(filesystem=self, **kwds)
        # my vnode table: a map from nodes to info structures
        self.vnodes = weakref.WeakKeyDictionary()
        # build an info structure for myself
        metadata = metadata if metadata is not None else self.metadata(uri='/')
        # add it to my vnode table
        self.vnodes[self] = metadata
        # all done
        return


    # implementation details
    __slots__ = ('vnodes')


# end of file 
