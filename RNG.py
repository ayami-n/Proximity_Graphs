import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial import distance


def RNG(G):
    """Insert edges according to the RNG rules into the graph G"""
    for c1 in G.nodes():
        for c2 in G.nodes():
            d = distance.euclidean(c1, c2)
            for possible_blocker in G.nodes():
                distToC1 = distance.euclidean(possible_blocker, c1)
                distToC2 = distance.euclidean(possible_blocker, c2)
                if distToC1 < d and distToC2 < d:
                    # this node is in the lune and blocks
                    break
            else:
                G.add_edge(c1, c2)


if __name__ == "__main__":
    # generate some random coordinates
    coordinates = np.random.rand(10, 2)
    G = nx.Graph()
    for x, y in coordinates:
        G.add_node((x, y), x=x, y=y)

    RNG(G)
    # GG(G)
    # draw the graph G
    pos = {n: (n[0], n[1]) for n in G.nodes()}
    nx.draw_networkx_nodes(G, pos=pos, node_shape="*")
    nx.draw_networkx_edges(G, pos=pos)

    plt.show()

