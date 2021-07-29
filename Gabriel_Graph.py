import math
import numpy as np
from scipy.spatial import distance
import networkx as nx
import matplotlib.pyplot as plt

def gg(G):
    for u in G.nodes():
        for v in G.nodes():
            if u != v:  # it avoids loop u -> u
                U_V = distance.euclidean(u, v)
                short = True

                for w in G.nodes():
                    if w != u and w != v:
                        x_center = (u[0] + v[0]) / 2  # half-distance
                        y_center = (u[1] + v[1]) / 2

                        if math.sqrt((w[0] - x_center) ** 2 + (w[1] - y_center) ** 2) < U_V / 2:
                            short = False
                            break

                if short == True:
                    G.add_edge(u, v)

if __name__ == '__main__':
    # generate some random coordinates
    coordinates = np.random.rand(20, 2)

    G = nx.Graph()
    for x, y in coordinates:
        G.add_node((x, y), x=x, y=y)

    gg(G)

    # draw the graph G

    pos = {n: (n[0], n[1]) for n in G.nodes()}
    nx.draw_networkx_nodes(G, pos=pos, node_shape="*", node_color='r')
    nx.draw_networkx_edges(G, pos=pos)

    plt.show()
