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
                            FixedTotalNumberConnector, \
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
        syn_params = projection.synapse_parameters()
        rule_params = {'autapses' : self.allow_self_connections,
                      'rule' : 'pairwise_bernoulli',
                      'p' : self.p_connect}
        projection._connect(rule_params, syn_params)

class NewAllToAllConnector() :
    def __init__(self, allow_self_connections=True, safe=True,
                 callback=None):
        self.allow_self_connections = allow_self_connections

    def connect(self,projection) :
        syn_params = projection.synapse_parameters()
        rule_params = {'autapses' : self.allow_self_connections,
                      'rule' : 'all_to_all'}

        projection._connect(rule_params, syn_params)

class NewOneToOneConnector() :
    def __init__(self, allow_self_connections=True, safe=True,
                 callback=None):
        self.allow_self_connections = allow_self_connections

    def connect(self,projection) :
        syn_params = projection.synapse_parameters()
        rule_params = {'autapses' : self.allow_self_connections,
                      'rule' : 'one_to_one'}

        projection._connect(rule_params, syn_params)

class NewFixedNumberPreConnector() :
    def __init__(self, n, allow_self_connections=True, safe=True,
                 callback=None):
        self.allow_self_connections = allow_self_connections
        self.n = n

    def connect(self,projection) :
        syn_params = projection.synapse_parameters()
        rule_params = {'autapses' : self.allow_self_connections,
                       'rule' : 'fixed_in_degree',
                       'indegree' : self.n }

        projection._connect(rule_params, syn_params)

class NewFixedNumberPostConnector() :
    def __init__(self, n, allow_self_connections=True, safe=True,
                 callback=None):
        self.allow_self_connections = allow_self_connections
        self.n = n

    def connect(self,projection) :
        syn_params = projection.synapse_parameters()
        rule_params = {'autapses' : self.allow_self_connections,
                       'rule' : 'fixed_out_degree',
                       'outdegree' : self.n }

        projection._connect(rule_params, syn_params)

class NewFixedTotalNumberConnector() :
    def __init__(self, n, allow_self_connections=True, safe=True,
                 callback=None):
        self.allow_self_connections = allow_self_connections
        self.n = n

    def connect(self,projection) :
        syn_params = projection.synapse_parameters()
        rule_params = {'autapses' : self.allow_self_connections,
                       'rule' : 'fixed_total_number',
                       'N' : self.n
                   }

        projection._connect(rule_params, syn_params)
