import random
from typing import Dict

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

def draw_graph(colorings , G):
    n = len(colorings)
    
    cols = min(4, n)              # max 4 graphs per row
    rows = int(np.ceil(n / cols))
    
    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(5 * cols, 5 * rows)
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