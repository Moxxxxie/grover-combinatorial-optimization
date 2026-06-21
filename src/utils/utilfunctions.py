import random
from typing import Dict
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

palette = [
    "red",
    "green",
    "blue",
    "yellow",
    "purple",
    "orange",
    "cyan",
    "pink"
]


def graphGen(n:int)-> Dict[int, set]:
    MaxnumEdge = n * (n-1)//2
    numEdge = random.randint(0 , MaxnumEdge)
    nodes = [i for i in range(n)]
    graph = {i:set() for i in range(n)}
    for i in range(numEdge):
        connection = random.sample(nodes , k=2)
        graph[connection[0]].add(connection[1])
        graph[connection[1]].add(connection[0])
    return graph



def availableColors(color:list , usedColor:list) -> int:
    I = -1
    minV = 1000
    availindex = {}
    for i in range(len(usedColor)):
        if usedColor[i] == 0:
            availindex[i] = color[i]
            if color[i] < minV:
                I = i
                minV = color[i]
    return I


def greedy(n , graph):
    colorsDB = {i:-1 for i in range(n)}
    color = [0]
    for node in range(n):
        usedColor = [0 for i in range(len(color))]
        for andj in graph[node]:
            c = colorsDB[andj]
            if c != -1:
                usedColor[c] = 1
        a = availableColors(color , usedColor)
        if a < 0:
            color.append(0)
            a = len(color)-1
        color[a] += 1
        colorsDB[node] = a
    return colorsDB , color


def toint(n) :
    num = 0
    for i in range(len(n)):        
        num += int(n[len(n) - i- 1]) * 2 ** (i)
    return num


def get_edges(graph):
    edges = set()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            edge = tuple(sorted((node, neighbor)))
            edges.add(edge)
    return list(edges)


def draw_graph(colorings , G , pos):
    # pos = nx.spring_layout(G, seed=42)
    n = len(colorings)
    
    cols = min(4, n)              # max 4 graphs per row
    rows = int(np.ceil(n / cols))
    
    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(3 * cols, 3 * rows)
    )
    
    # Makes indexing easier when rows/cols = 1
    axes = np.array(axes).reshape(-1)
    
    for i, colorsDB in enumerate(colorings):
    
        node_colors = [
            palette[colorsDB[node] % len(palette)]
            for node in G.nodes()
        ]
    
        nx.draw(
            G,
            pos,
            ax=axes[i],
            with_labels=True,
            node_color=node_colors,
            node_size=800,
            edgecolors="black",
            arrows=False
        )
    
        axes[i].set_title(f"Solution {i+1}")
    
    # Hide unused axes
    for j in range(len(colorings), len(axes)):
        axes[j].axis("off")
    
    plt.tight_layout()
    plt.show()



def draw_simple_graph( G,pos):
    plt.figure(figsize=(3,3))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=800,
        arrows=False
    )



def get_graph(graph):
    G = nx.DiGraph()
    for node , Neighbors in graph.items():
        for i in Neighbors:
            G.add_edge(node,i)
    return G



def get_pos(G):
    return nx.spring_layout(G, seed=42)



def factor(N):
    fac = 1
    for i in range(1, N+1):
        fac *= i
    return fac


def translator(N, K, counts):
    colors = []
    for seq, _ in counts.items():
        seq = seq[::-1]             
        colorsample = {}
        for n in range(N):
            block = seq[n*K:(n+1)*K]
            colorsample[n] = block.index('1')
        colors.append(colorsample)
    return colors


def edge_map(coloring , edges):
    flag = True
    for nodeA , nodeB in list(edges):
        flag = flag and (coloring[nodeA] != coloring[nodeB])
    return flag


def answer_validity(colorings , edges):
    valid_colorings = []
    for coloring in colorings:
        if edge_map(coloring , edges) :
            if coloring not in valid_colorings:
                valid_colorings.append(coloring)
    return valid_colorings