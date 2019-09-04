# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2019 all rights reserved
#


# support
import pyre
# my protocol
from .Producer import Producer
# my superclass
from .Node import Node
# my meta-class
from .FactoryMaker import FactoryMaker


# class declaration
class Factory(Node, metaclass=FactoryMaker, implements=Producer, internal=True):
    """
    The base class for creators of data products
    """


    # types
    from .exceptions import IncompleteFlowError


    # public data
    @property
    def pyre_inputs(self):
        """
        Build the list of my input products
        """
        # grab my inventory
        inventory = self.pyre_inventory
        # go through my input traits
        for trait in self.pyre_inputTraits:
            # get the associated product
            product = inventory[trait].value
            # pass it on along with its meta-data
            yield trait, product
        # all done
        return


    @property
    def pyre_outputs(self):
        """
        Build the list of my output products
        """
        # grab my inventory
        inventory = self.pyre_inventory
        # go through my output traits
        for trait in self.pyre_outputTraits:
            # get the associated product
            product = inventory[trait].value
            # pass it on along with its meta-data
            yield trait, product
        # all done
        return


    # protocol obligations
    @pyre.export
    def pyre_make(self, **kwds):
        """
        Construct my products
        """
        # sort my inputs
        unbound, stale, _ = self.pyre_examineInputs()
        # if there are unbound traits
        if unbound:
            # build a locator that blames my caller
            locator = pyre.tracking.here(level=1)
            # complain
            raise self.IncompleteFlowError(node=self, traits=unbound, locator=locator)
        # go through the stale products
        for product in stale:
            # refresh them
            product.pyre_make(**kwds)
        # if anything were stale
        if stale:
            # invoke me
            self.pyre_run(stale=stale, **kwds)
        # all done
        return


    @pyre.export
    def pyre_tasklist(self, **kwds):
        """
        Generate the sequence of factories that must be invoked to rebuild a product
        """
        # sort my inputs
        unbound, stale, _ = self.pyre_examineInputs()
        # if there are unbound traits
        if unbound:
            # build a locator that blames my caller
            locator = pyre.tracking.here(level=1)
            # complain
            raise self.IncompleteFlowError(node=self, traits=unbound, locator=locator)
        # go through the stale products
        for product in stale:
            # ask them to contribute
            yield from product.pyre_tasklist(**kwds)
        # add me to the pile
        yield self
        # all done
        return


    @pyre.export
    def pyre_targets(self, context=None):
        """
        Generate the sequence of products that must be refreshed
        """
        # sort my inputs
        unbound, stale, _ = self.pyre_examineInputs()
        # if there are unbound traits
        if unbound:
            # build a locator that blames my caller
            locator = pyre.tracking.here(level=1)
            # complain
            raise self.IncompleteFlowError(node=self, traits=unbound, locator=locator)
        # go through the stale inputs
        for product in stale:
            # ask them to contribute
            yield from product.pyre_targets()
        # all done
        return


    # meta-methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # get my inventory
        inventory = self.pyre_inventory
        # get my inputs
        inputs = (inventory[trait].value for trait in self.pyre_inputTraits)
        # bind me to them
        self.pyre_bindInputs(*inputs)
        # get my outputs
        outputs = (inventory[trait].value for trait in self.pyre_outputTraits)
        # bind me to them
        self.pyre_bindOutputs(*outputs)
        # all done
        return


    # flow hooks
    # deployment
    def pyre_run(self, **kwds):
        """
        Invoke me and remake my products
        """
        # nothing to do
        return self


    # status management
    def pyre_newStatus(self, **kwds):
        """
        Build a handler for my status changes
        """
        # grab the factory
        from .FactoryStatus import FactoryStatus
        # make one and return it
        return FactoryStatus(**kwds)


    # introspection
    def pyre_examineInputs(self):
        """
        Go through my inputs and sort them in three piles: unbound, stale, and fresh
        """
        # make a pile of fresh inputs
        fresh = []
        # one for stale inputs
        stale = []
        # and another for the unbound traits
        unbound = []
        # go through my inputs
        for trait, product in self.pyre_inputs:
            # if the product is unbound
            if product is None:
                # add it to the pile
                unbound.append(trait)
                # and move on
                continue
            # if the product is stale
            if product.pyre_stale is True:
                # add it to the stale pile
                stale.append(product)
                # and move on
                continue
            # otherwise, it must be fresh
            fresh.append(product)
        # return the three piles
        return unbound, stale, fresh


    # connectivity maintenance
    def pyre_bindInputs(self, *inputs):
        """
        Bind me to the sequence of products in {inputs}
        """
        # get my status monitor
        monitor = self.pyre_status
        # go through each of my inputs
        for product in inputs:
            # tell the product i'm interested in its state
            product.pyre_addInputBinding(factory=self)
            # and notify my monitor
            monitor.addInputBinding(factory=self, product=product)
        # all done
        return self


    def pyre_unbindInputs(self, *inputs):
        """
        Unbind me to the sequence of products in {inputs}
        """
        # get my status monitor
        monitor = self.pyre_status
        # go through each of my inputs
        for product in inputs:
            # tell the product i'm interested in its state
            product.pyre_removeInputBinding(factory=self)
            # and notify my monitor
            monitor.removeInputBinding(factory=self, product=product)
        # all done
        return self


    def pyre_bindOutputs(self, *outputs):
        """
        Bind me to the sequence of products in {outputs}
        """
        # get my status monitor
        monitor = self.pyre_status
        # go through the products
        for product in outputs:
            # tell the product i'm its factory
            product.pyre_addOutputBinding(factory=self)
            # and notify my monitor
            monitor.addOutputBinding(factory=self, product=product)
        # all done
        return self


    def pyre_unbindOutputs(self, *outputs):
        """
        Unbind me to the sequence of products in {outputs}
        """
        # get my status monitor
        monitor = self.pyre_status
        # go through the products
        for product in outputs:
            # tell the product i'm not its factory any more
            product.pyre_removeOutputBinding(factory=self)
            # and notify my monitor
            monitor.removeOutputBinding(factory=self, product=product)
        # all done
        return self


    # framework hooks
    def pyre_traitModified(self, trait, new, old):
        """
        Hook invoked when a trait changes value
        """
        # evaluate
        newValue = new.value
        oldValue = old.value
        # if {trait} is an input
        if trait.input:
            # if {oldValue} is non-trivial
            if oldValue is not None:
                # remove from my input pile
                self.pyre_unbindInputs(oldValue)
            # if {newValue} is non-trivial
            if newValue is not None:
                # add it to my pile of inputs
                self.pyre_bindInputs(newValue)

        # if {trait} is an output
        if trait.output:
            # if {oldValue} is non-trivial
            if oldValue is not None:
                # ask it to forget me
                self.pyre_unbindOutputs(oldValue)
            # if {newValue} is non-trivial
            if newValue is not None:
                # tell it i'm one of its factories
                self.pyre_bindOutputs(newValue)
        # chain up
        return super().pyre_traitModified(trait=trait, new=new, old=old)


    # private data
    pyre_inputTraits = ()
    pyre_outputTraits = ()


# end of file
