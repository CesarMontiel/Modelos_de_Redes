import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_weighted_edges_from([('A','B',5),('A','C',2),('C','D',3),('B','D',1)])

pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G,'weight')
nx.draw(G,pos,with_labels=True,node_size=3000)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

ruta = nx.shortest_path(G,source='A',target='D',weight='weight')
distancia = nx.shortest_path_length(G,source='A',target='D',weight='weight')
print(ruta)
print(distancia)