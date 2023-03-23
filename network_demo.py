import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

import plotly.graph_objects as go

edge_df = pd.read_csv('edge_list.csv')
print(edge_df)

# Convert your dataframe to graph
G = nx.from_pandas_edgelist(edge_df, edge_attr=True)

# Generate the layout and set the 'pos' attribute
#pos = nx.drawing.layout.spring_layout(G)
#nx.set_node_attributes(G, pos, 'pos')

'''
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)
'''

nx.write_gexf(G, "test.gexf")
