import sys
# Read input from standard input
adj_list={}

for line in sys.stdin:

    if line.startswith("#"):
        continue


    row = line.strip().split("\t")
    source, target = (row[0]), row[1]

    if source not in adj_list:
        adj_list[source] = [target]
    else:
        adj_list[source].append(target)
        

for source, targets in adj_list.items():
    print(f"{source}\t{' '.join(targets)}")
