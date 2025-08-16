import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
# --- 1. Synthetic Data Generation ---
# Number of countries
num_countries = 20
# Generate random GDP growth rates
np.random.seed(42) # for reproducibility
gdp_growth = np.random.uniform(0.01, 0.05, num_countries)
# Generate random trade flows (adjacency matrix)
trade_flows = np.random.randint(0, 100, size=(num_countries, num_countries))
# Ensure diagonal is zero (no self-trade)
np.fill_diagonal(trade_flows, 0)
# Make it symmetric to represent bilateral trade
trade_flows = np.triu(trade_flows) + np.triu(trade_flows, 1).T
# Create pandas DataFrame
countries = [f'Country {i+1}' for i in range(num_countries)]
df = pd.DataFrame(trade_flows, index=countries, columns=countries)
df['GDP Growth'] = gdp_growth
# --- 2. Data Cleaning and Analysis (Minimal in this synthetic example) ---
# (In a real-world scenario, this section would involve more extensive data cleaning and preprocessing)
# --- 3. Visualization ---
# Create a network graph using NetworkX
G = nx.from_numpy_array(trade_flows)
nx.set_node_attributes(G, dict(zip(range(num_countries), gdp_growth)), 'gdp_growth')
# Node sizes based on GDP growth
node_sizes = [v['gdp_growth'] * 1000 for v in G.nodes(data=True)]
# Edge widths based on trade flow values
edge_widths = [df.iloc[u,v] for u,v in G.edges()]
# Draw the graph
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G) # You can experiment with different layouts
nx.draw(G, pos, with_labels=True, node_size=node_sizes, width=edge_widths, node_color=node_sizes, cmap=plt.cm.viridis)
plt.title('Global Economic Interdependencies: Trade Flows and GDP Growth')
plt.colorbar(label='GDP Growth Rate')
plt.savefig('global_economic_network.png')
print("Plot saved to global_economic_network.png")
#Further analysis could involve community detection or centrality measures