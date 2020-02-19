import networkx as nx
import matplotlib.pyplot as plt
# G = nx.Graph()
# G.add_node(1)
# G.add_nodes_from([2,3])
# H = nx.path_graph(10)
# G.add_nodes_from(H)
#
# G.add_edge(1, 2)
# e = (2, 3)
# G.add_edge(*e)
# G.add_edges_from([(1, 2), (1, 3)])
# print(G.number_of_nodes())
# print(list(G.nodes))
# print(list(G.edges))
# print(list(G.adj[1]))
# # nx.drawing(G)
# # plt.show()

G = nx.path_graph(8)
nx.draw(G)
plt.show()