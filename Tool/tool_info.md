Tool requirements
=================
Input:
1. a network/file path to the network.
2. max number or range of communities to look for in the network
3. percent of edges to remove for the link prediction
4. whether edge removal should be from all possible (0/1) or actual (1) edges.

Output:
1. soft membership for the nodes - allow for uni/bi partite
2. a table with: for each required K in the input: maximum likelyhood + AIC + BIC
3. link prediction results (a matrix of every paired layers + diabonal)