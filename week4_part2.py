"""
Week 4 Part 2: Task Ordering with Topological Sort
"""

from collections import defaultdict, deque


def parse_graph(filename):
    """Parse the digraph file to extract dependencies."""
    edges = []
    nodes = set()
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if '->' in line:
                # Parse lines like: "0" -> "3";
                parts = line.split('->')
                from_node = parts[0].strip().strip('"').strip()
                to_node = parts[1].strip().strip(';').strip().strip('"').strip()
                
                from_node = int(from_node)
                to_node = int(to_node)
                
                edges.append((from_node, to_node))
                nodes.add(from_node)
                nodes.add(to_node)
    
    return edges, nodes


def topological_sort(edges, nodes):
    """
    Perform topological sort using Kahn's algorithm.
    Returns a list of nodes in valid execution order.
    """
    # Build adjacency list and in-degree count
    graph = defaultdict(list)
    in_degree = {node: 0 for node in nodes}
    
    for from_node, to_node in edges:
        graph[from_node].append(to_node)
        in_degree[to_node] += 1
    
    # Find all nodes with no incoming edges
    queue = deque([node for node in nodes if in_degree[node] == 0])
    result = []
    
    while queue:
        # Sort to ensure consistent ordering when there are multiple valid choices
        queue = deque(sorted(queue))
        node = queue.popleft()
        result.append(node)
        
        # Reduce in-degree for all neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all nodes were processed (no cycles)
    if len(result) != len(nodes):
        raise ValueError("Graph has a cycle!")
    
    return result


def main():
    # First, validate approach with example
    print("=" * 60)
    print("VALIDATING WITH EXAMPLE (ex4_2.txt)")
    print("=" * 60)
    
    edges, nodes = parse_graph("ex4_2.txt")
    print(f"Nodes: {sorted(nodes)}")
    print(f"Number of nodes: {len(nodes)}")
    
    order = topological_sort(edges, nodes)
    print(f"Valid execution order: {order}")
    print()
    
    # Now solve the real problem
    print("=" * 60)
    print("SOLVING REAL PROBLEM (4_2.txt)")
    print("=" * 60)
    
    edges, nodes = parse_graph("4_2.txt")
    print(f"Nodes: {sorted(nodes)}")
    print(f"Number of nodes: {len(nodes)}")
    print(f"Number of edges: {len(edges)}")
    print()
    
    order = topological_sort(edges, nodes)
    print(f"Valid execution order: {order}")
    print(f"\nLength: {len(order)}")
    
    return order


if __name__ == "__main__":
    result = main()
