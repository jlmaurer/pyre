# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#

"""
Definitions for all the exceptions raised by this package
"""

from ..framework.exceptions import FrameworkError


class GenericError(FrameworkError):
    """
    Base class for all errors in this package

    Can be used as a catchall when detecting errors generated by this package
    """


class DirectoryListingError(GenericError):
    """
    Exception raised when something goes wrong with listing the contents of a local directory
    """

    def __init__(self, uri, error, **kwds):
        msg = "error while accessing {!r}: {}".format(uri, error)
        super().__init__(description=msg, **kwds)
        self.uri = uri
        return


class MountPointError(GenericError):
    """
    Exception generated when the root of a filesystem is invalid
    """

    def __init__(self, uri, error):
        msg = "error while mounting {!r}: {}".format(uri, error)
        super().__init__(description=msg)
        self.uri = uri
        return


class FilesystemError(GenericError):
    """
    Base class for all filesystem errors

    Can be used as a catchall when detecting filesystem related exceptions
    """

    def __init__(self, filesystem, node, **kwds):
        super().__init__(**kwds)
        self.filesystem = filesystem
        self.node = node
        return


class NotFoundError(FilesystemError):
    """
    Exception raised when attempting to find a node and the supplied URI does not exist
    """

    def __init__(self, uri, fragment, **kwds):
        msg = "while looking for {!r}: {!r} not found".format(uri, fragment)
        super().__init__(description=msg, **kwds)
        self.uri = uri
        self.fragment = fragment
        return


class FolderInsertionError(FilesystemError):
    """
    Exception raised when attempting to insert a node in a filsystem and the target node is not
    a folder
    """

    def __init__(self, uri, target, **kwds):
        msg = "error while inserting {!r}: {!r} is not a folder".format(uri, target)
        super().__init__(description=msg, **kwds)
        self.uri = uri
        self.target = target
        return


class URISpecificationError(GenericError):
    """
    Exception raised when the supplied uri cannot be decoded
    """

    def __init__(self, uri, reason, **kwds):
        msg = "{}: {}".format(uri, reason)
        super().__init__(description=msg , **kwds)
        self.uri = uri
        self.reason = reason
        return


# end of file 
