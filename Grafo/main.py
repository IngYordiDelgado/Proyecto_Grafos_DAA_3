from parser_writer import guardar_grafo
from parser_writer import mostrar_grafo
from grafo import Grafo
"""""
# Generamos grafo de mallas con 30 nodos
grafo_malla_30 = Grafo(dirigido=False)
grafo_malla_30.grafo_malla(5, 6)
#mostrar_grafo(grafo_malla_30)
guardar_grafo(grafo_malla_30, "grafo_malla_30_nodos")
guardar_grafo(grafo_malla_30.Dijkstra("0"),"grafo_malla_30_nodos_Dijkstra")
"""""
"""""
# Generamos grafo de mallas con 500 nodos
grafo_malla_500 = Grafo(dirigido=False)
grafo_malla_500.grafo_malla(50, 10)
guardar_grafo(grafo_malla_500, "grafo_malla_500_nodos")
guardar_grafo(grafo_malla_500.Dijkstra("1"), "grafo_malla_500_nodos_Dijkstra")
"""

"""""
# Generamos grafo Erdös y Rényi con 30 nodos y 200 aristas
grafo_erdos_30_200 = Grafo(dirigido=False)
grafo_erdos_30_200.grafo_erdos_renyi(30, 200)
guardar_grafo(grafo_erdos_30_200, "grafo_erdos_30_200")
guardar_grafo(grafo_erdos_30_200.Dijkstra("1"), "grafo_erdos_30_200_Dijkstra")

# Generamos grafo Erdös y Rényi con 500 nodos y 2500 aristas
grafo_erdos_500_2500 = Grafo(dirigido=False)
grafo_erdos_500_2500.grafo_erdos_renyi(500, 2500)
guardar_grafo(grafo_erdos_500_2500, "grafo_erdos_500_2500")
guardar_grafo(grafo_erdos_500_2500.Dijkstra("1"),"grafo_erdos_500_2500_Dijkstra")
"""""
"""""
# generamos grafo con modelo de Gilbert 30 nodos y probabilidad 0.5
grafo_gilbert_30_05 = Grafo(dirigido=False)
grafo_gilbert_30_05.grafo_gilbert(30, 0.5)
guardar_grafo(grafo_gilbert_30_05, "grafo_gilbert_30_05")
guardar_grafo(grafo_gilbert_30_05.Dijkstra("1"),"grafo_gilbert_30_05_Dijkstra")
# generamos grafo con modelo de Gilbert 500 nodos y probabilidad 0.02
grafo_gilbert_500_002 = Grafo(dirigido=False)
grafo_gilbert_500_002.grafo_gilbert(500, 0.02)
guardar_grafo(grafo_gilbert_500_002, "grafo_gilbert_500_002")
guardar_grafo(grafo_gilbert_500_002.Dijkstra("1"),"grafo_gilbert_500_002_Dijkstra")

# generamos grafo con modelo geográfico simple con 30 nodos y r=0.5
grafo_geografico_30_05 = Grafo(dirigido=False)
grafo_geografico_30_05.grafo_geografico(30, 0.5)
guardar_grafo(grafo_geografico_30_05, "grafo_geografico_30_05")
guardar_grafo(grafo_geografico_30_05.Dijkstra("1"), "grafo_geografico_30_05_Dijkstra")
# generamos grafo con modelo geográfico simple con 500 nodos y r=0.1
grafo_geografico_500_01 = Grafo(dirigido=False)
grafo_geografico_500_01.grafo_geografico(500, 0.15)
guardar_grafo(grafo_geografico_500_01, "grafo_geografico_500_01")
guardar_grafo(grafo_geografico_500_01.Dijkstra("1"), "grafo_geografico_500_01_Dijkstra")
"""""
"""""
# generamos grafo con modelo Barabási-Albert con 30 nodos y grado 10
grafo_babarasi_30_10 = Grafo(dirigido=False)
grafo_babarasi_30_10.grafo_barabasi_albert(30, 10, False, False)
guardar_grafo(grafo_babarasi_30_10, "grafo_babarasi_30_10")
guardar_grafo(grafo_babarasi_30_10.Dijkstra("1"), "grafo_babarasi_30_10_Dijkstra")
# generamos grafo con modelo Barabási-Albert con 500 nodos y grado 12
grafo_babarasi_500_12 = Grafo(dirigido=False)
grafo_babarasi_500_12.grafo_barabasi_albert(500, 15)
guardar_grafo(grafo_babarasi_500_12, "grafo_babarasi_500_12")
guardar_grafo(grafo_babarasi_500_12.Dijkstra("1"), "grafo_babarasi_500_12_Dijkstra")
"""
# generamos grafo con modelo Dorogovtsev-Mendes con 30 nodos
grafo_dorogovtsev_mendes_30 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_30.dorogovtsev_mendes(30)
guardar_grafo(grafo_dorogovtsev_mendes_30, "grafo_dorogovtsev_mendes_30")
guardar_grafo(grafo_dorogovtsev_mendes_30.Dijkstra("1"), "grafo_dorogovtsev_mendes_30_Dijkstra")
# generamos grafo con modelo Dorogovtsev-Mendes con 500 nodos
grafo_dorogovtsev_mendes_500 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_500.dorogovtsev_mendes(500)
guardar_grafo(grafo_dorogovtsev_mendes_500, "grafo_dorogovtsev_mendes_500")
guardar_grafo(grafo_dorogovtsev_mendes_500.Dijkstra("1"), "grafo_dorogovtsev_mendes_500_Dijkstra")



