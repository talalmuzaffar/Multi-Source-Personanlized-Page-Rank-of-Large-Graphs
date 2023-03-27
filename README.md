# Multi Source Personalized PageRank Algorithm
This repository contains an implementation of the Multi Source Personalized PageRank algorithm using Hadoop MapReduce.

## Why it's Better
The PageRank algorithm with personalization vector is an improvement over the basic PageRank algorithm because it takes into account the user's preferences when ranking web pages. By allowing the user to specify a personalization vector, the algorithm can be customized to reflect their interests and preferences. This can lead to more accurate and relevant search results, which can save time and effort for the user.

## mapper.py
The Mapper reads input from standard input and creates an adjacency list in the form of a dictionary. It then iterates through the dictionary and prints the key-value pairs to standard output in the required format.

## reducer.py
The Reducer reads input from standard input and parses the input to create an adjacency list and initialize the necessary variables. It then runs the Personalized PageRank algorithm for each source node, using the adjacency list, personalization vector, and alpha value. The algorithm is run for a fixed number of iterations and the resulting PageRank values are printed to standard output in the required format.

## Requirements
This code requires Python 3 and the following packages:

- sys
- random

## Usage
To run the code, follow these steps:

- Clone the repository.
- Open the terminal and navigate to the cloned repository.
- Run the following command to run the Mapper and Reducer on the provided input file:
`cat input.txt | python3 mapper.py | sort | python3 reducer.py`
- The resulting PageRank values will be printed to standard output in the required format.

## Input Format
The input file should contain lines in the following format:
`source_node	target_node`

Lines beginning with `"#"` are ignored.

## Output Format
The output will be in the following format:
`source_node	target_node	PageRank_value`
