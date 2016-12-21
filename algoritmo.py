from model import KPI
from dimension_producto import get_dimension_product
from dimension_vendedor import get_dimension_vendedor
from model import Restriction
import sys


def get_initial_hierarchies(dimension_list, kpi):
    lista = []

    for dimension in dimension_list:
        dimension.graph.initialize_kpi(kpi)
        lista_hierarchies_dimension = dimension.graph.get_hierarchies(1)
        lista.append(lista_hierarchies_dimension)

    return lista


def find_restriction_by_dimension(dimension_name, restrictions):
    for restriction in restrictions:
        if restriction.dimension_name == dimension_name:
            return True
    return False


def add_restriction(dimension_list, hierarchy_list, index_worst_dimension, index_worst_hierarchy, restrictions):

    peor_dimension = dimension_list[index_worst_dimension]
    jerarquia_elegida= hierarchy_list[index_worst_dimension][index_worst_hierarchy]
    peor_instancia = jerarquia_elegida.get_worst_instance()
    restriccion = Restriction(peor_dimension.name, jerarquia_elegida.name, peor_instancia.name)
    restrictions.append(restriccion)

    il = peor_instancia.current_value/(jerarquia_elegida.target_value/len(jerarquia_elegida.instances))

    return il


def dilldrown(dimension_list, index_worst_dimension, hierarchy_list, index_worst_hierarchy):

    i=0
    lista = []
    dimension_elegida = dimension_list[index_worst_dimension]

    for hierarchies_list_by_dimension in hierarchy_list:

        if(i==index_worst_dimension):

            new_hierarchies = dimension_elegida.graph.get_next_hierarchies(hierarchy_list[index_worst_dimension][index_worst_hierarchy]);
            if(len(new_hierarchies) == 0):
                del dimension_list[index_worst_dimension]
            else:
                lista.append(new_hierarchies)

        else:
            lista.append(hierarchies_list_by_dimension)

        i += 1

    return lista


def init():

    dimension_producto = get_dimension_product()
    dimension_vendedor = get_dimension_vendedor()
    dimension_list = [dimension_producto, dimension_vendedor]

    kpi = KPI(90000, 40000, 30000)
    lista_kpi = [kpi]

    IL_th = 0.1

    for kpi in lista_kpi:
        # [(j11, j12], (j21, j22)]
        hierarchies_list_by_dimension = get_initial_hierarchies(dimension_list, kpi)
        IL = 0
        restrictions = []

        while(IL < IL_th and len(hierarchies_list_by_dimension) > 0):
            IG = -sys.maxsize
            index_worst_dimension = -1
            i_d = -1

            for hierarchies_list in hierarchies_list_by_dimension:

                i_d += 1
                index_worst_hierarchy = -1
                j_h = -1

                for hierarchy in hierarchies_list:

                    j_h += 1
                    ig_candidate = hierarchy.get_IG_value()
                    if(ig_candidate > IG):
                        IG = ig_candidate
                        index_worst_dimension = i_d
                        index_worst_hierarchy = j_h

            il_restriction = add_restriction(dimension_list, hierarchies_list_by_dimension, index_worst_dimension, index_worst_hierarchy, restrictions)
            hierarchies_list_by_dimension = dilldrown(dimension_list, index_worst_dimension, hierarchies_list_by_dimension, index_worst_hierarchy)
            IL = IL + il_restriction

    print(restrictions)
init()