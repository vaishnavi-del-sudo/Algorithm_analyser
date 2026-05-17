import streamlit as st
import heapq
from collections import deque
import pandas as pd

# ==========================================
# SEARCH ALGORITHM IMPLEMENTATIONS
# ==========================================

def bfs(graph, start, goal):
    queue = deque([(start, [start], 0)])
    visited = set()
    while queue:
        node, path, cost = queue.popleft()
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                queue.append((neighbor, path + [neighbor], cost + weight))
    return None, float('inf')

def dfs(graph, start, goal, visited=None, path=None, cost=0):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    if start == goal:
        return path, cost
    visited.add(start)
    for neighbor, weight in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path + [neighbor], cost + weight)
            if result[0] is not None:
                return result
    return None, float('inf')

def astar(graph, heuristic, start, goal):
    if start not in heuristic or goal not in heuristic:
        return None, float('inf')
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return path, g
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                new_g = g + weight
                new_f = new_g + heuristic.get(neighbor, 0)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
    return None, float('inf')

def best_first(graph, heuristic, start, goal):
    if start not in heuristic:
        return None, float('inf')
    pq = [(heuristic[start], start, [start], 0)]
    visited = set()
    while pq:
        h, node, path, cost = heapq.heappop(pq)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                heapq.heappush(pq, (heuristic.get(neighbor, 0), neighbor, path + [neighbor], cost + weight))
    return None, float('inf')

def hill_climbing(graph, heuristic, start, goal):
    current = start
    path = [current]
    cost = 0
    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:
            return None, float('inf')
        
        valid_neighbors = [n for n in neighbors if n[0] in heuristic]
        if not valid_neighbors:
            return None, float('inf')

        next_node = min(valid_neighbors, key=lambda x: heuristic[x[0]])
        if heuristic[next_node[0]] >= heuristic[current]:
            return None, float('inf')

        current = next_node[0]
        cost += next_node[1]
        path.append(current)
    return path, cost

# ==========================================
# STREAMLIT UI CONFIGURATION & STYLING
# ==========================================

