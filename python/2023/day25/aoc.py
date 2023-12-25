import re

import networkx as ne

if __name__ == "__main__":
    con, rg = [], []
    graph = ne.Graph()
    lines = open("input.txt").read().strip().split("\n")

    for line in lines:
        con.append(re.findall("\w+", line))

    for c in con:
        for n in c[1:]:
            graph.add_edge(c[0], n)

    for ec in ne.minimum_edge_cut(graph):
        graph.remove_edge(ec[0], ec[1])

    for cc in ne.connected_components(graph):
        rg.append(cc)

    assert len(rg) == 2, "Data input error"
    print(f"Result:{len(rg[0]) * len(rg[1])}")
