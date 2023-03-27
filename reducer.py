import sys
import random

adj_list = {}
alpha = 0.85
personalization = {}
pagerank_values = {}


# Parse input from stdin
for line in sys.stdin:
    node, neighbors = line.strip().split('\t')
    adj_list[node] = neighbors.split()
    pagerank_values[node] = 0.0


# Initialize personalization vector
source_nodes = ['1', '2', '3']
for node in source_nodes:
    personalization[node] = 1.0 / len(source_nodes)


# Run personalized PageRank for each source node
for source_node in source_nodes:

    # Reset PageRank values for all nodes
    for node in pagerank_values:
        pagerank_values[node] = 0.0

    # Set the initial PageRank value for the source node
    pagerank_values[source_node] = 1.0

    # Run the PageRank algorithm for a fixed number of iterations
    for i in range(10): 
        new_pagerank_values = {}
        sink_nodes = []
        sink_mass = 0

        # Find sink nodes and calculate their mass
        for node in pagerank_values:
            if not adj_list[node]:
                sink_nodes.append(node)
                sink_mass += pagerank_values[node]

        # Update PageRank values for each node
        for node in pagerank_values:
            if node in source_nodes:
                # Do not update source nodes
                new_pagerank_values[node] = pagerank_values[node]
                continue

            # Calculate contributions from neighbors
            neighbor_contributions = 0
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if neighbor in pagerank_values and len(adj_list[neighbor]) > 0:
                        neighbor_contributions += pagerank_values[neighbor] / len(adj_list[neighbor])
            else:
                # If node has no outlinks, choose a random source node
                random_node = random.choice(source_nodes)
                neighbor_contributions = pagerank_values[random_node] / len(source_nodes)

            # Calculate new PageRank value for the node
            new_pagerank_value = (1 - alpha) / len(pagerank_values) + alpha * (sink_mass / len(pagerank_values) + neighbor_contributions)

            # Update the PageRank value for the node
            new_pagerank_values[node] = new_pagerank_value

        # Update PageRank values for sink nodes
        for node in sink_nodes:
            new_pagerank_value = (1 - alpha) / len(pagerank_values) + alpha * (sink_mass / len(pagerank_values))
            new_pagerank_values[node] = new_pagerank_value

        # Apply personalization vector
        for node in personalization:
            new_pagerank_values[node] += alpha * personalization[node]

        # Update PageRank values for all nodes
        pagerank_values = new_pagerank_values

    # Print PageRank values for the current source node
    for node in pagerank_values:
        print(f"{source_node}\t{node}\t{pagerank_values[node]}")