st.set_page_config(
    page_title="Pathfinding Matrix AI",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for polished typography and cards
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .section-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2a5298;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Dashboard Header
st.markdown("""
    <div class="main-header">
        <h1 style='margin:0; font-family:sans-serif;'>🧠 Search Algorithm Matrix Benchmarker</h1>
        <p style='margin:10px 0 0; opacity:0.9; font-size:1.1rem;'>
            Design custom network topologies, assign weights, and visualize how classic AI search strategies navigate your graph.
        </p>
    </div>
""", unsafe_allow_html=True)

# Sidebar App Meta Details
with st.sidebar:
    st.image("https://img.icons8.com/fluent/100/000000/network.png", width=80)
    st.title("About the Tool")
    st.info(
        "This platform compares **Uninformed** (BFS, DFS) against **Informed/Heuristic** "
        "(A*, Greedy Best-First, Hill Climbing) AI search variants simultaneously."
    )
    st.caption("Developed with ❤️ using Streamlit Architecture.")

# ==========================================
# CORE DATA INPUT PANELS (COLUMNS)
# ==========================================

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="section-card"><h3>🗺️ 1. Edge Registry Topology</h3><p style="color:gray; font-size:0.9rem;">Configure edges and weights below.</p></div>', unsafe_allow_html=True)
    
    # Pre-populate with a beautifully clean structured default graph
    if "edge_df" not in st.session_state:
        st.session_state.edge_df = pd.DataFrame([
            {"Source": "A", "Destination": "B", "Cost": 2},
            {"Source": "A", "Destination": "C", "Cost": 4},
            {"Source": "B", "Destination": "D", "Cost": 7},
            {"Source": "B", "Destination": "E", "Cost": 3},
            {"Source": "C", "Destination": "E", "Cost": 2},
            {"Source": "D", "Destination": "F", "Cost": 1},
            {"Source": "E", "Destination": "F", "Cost": 5}
        ])
    
    edited_edges = st.data_editor(
        st.session_state.edge_df, 
        num_rows="dynamic", 
        use_container_width=True,
        key="edge_editor"
    )

    # Automatically extract unique nodes dynamically
    all_nodes = sorted(list(set(edited_edges["Source"].dropna().astype(str).str.strip().tolist() + 
                                edited_edges["Destination"].dropna().astype(str).str.strip().tolist())))

with col2:
    st.markdown('<div class="section-card"><h3>🎯 2. Straight-Line Heuristics</h3><p style="color:gray; font-size:0.9rem;">Estimated cost mappings targeting the goal node.</p></div>', unsafe_allow_html=True)
    
    # Establish baseline defaults for nodes
    if "h_df" not in st.session_state or set(all_nodes) != set(st.session_state.h_df["Node"].tolist()):
        default_h = [{"Node": node, "Heuristic Value": 0} for node in all_nodes]
        st.session_state.h_df = pd.DataFrame(default_h)

    edited_heuristics = st.data_editor(
        st.session_state.h_df,
        use_container_width=True,
        key="heuristic_editor",
        disabled=["Node"]
    )

# ==========================================
# LIVE NETWORK GRAPH VISUALIZATION
# ==========================================

st.markdown("### 🖥️ Live Network Topography Preview")
if all_nodes and not edited_edges.empty:
    # Dynamically generate Graphviz DOT notation layout styling
    dot_code = "digraph G {\n"
    dot_code += "  rankdir=LR;\n"
    dot_code += "  node [shape=circle, style=filled, fillcolor=\"#eef2ff\", color=\"#1e3c72\", fontname=\"Helvetica\"];\n"
    dot_code += "  edge [fontname=\"Helvetica\", color=\"#555555\"];\n"
    
    for _, row in edited_edges.iterrows():
        if pd.notna(row["Source"]) and pd.notna(row["Destination"]):
            dot_code += f'  "{row["Source"]}" -> "{row["Destination"]}" [label="{row["Cost"]}"];\n'
    dot_code += "}"
    
    # Render interactive graph
    st.graphviz_chart(dot_code, use_container_width=True)
else:
    st.warning("Please add rows to the Edge Registry topology dataset to render the network map model visualizer.")

st.markdown("---")

# ==========================================
# PROCESSING COMPILATION MATRIX
# ==========================================

st.markdown('<div class="section-card"><h3>⚙️ 3. Execution Parameter Core</h3></div>', unsafe_allow_html=True)
nav_col1, nav_col2, nav_col3 = st.columns([1, 1, 1])

with nav_col1:
    start_node = st.selectbox("🎯 Target Node Context Initiation (Start)", options=all_nodes)
with nav_col2:
    goal_node = st.selectbox("🏁 Target Terminal Destination Focus (Goal)", options=all_nodes, index=len(all_nodes)-1 if all_nodes else 0)
with nav_col3:
    st.write("##")
    run_btn = st.button("🚀 Process Engine Evaluation Matrix", type="primary", use_container_width=True)

# Generate internal data dictionary maps
graph = {node: [] for node in all_nodes}
for _, row in edited_edges.iterrows():
    src, dest, cost = row["Source"], row["Destination"], row["Cost"]
    if pd.notna(src) and pd.notna(dest):
        try:
            graph[str(src).strip()].append((str(dest).strip(), int(cost)))
        except (ValueError, TypeError):
            continue

heuristic = {}
for _, row in edited_heuristics.iterrows():
    node, h_val = row["Node"], row["Heuristic Value"]
    if pd.notna(node):
        try:
            heuristic[str(node).strip()] = int(h_val)
        except (ValueError, TypeError):
            heuristic[str(node).strip()] = 0

# Display results
if run_btn:
    if not start_node or not goal_node:
        st.error("Invalid configuration settings mapping context parameters. Execution halted.")
    else:
        with st.spinner("Crunching analytics matrices..."):
            results = {
                "Breadth-First Search (BFS)": bfs(graph, start_node, goal_node),
                "Depth-First Search (DFS)": dfs(graph, start_node, goal_node),
                "A* Search Algorithm": astar(graph, heuristic, start_node, goal_node),
                "Greedy Best First Search": best_first(graph, heuristic, start_node, goal_node),
                "Hill Climbing Local Search": hill_climbing(graph, heuristic, start_node, goal_node)
            }

        st.markdown("### 📊 Metrics Performance Evaluation Matrix")
        
        ui_report_data = []
        best_algo = None
        min_cost = float('inf')

        for algo, (path, cost) in results.items():
            readable_path = " → ".join(path) if path else "❌ Path Deficit Connection Blocked"
            readable_cost = cost if cost != float('inf') else "∞"
            
            ui_report_data.append({
                "Search Variant Subsystem Strategy": algo,
                "Computed Target Traversal Route": readable_path,
                "Path Cost Efficiency Rating": readable_cost
            })

            if cost < min_cost:
                min_cost = cost
                best_algo = algo

        # Render data table
        st.dataframe(pd.DataFrame(ui_report_data), use_container_width=True, hide_index=True)

        # UI Highlight Section for the Winner
        st.markdown("### 🏆 Benchmarking Optimization Verdict")
        if best_algo and min_cost != float('inf'):
            st.balloons()
            
            # Highlight with a sleek structural metric display block
            m_col1, m_col2 = st.columns(2)
            with m_col1:
                st.metric(label="Optimal Framework Strategy", value=best_algo)
            with m_col2:
                st.metric(label="Minimum Evaluated Cost Threshold Score", value=int(min_cost))
                
            st.success(f"**Optimization Verdict Matrix:** `{best_algo}` systematically isolated the most structurally sound navigational pathway profile setup context parameters.")
        else:
            st.error("No search algorithms were successfully able to locate a link trail connecting those chosen nodes.")
