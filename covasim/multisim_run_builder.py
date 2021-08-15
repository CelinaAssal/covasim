from . import run
from abc import ABCMeta, abstractmethod

class IBuilder(metaclass=ABCMeta):

    @abstractmethod
    def run_start(self):
        pass

    @staticmethod
    @abstractmethod
    def build_run(self, reduce=False, combine=False, **kwargs):
        '''
        Run the actual sims

        Args:
            reduce  (bool): whether or not to reduce after running (see reduce())
            combine (bool): whether or not to combine after running (see combine(), not compatible with reduce)
            kwargs  (dict): passed to multi_run(); use run_args to pass arguments to sim.run()

        Returns:
            None (modifies MultiSim object in place)

        **Examples**::

            msim.run()
            msim.run(run_args=dict(until='2020-0601', restore_pars=False))
        '''
        # Handle which sims to use -- same as init_sims()
        if self.sims is None:
            sims = self.base_sim
        else:
            sims = self.sims

        # Run
        kwargs = sc.mergedicts(self.run_args, kwargs)
        self.sims = multi_run(sims, **kwargs)

        # Reduce or combine
        if reduce:
            self.reduce()
        elif combine:
            self.combine()

        return run
    
    @abstractmethod
    def run_complete(self):
        pass


class Builder(IBuilder):
    
    def __init__(self):
        self.product = Product()

    def run_start(self):
        self.product.append("Starting to run...")

    def run_complete(self):
        self.product.append("Run complete.")

    def get_result(self):
        self.product = self.product.build_run()
        return self.product


class Product():

    def __init__(self):
        self.parts = []


class Director:

    @staticmethod
    def construct():
        return IBuilder()\
        .run_start()\
        .build_run()\
        .run_complete()
