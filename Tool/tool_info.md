Tool requirements
=================
Input:
1. a network/file path to the network. (string)
2. min number of communities to look for in the network (integer)
3. max number of communities to look for in the network - can be identical to input no. 2 (integer)
4. percent of edges to remove for the link prediction (float)
5. whether edge removal should be from all possible (0/1) or actual (1) edges. (all/actual - string)

Output:
1. soft membership for the nodes - allow for uni/bi partite
2. a table with: for each required K in the input: maximum likelyhood + AIC + BIC
3. link prediction results (a matrix of every paired layers + diagonal)