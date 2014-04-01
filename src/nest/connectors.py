"""
Connection method classes for nest

:copyright: Copyright 2006-2013 by the PyNN team, see AUTHORS.
:license: CeCILL, see LICENSE for details.

"""

from pyNN import random, core, errors
from pyNN.connectors import Connector, \
                            AllToAllConnector, \
                            DistanceDependentProbabilityConnector, \
                            DisplacementDependentProbabilityConnector, \
                            IndexBasedProbabilityConnector, \
                            FixedNumberPreConnector, \
                            FixedNumberPostConnector, \
                            OneToOneConnector, \
                            SmallWorldConnector, \
                            FromListConnector, \
                            FromFileConnector, \
                            CSAConnector, \
                            CloneConnector, \
                            ArrayConnector,\
                            FixedProbabilityConnector


class NewFixedProbabilityConnector() :
    def __init__(self, p_connect, allow_self_connections=True,
                 rng=None, safe=True, callback=None): 
        self.allow_self_connections = allow_self_connections
        self.p_connect = float(p_connect)
#        self.rng = _get_rng(rng)


    def connect(self, projection) :
        params = projection.transform_parameters()
        params.update({'autapses' : self.allow_self_connections,
                      'rule' : 'pairwise_bernoulli',
                      'p' : self.p_connect})

        projection._connect(params = params)

