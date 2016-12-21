from model import Instance
from model import Hierarchy
from model import GraphDAG
from model import Dimension


def get_dimension_product():

    instancia_opel_corsa = Instance("Opel Corsa", 2200)
    instancia_opel_adam = Instance("Opel Adam", 300)
    instancia_opel_astra = Instance("Opel Astra", 4000)
    instancia_opel_vectra = Instance("Opel Vectra", 2500)
    instancia_opel_vivaro = Instance("Opel Vivaro", 3500)

    instancia_mercedes_clasea = Instance("Mercedes Clase A", 2000)
    instancia_mercedes_claseb = Instance("Mercedes Clase B", 500)
    instancia_mercedes_clasee = Instance("Mercedes Clase E", 3000)
    instancia_mercedes_clases = Instance("Mercedes Clase S", 500)
    instancia_mercedes_vito = Instance ("Mercedes Vito", 1500)

    instancia_bmw_serie1 = Instance("BMW Serie 1", 11000)
    instancia_bmw_serie2 = Instance("BMW Serie 2", 9000)
    instancia_bmw_serie3 = Instance("BMW Serie 3", 15000)
    instancia_bmw_serie5 = Instance("BMW Serie 5", 5000)

    jerarquia_producto = Hierarchy("Producto especifico",
                                   [instancia_opel_corsa, instancia_opel_adam, instancia_opel_astra, instancia_opel_vectra,instancia_opel_vivaro,
                                    instancia_mercedes_clasea, instancia_mercedes_claseb, instancia_mercedes_clasee, instancia_mercedes_clases, instancia_mercedes_vito,
                                    instancia_bmw_serie1, instancia_bmw_serie2, instancia_bmw_serie3, instancia_bmw_serie5])

    instancia_utilitario = Instance("Utilitario", 25000)
    instancia_compacto = Instance("Compacto", 30000)
    jerarquia_segmento = Hierarchy("Segmento", [instancia_utilitario, instancia_compacto])

    instancia_industrial = Instance("Industrial", 5000)
    instancia_personal = Instance("Personal", 55000)
    jerarquia_tipo = Hierarchy("Tipo", [instancia_industrial, instancia_personal])

    instancia_opel = Instance("Opel", 12500)
    instancia_mercedes = Instance("Mercedes", 7500)
    instancia_bmw = Instance("BMW", 40000)
    jerarquia_marca = Hierarchy("Marca", [instancia_opel, instancia_mercedes, instancia_bmw])

    grafo = GraphDAG()
    grafo.add_hierarchy(jerarquia_marca)
    grafo.add_hierarchy(jerarquia_tipo)
    grafo.add_hierarchy(jerarquia_segmento)
    grafo.add_hierarchy(jerarquia_producto)

    grafo.add_edge(jerarquia_marca, jerarquia_segmento)
    grafo.add_edge(jerarquia_marca, jerarquia_tipo)
    grafo.add_edge(jerarquia_tipo, jerarquia_producto)
    grafo.add_edge(jerarquia_segmento, jerarquia_producto)

    return Dimension("Producto", grafo)
