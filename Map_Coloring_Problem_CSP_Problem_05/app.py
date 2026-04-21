import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def is_safe(node, color, assignment, graph):
    """Check if any adjacent nodes have the same color."""
    for neighbor in graph.get(node, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(nodes, colors, assignment, graph):
    """CSP Backtracking algorithm."""
    if len(assignment) == len(nodes):
        return assignment

    unassigned = [n for n in nodes if n not in assignment]
    node = unassigned[0]

    for color in colors:
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(nodes, colors, assignment, graph)
            if result:
                return result
            # Backtrack
            del assignment[node]
    return None

# Streamlit UI
st.title("🎨 AI Map Coloring Solver (CSP)")
st.sidebar.header("Configuration")

# 1. Input Regions
regions_input = st.sidebar.text_input("Enter Regions (comma separated)", "A, B, C, D")
nodes = [r.strip() for r in regions_input.split(",")]

# 2. Input Adjacency
adj_input = st.sidebar.text_area("Enter Adjacency (e.g., A-B, B-C)", "A-B, A-C, B-C, B-D, C-D")
edges = []
graph = {node: [] for node in nodes}

if adj_input:
    for pair in adj_input.split(","):
        if "-" in pair:
            u, v = pair.split("-")
            u, v = u.strip(), v.strip()
            if u in nodes and v in nodes:
                edges.append((u, v))
                graph[u].append(v)
                graph[v].append(u)

# 3. Select Colors
num_colors = st.sidebar.slider("Number of Colors", 3, 4, 3)
available_colors = ["Red", "Green", "Blue", "Yellow"][:num_colors]

if st.button("Solve Map Coloring"):
    solution = backtrack(nodes, available_colors, {}, graph)
    
    if solution:
        st.success("Solution Found!")
        
        # Display Mapping
        cols = st.columns(len(nodes))
        for i, node in enumerate(nodes):
            cols[i].metric(label=f"Region {node}", value=solution[node])

        # Visualization
        fig, ax = plt.subplots()
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        
        node_colors = [solution[node].lower() for node in G.nodes()]
        
        nx.draw(G, with_labels=True, node_color=node_colors, 
                node_size=2000, font_weight='bold', ax=ax)
        st.pyplot(fig)
    else:
        st.error("No solution exists with the given constraints.")