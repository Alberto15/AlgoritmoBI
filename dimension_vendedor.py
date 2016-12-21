from model import Instance
from model import Hierarchy
from model import GraphDAG
from model import Dimension

def get_dimension_vendedor():

    instancia_escuela = Instance("Estudios primarios", 3000)
    instancia_instituto = Instance("Estudios secundarios", 30000)
    instancia_formacion_profesional = Instance("Estudios en formación profesional", 20000)
    instancia_universidad = Instance("Estudios universitarios", 5000)
    instancia_master = Instance("Estudios de postgrado", 2000)

    jerarquia_estudios = Hierarchy("Estudios", [instancia_escuela, instancia_instituto, instancia_formacion_profesional, instancia_universidad, instancia_master])

    instancia_nacionalidad_espanyola = Instance("Española", 7000)
    instancia_nacionalidad_italiana = Instance("Italiana", 4000)
    instancia_nacionalidad_francesa = Instance("Francesa", 5000)
    instancia_nacionalidad_alemana = Instance("Alemana", 12500)
    instancia_nacionalidad_inglesa = Instance("Inglesa", 6000)
    instancia_nacionalidad_holandesa = Instance("Holandesa", 1000)
    instancia_nacionalidad_canadiense = Instance("Canadiense", 3000)
    instancia_nacionalidad_chilena = Instance("Chilena", 500)
    instancia_nacionalidad_mexicana = Instance("Mexicana", 800)
    instancia_nacionalidad_japonesa = Instance("Japonesa", 3500)
    instancia_nacionalidad_singapurense = Instance("Singapurense", 600)
    instancia_nacionalidad_china = Instance("China", 12000)
    instancia_nacionalidad_taiwanesa = Instance("Taiwanesa", 100)
    instancia_nacionalidad_luxemburguesa = Instance("Luxemburguesa", 1500)
    instancia_nacionalidad_belga = Instance("Belga", 2500)

    jerarquia_nacionalidad = Hierarchy("Nacionalidad",
                                       [instancia_nacionalidad_espanyola, instancia_nacionalidad_italiana, instancia_nacionalidad_francesa,
                                        instancia_nacionalidad_alemana, instancia_nacionalidad_inglesa, instancia_nacionalidad_holandesa,
                                        instancia_nacionalidad_canadiense, instancia_nacionalidad_chilena, instancia_nacionalidad_mexicana,
                                        instancia_nacionalidad_japonesa, instancia_nacionalidad_singapurense, instancia_nacionalidad_china,
                                        instancia_nacionalidad_taiwanesa, instancia_nacionalidad_luxemburguesa, instancia_nacionalidad_belga])

    instancia_hombre = Instance("Hombre", 20000)
    instancia_mujer = Instance("Mujer", 40000)
    jerarquia_sexo = Hierarchy("Sexo", [instancia_hombre, instancia_mujer])

    instancia_sinexperiencia = Instance("Sin experiencia", 2000)
    instancia_menosde3anyos = Instance("Menos de 3 años", 3000)
    instancia_3a5 = Instance("De 3 a 5 años", 7000)
    instancia_5a10 = Instance("De 5 a 10 años", 6000)
    instancia_10a15 = Instance("De 10 a 15 años", 12000)
    instancia_15a20 = Instance("De 15 a 20 años", 15000)
    instancia_masde20anyos = Instance("Más de 20 años", 15000)

    jerarquia_experiencia = Hierarchy("Experiencia", [instancia_sinexperiencia, instancia_menosde3anyos, instancia_3a5,
                                                      instancia_5a10, instancia_10a15, instancia_15a20, instancia_masde20anyos])


    instancia_antonio = Instance("Antonio", 1000)
    instancia_alberto = Instance("Alberto", 2000)
    instancia_alfredo = Instance("Alfredo", 2500)
    instancia_roman = Instance("Roman", 500)
    instancia_fran = Instance("Fran", 300)
    instancia_akram = Instance("Akram", 800)
    instancia_manu = Instance("Manu", 600)
    instancia_mario = Instance("Mario", 900)
    instancia_jose = Instance("Jose", 2000)
    instancia_juan = Instance("Juan", 500)
    instancia_ferran = Instance("Ferran", 1500)
    instancia_alvaro = Instance("Alvaro", 2500)
    instancia_joan = Instance("Joan", 300)
    instancia_carlos = Instance("Carlos", 200)
    instancia_aitor = Instance("Aitor", 50)
    instancia_david = Instance("David", 100)
    instancia_edgar = Instance("Edgar", 20)
    instancia_cesar = Instance("Cesar", 300)
    instancia_lucas = Instance("Lucas", 200)
    instancia_pablo = Instance("Pablo", 150)
    instancia_jorge = Instance("Jorge", 170)
    instancia_diego = Instance("Diego", 310)
    instancia_victor = Instance("Victor", 220)
    instancia_tomas = Instance("Tomas", 1000)
    instancia_marcelo = Instance("Marcelo", 1880)

    instancia_maria = Instance("Maria", 4000)
    instancia_carolina = Instance("Carolina", 6000)
    instancia_severiana = Instance("Severiana", 2000)
    instancia_lucia = Instance("Lucía", 300)
    instancia_lydia = Instance("Lydia", 3500)
    instancia_judith = Instance("Judith", 2500)
    instancia_marta = Instance("Marta", 4200)
    instancia_encarna = Instance("Encarna", 3200)
    instancia_ana = Instance("Ana", 2100)
    instancia_sheila = Instance("Sheila", 3500)
    instancia_claudia = Instance("Claudia", 4000)
    instancia_andrea = Instance("Andrea", 2000)
    instancia_carmen = Instance("Carmen", 100)
    instancia_rocio = Instance("Rocío", 400)
    instancia_natalia = Instance("Natalia", 600)
    instancia_veronica = Instance("Verónica", 1600)

    jerarquia_vendedor_especifico = Hierarchy("Vendedor Específico", [instancia_antonio, instancia_alberto, instancia_alfredo, instancia_roman,
                                                                      instancia_fran, instancia_akram, instancia_manu, instancia_mario,
                                                                      instancia_jose, instancia_juan, instancia_ferran, instancia_alvaro,
                                                                      instancia_joan, instancia_carlos, instancia_aitor, instancia_david,
                                                                      instancia_edgar, instancia_cesar, instancia_lucas, instancia_pablo,
                                                                      instancia_jorge, instancia_diego, instancia_victor, instancia_tomas,
                                                                      instancia_marcelo, instancia_maria, instancia_carolina, instancia_severiana,
                                                                      instancia_lucia, instancia_lydia, instancia_judith, instancia_marta,
                                                                      instancia_encarna, instancia_ana, instancia_sheila, instancia_claudia,
                                                                      instancia_andrea, instancia_carmen, instancia_rocio, instancia_natalia,
                                                                      instancia_veronica])

    grafo = GraphDAG()
    grafo.add_hierarchy(jerarquia_nacionalidad)
    grafo.add_hierarchy(jerarquia_sexo)
    grafo.add_hierarchy(jerarquia_experiencia)
    grafo.add_hierarchy(jerarquia_estudios)
    grafo.add_hierarchy(jerarquia_vendedor_especifico)

    grafo.add_edge(jerarquia_nacionalidad, jerarquia_estudios)
    grafo.add_edge(jerarquia_estudios, jerarquia_vendedor_especifico)
    grafo.add_edge(jerarquia_sexo, jerarquia_vendedor_especifico)
    grafo.add_edge(jerarquia_experiencia, jerarquia_vendedor_especifico)

    return Dimension("Vendedores", grafo)