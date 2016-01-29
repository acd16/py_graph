#!/usr/bin/env python

"""
Clone of 2048 game.
"""

GRAPH_LIST = [{0: set([1, 2]),
               1: set([]),
               2: set([])
            }, 

    {0: set([1, 4, 5]),
        1: set([2, 6]),
        2: set([3]),
        3: set([0]),
        4: set([1]),
        5: set([2]),
        6: set([])
        }, 

    {0: set([1, 4, 5]),
        1: set([2, 6]),
        2: set([3, 7]),
        3: set([7]),
        4: set([1]),
        5: set([2]),
        6: set([]),
        7: set([3]),
        8: set([1, 2]),
        9: set([0, 3, 4, 5, 6, 7])
        }
    ]

EX_GRAPH0 = GRAPH_LIST[0]
EX_GRAPH1 = GRAPH_LIST[1]
EX_GRAPH2 = GRAPH_LIST[2]

def make_complete_graph(num_nodes):
    """
    Function that creates a completely connected graph.
    """
    grph = {}
    if num_nodes > 0:
        for dummy_i in range(num_nodes):
            edges = set()
            edges.update(range(0, dummy_i))
            edges.update(range(dummy_i+1, num_nodes))
            grph[dummy_i] = edges 
    return grph

def compute_in_degrees(digraph):
    """
    Function that computes the in-degrees of all nodes.
    """
    deg_dis = {}
    for key in digraph.keys():
        for val in digraph[key]:
            if val in deg_dis:
                deg_dis[val] += 1
            else:
                deg_dis[val] = 1
        if not deg_dis.has_key(key):
            deg_dis[key] = 0
    return deg_dis

def in_degree_distribution(digraph):
    """
    Function that computes the in-degree distribution of the graph.
    """
    deg_nor = compute_in_degrees(digraph)
    deg_dis = {}
    for val in deg_nor.values():
        if val in deg_dis:
            deg_dis[val] += 1
        else:
            deg_dis[val] = 1
    return deg_dis


# print make_complete_graph(6)

print compute_in_degrees(GRAPH_LIST[1])
print in_degree_distribution(GRAPH_LIST[1])
