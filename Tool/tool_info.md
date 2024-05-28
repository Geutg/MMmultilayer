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




Tool Snapshot
=============

This section is here so that next time I have to work on this tool, getting up to speed will be easier.

  

This tool is based on the this paper: https://arxiv.org/abs/1803.01616

not used in the cancer paper but recommended by Xei and Jamie.

  

this tool is mainly link prediction, but its usage is not completely clear right now, and we contacted Marta Sales-Pardo

requesting someone for a little help.

- it gets a training + test data sets and predicts link types, while producing mixed membership information about nodes, layers and one more thing, as params.


questions I wanted to ask (also in the tablet):

1. is there a way to disregard layer groups? like set L = 1?
2. does link prediction also predicts their existence or only their type? how are non-existing links? as link type or just absent from the edge list? (this Q is a bit different then the tablet one)
3. how do i represent bipartite vs unipartite networks? and directed vs undirected?
4. is there meaning to the weight of the edges? if so, do they have restrictions (e.g. only positive/integers)?
5. do interlayer edges have no meaning in this analysis?
6. how do you represent the network if it has only one type of links (R=1)?
7. what does the last chunk of rows in the "params" output files mean?
8. cd - is it done one the partial network? is there an option to have it on the whole network?
9. what is the best way to determine a node's membership from the set of mixed membership param files?
10. lp - using one layer to predict another, is it an issue if the same edge appears more then once in the training set?
with those answers I can better define the tool.
  

## structure

running the main file, `run_sbm_lp.py` is supposed to produce results according to the above "Tool requirements".

but:

the tool right now is built as such that it runs on a single network once, while removing randomly links for testing dataset.

this is not enough as due to the removal being random, we need to repeat the process (did xei repeat the process in the cancer code? i need to check) - do i just run this script multiple times?


## important: is the cd part (mixed membership) produced on a partial network? on the test or train, or both?


## missing

still missing from the implementation at the moment:

- finish edge removal (both types) logic + saving them in files (what is the best way to organize all the data files? need to remember to make sure different iterations dont override eachother)
- finish building output folder system for writing and reading of likelihood, for AIC and BIC + save the results
- issue: should different edge removal iteration be in a separate process or synchronically?
	  if the first, how do i make the script wait for all of them as the script needs to collect values from all of them? also should they all append to the same output AIC BIC file?

* in the end, the files that will exist:
	for each input network (e.g. canary islands): 
		fore each edge removal iteration:
			several sets of cd params
			->
			need to average their likelihood to have one set of AIC BIC - one value for each K

 missing: get the membership itself from the sets of memberships for each node? how do i do that?
 
 missing 2: link prediction  - how to get from one layer to another? just make a new edge list containing both layers (more like a layer and then some)? is it fine to have double the edges?
 ->
 this might mean the need to call for the link prediction in a separate script altogether, especially of the input edge list is different from the one on the cd analysis.
 ->
 all in all some of Xei's code can be relevant in the implementation of this part of the tool. Xei's code is given in th repo:
 https://github.com/Ecological-Complexity-Lab/lp_sbm_tool