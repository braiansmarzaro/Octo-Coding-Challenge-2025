"""
Week 4 Part 1: Shortest Path Counting with Time-dependent Edges
"""

from collections import defaultdict, deque
import re


def parse_graph_with_timesteps(filename):
    """Parse the DOT graph file to extract edges with timestep constraints."""
    edges = []
    nodes = set()
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if '--' in line:
                # Parse lines like: "AA" -- "BA" [timestep="odd"];
                match = re.match(r'"([^"]+)"\s*--\s*"([^"]+)"\s*\[timestep="(even|odd)"\]', line)
                if match:
                    node1 = match.group(1)
                    node2 = match.group(2)
                    timestep = match.group(3)
                    
                    edges.append((node1, node2, timestep))
                    nodes.add(node1)
                    nodes.add(node2)
    
    return edges, nodes


def count_shortest_paths(edges, start, end):
    """
    Count the number of shortest paths from start to end.
    
    The graph has time-dependent edges:
    - "even" edges can only be traversed at even timesteps
    - "odd" edges can only be traversed at odd timesteps
    - Each edge traversal takes 1 timestep
    - Can wait at any intersection (takes 1 timestep, changes parity)
    
    Returns: (shortest_distance, number_of_paths)
    """
    # Build adjacency list (undirected graph)
    graph = defaultdict(list)
    for node1, node2, timestep in edges:
        graph[node1].append((node2, timestep))
        graph[node2].append((node1, timestep))
    
    # Dijkstra's algorithm since all edges have weight 1
    # State: (node, timestep)
    # Use distance and count for each state
    import heapq
    
    pq = [(0, start, 0)]  # (distance, node, timestep)
    
    # Track best distance to each (node, timestep) state
    dist = {}
    dist[(start, 0)] = 0
    
    # Track number of shortest paths to each state
    count = {}
    count[(start, 0)] = 1
    
    # Track best distance to end node (regardless of timestep)
    best_to_end = float('inf')
    end_count = 0
    
    while pq:
        current_dist, current_node, current_time = heapq.heappop(pq)
        
        # Skip if we've already found a better path
        if current_dist > dist.get((current_node, current_time), float('inf')):
            continue
        
        # Check if we reached the end
        if current_node == end:
            if current_dist < best_to_end:
                best_to_end = current_dist
                end_count = count[(current_node, current_time)]
            elif current_dist == best_to_end:
                end_count += count[(current_node, current_time)]
            continue
        
        # Skip if this path is already longer than best path to end
        if current_dist >= best_to_end:
            continue
        
        current_count = count[(current_node, current_time)]
        
        # Option 1: Wait at current intersection (changes timestep parity)
        next_time_wait = current_time + 1
        next_dist = current_dist + 1
        wait_state = (current_node, next_time_wait)
        
        if wait_state not in dist or dist[wait_state] > next_dist:
            dist[wait_state] = next_dist
            count[wait_state] = current_count
            heapq.heappush(pq, (next_dist, current_node, next_time_wait))
        elif dist[wait_state] == next_dist:
            count[wait_state] += current_count
        
        # Option 2: Traverse each edge (if timestep matches)
        for neighbor, edge_type in graph[current_node]:
            can_traverse = (edge_type == "even" and current_time % 2 == 0) or \
                          (edge_type == "odd" and current_time % 2 == 1)
            
            if can_traverse:
                next_time = current_time + 1
                next_dist = current_dist + 1
                next_state = (neighbor, next_time)
                
                if next_state not in dist or dist[next_state] > next_dist:
                    dist[next_state] = next_dist
                    count[next_state] = current_count
                    heapq.heappush(pq, (next_dist, neighbor, next_time))
                elif dist[next_state] == next_dist:
                    count[next_state] += current_count
    
    return best_to_end, end_count


def solve_with_wait_option(edges, start, end):
    """
    Alternative solution that allows waiting at a node if needed.
    This explores if we can wait at a node to match the edge timing.
    """
    # Build adjacency list (undirected graph)
    graph = defaultdict(list)
    for node1, node2, timestep in edges:
        graph[node1].append((node2, timestep))
        graph[node2].append((node1, timestep))
    
    # BFS with state: (node, timestep)
    from collections import deque
    
    queue = deque([(start, 0, 1)])  # (node, timestep, path_count)
    
    # Best distance to reach (node, timestep_parity)
    best = {}
    best[(start, 0)] = (0, 1)  # (distance, count)
    
    result_distance = float('inf')
    result_count = 0
    
    while queue:
        current_node, current_time, path_count = queue.popleft()
        
        # Check if we've already found a better path to this state
        state = (current_node, current_time % 2)
        if state in best and best[state][0] < current_time:
            continue
        
        # Check if we reached the end
        if current_node == end:
            if current_time < result_distance:
                result_distance = current_time
                result_count = path_count
            elif current_time == result_distance:
                result_count += path_count
            continue
        
        # Skip if we've exceeded known shortest path to end
        if current_time >= result_distance:
            continue
        
        # Try each neighbor
        for neighbor, edge_type in graph[current_node]:
            # Check if we can traverse this edge now
            can_traverse_now = (edge_type == "even" and current_time % 2 == 0) or \
                              (edge_type == "odd" and current_time % 2 == 1)
            
            if can_traverse_now:
                next_time = current_time + 1
                next_state = (neighbor, next_time % 2)
                
                if next_state not in best or best[next_state][0] >= next_time:
                    if next_state not in best:
                        best[next_state] = (next_time, 0)
                    
                    if best[next_state][0] == next_time:
                        best[next_state] = (next_time, best[next_state][1] + path_count)
                        queue.append((neighbor, next_time, path_count))
                    elif best[next_state][0] > next_time:
                        best[next_state] = (next_time, path_count)
                        queue.append((neighbor, next_time, path_count))
    
    return result_distance, result_count


