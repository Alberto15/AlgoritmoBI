from collections import OrderedDict
from copy import deepcopy
import sys

class Dimension(object):
    def __init__(self, name, graph):
        self.name = name
        self.graph = graph

class Restriction(object):
    def __init__(self, dimension_name, hierarchy_name, worst_instance):
        self.dimension_name = dimension_name
        self.hierarchy_name = hierarchy_name
        self.worst_instance = worst_instance

class KPI(object):
    def __init__(self, target_value, thresold_value, worst_value):
        self.target_value = target_value
        self.thresold_value = thresold_value
        self.worst_value = worst_value

class Instance(object):
    def __init__(self, name, current_value):
        self.name = name
        self.current_value = current_value

class Hierarchy(object):
    def __init__(self, name, instances):
        self.name = name
        self.instances = instances
        self.nivel = 1
        self.target_value = 0

    def get_IG_value(self):

        target_instance = self.target_value/len(self.instances)
        max = -sys.maxsize
        min = sys.maxsize

        for instance in self.instances:
            deviation = target_instance - instance.current_value

            if deviation > max:
                max = deviation
            if deviation < min:
                min = deviation

        return (max - min)/target_instance

    def print(self):

        instances_str = "("
        i = 0
        len_instances = len(self.instances)
        for instance in self.instances:
            i += 1

            if(len_instances == i):
                instances_str += instance.name + " - " + str(instance.current_value) + ")"
            else:
                instances_str += instance.name + " - " + str(instance.current_value) + ","

        print("[" + self.name + ", " + instances_str + "]")


    def get_worst_instance(self):

        target_instance = self.target_value / len(self.instances)
        max = -sys.maxsize
        worst_instance = Instance("",-1)

        for instance in self.instances:
            deviation = target_instance - instance.current_value

            if deviation > max:
                max = deviation
                worst_instance = deepcopy(instance)

        return worst_instance

class GraphDAG(object):
    def __init__(self):
        self.graph = OrderedDict()


    def is_hierarchy_in_graph(self, hierarchy_to_find):
        for hierarchy, v in self.graph.items():
            if(hierarchy_to_find.name == hierarchy.name):
                return True
        return False

    def add_hierarchy(self, hierarchy):
        """ Add a node if it does not exist yet, or error out. """
        #if node in graph:
        #    raise KeyError('node %s already exists' % node)
        self.graph[hierarchy] = set()


    def print(self):
        for hierarchy, v in self.graph.items():
            hierarchy.print()


    def add_edge(self, hierarchy_top, hierarchy_down):
        #    """ Add an edge (dependency) between the specified nodes. """
        if (self.is_hierarchy_in_graph(hierarchy_top) is False) or (self.is_hierarchy_in_graph(hierarchy_down) is False):
           raise KeyError('one or more nodes do not exist in graph')

        self.graph[hierarchy_top].add(hierarchy_down)
        if(hierarchy_top.nivel + 1 > hierarchy_down.nivel):
            hierarchy_down.nivel = hierarchy_top.nivel + 1


    def initialize_kpi(self, kpi):
        for hierarchy, v in self.graph.items():
                hierarchy.target_value = kpi.target_value


    def find_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        if self.is_hierarchy_in_graph(start) is False:
            return None
        for node in self.graph[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path

        return None

    def get_hierarchies(self, nivel):
        lista = []

        for hierarchy, v in self.graph.items():
            if hierarchy.nivel == nivel:
                lista.append(hierarchy)

        return lista

    def get_next_hierarchies(self, start):
        hierarchies_next_level = []
        for node in self.graph[start]:
            node.target_value
            hierarchies_next_level.append(node)

        return hierarchies_next_level