def main():
    print("=" * 70)
    print("VALIDATING WITH EXAMPLE (ex4_1.txt)")
    print("=" * 70)
    
    edges, nodes = parse_graph_with_timesteps("ex4_1.txt")
    print(f"Nodes: {sorted(nodes)}")
    print(f"Number of nodes: {len(nodes)}")
    print(f"Number of edges: {len(edges)}")
    print()
    
    print("Edges:")
    for node1, node2, timestep in edges:
        print(f"  {node1} -- {node2} [{timestep}]")
    print()
    
    # Find shortest paths with detailed output
    distance, count = count_shortest_paths_debug(edges, "AA", "ZZ")
    
    print(f"\nShortest distance from AA to ZZ: {distance} timesteps")
    print(f"Number of shortest paths: {count}")
    
    # Now solve the real problem
    print("\n" + "=" * 70)
    print("SOLVING REAL PROBLEM (4_1.txt)")
    print("=" * 70)
    
    edges, nodes = parse_graph_with_timesteps("4_1.txt")
    print(f"Number of nodes: {len(nodes)}")
    print(f"Number of edges: {len(edges)}")
    print()
    
    distance, count = count_shortest_paths(edges, "AA", "ZZ")
    
    print(f"Shortest distance from AA to ZZ: {distance} timesteps")
    print(f"Number of shortest paths: {count}")
    
    return distance, count


def count_shortest_paths_debug(edges, start, end):
    """Debug version that shows all shortest paths."""
    from collections import defaultdict
    import heapq
    
    # Build adjacency list (undirected graph)
    graph = defaultdict(list)
    for node1, node2, timestep in edges:
        graph[node1].append((node2, timestep))
        graph[node2].append((node1, timestep))
    
    # Track paths for debugging
    pq = [(0, start, 0, [start])]  # (distance, node, timestep, path)
    
    dist = {}
    dist[(start, 0)] = 0
    
    count = {}
    count[(start, 0)] = 1
    
    # Store actual paths
    paths_to_state = {}
    paths_to_state[(start, 0)] = [[start]]
    
    best_to_end = float('inf')
    end_paths = []
    
    while pq:
        current_dist, current_node, current_time, path = heapq.heappop(pq)
        
        # Skip if we've already processed a better path
        if current_dist > dist.get((current_node, current_time), float('inf')):
            continue
        
        # Check if we reached the end
        if current_node == end:
            if current_dist < best_to_end:
                best_to_end = current_dist
                end_paths = [path]
            elif current_dist == best_to_end:
                end_paths.append(path)
            continue
        
        # Skip if this path is already longer than best path to end
        if current_dist >= best_to_end:
            continue
        
        # Option 1: Wait at current intersection
        next_time_wait = current_time + 1
        next_dist = current_dist + 1
        wait_state = (current_node, next_time_wait)
        wait_path = path + [f"[wait@{current_node}]"]
        
        if wait_state not in dist or dist[wait_state] >= next_dist:
            if wait_state not in dist or dist[wait_state] > next_dist:
                dist[wait_state] = next_dist
                count[wait_state] = 1
                paths_to_state[wait_state] = [wait_path]
            elif dist[wait_state] == next_dist:
                count[wait_state] += 1
                paths_to_state[wait_state].append(wait_path)
            heapq.heappush(pq, (next_dist, current_node, next_time_wait, wait_path))
        
        # Option 2: Traverse each edge
        for neighbor, edge_type in graph[current_node]:
            can_traverse = (edge_type == "even" and current_time % 2 == 0) or \
                          (edge_type == "odd" and current_time % 2 == 1)
            
            if can_traverse:
                next_time = current_time + 1
                next_dist = current_dist + 1
                next_state = (neighbor, next_time)
                next_path = path + [neighbor]
                
                if next_state not in dist or dist[next_state] >= next_dist:
                    if next_state not in dist or dist[next_state] > next_dist:
                        dist[next_state] = next_dist
                        count[next_state] = 1
                        paths_to_state[next_state] = [next_path]
                    elif dist[next_state] == next_dist:
                        count[next_state] += 1
                        if next_state in paths_to_state:
                            paths_to_state[next_state].append(next_path)
                    heapq.heappush(pq, (next_dist, neighbor, next_time, next_path))
    
    print(f"\nAll shortest paths (distance {best_to_end}):")
    for i, path in enumerate(end_paths, 1):
        # Count actual moves (not waits)
        actual_moves = [p for p in path if not p.startswith('[wait')]
        print(f"  Path {i}: {' -> '.join(path)}")
    
    return best_to_end, len(end_paths)


if __name__ == "__main__":
    result = main()
