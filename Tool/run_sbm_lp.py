# =============== run_sbm_lb.py ===================
# Date: 04.06.23 
# author: Geut Galai
# description: This script combines code from preciously written 
# tools to create a tool that recieves data for a multilayer network, 
# and runs an SBM analysis as well as a link prediction analysis
# ===================================================

# ===================================================
# Assumption:
# 1. all the layers are in the same group (L = 1)
# 2. Nodes and layers are numbered consecutively [0,...,#nodes] , [0,...,#layers]
# 3. the TensorialMMSBM.py script file is one level up in the directory tree.
#
# example cmd to call this script:
# python run_sbm_lb.py <path> 3 4 0.2 all 
# ===================================================

# Imports --------
import sys
import os
import functions as fnc

# Consts ------
removal_itr = 5
sbm_itr_num = 10

# Run --------
# Get input from command line
net_path=sys.argv[1]
min_k=int(sys.argv[2])
max_k=int(sys.argv[3])
to_remove=float(sys.argv[4])
removal_type=sys.argv[5]

# validate input
if (not os.path.isfile(net_path)):
    raise("Network file path is incorrect - not a file.")
if (not min_k > 0):
    raise("Min number of communitis to detect must be higher then 0.")
if (not max_k > min_k):
    raise("Max number of communitis to detect must be higher then the min.")
if (to_remove >= 1 or to_remove <= 0):
    raise("Proportion of links to remove must be a number between 0 and 1.")
if (not (removal_type == "all" or removal_type == "actual")):
    # "all" means from all possible links, whether they exist or not in the network.
    # "actual" means removing links only from actual links that exist in the networks.
    raise("Link removal method must either be \"all\" or \"actual\".")



# TODO: temp values to be deleted when done working
net_path= "input/canary_islands_edgelist.csv"
min_k=3
max_k=4
to_remove=0.2
removal_type="all"



# read network:
intra_only = fnc.load_network_intralayer(net_path)

# remove links according to settings
if removal_type == "all":
   new_net = fnc.link_removal_from_all(intra_only, to_remove)
else:
   new_net = fnc.link_removal_from_actual(intra_only, to_remove)
# TODO should this occure multiple times as the removal is random? 
#      shai says yes - done as running this script multiple times?

# save new networks to a file
# TODO values I need to extract for performing the tensorial analysis: 
# taining file mame
# test file name
# number of nodes
# number of layers
# k
# L = 1
# labels = 1
# iterations = sbm_itr_num
# should print params = 1
# output_folder = "output/canary/"


# go over range of k
for i in range (min_k, max_k+1):
    print("Calling TensorialMMSBM.py script using K = ", int(i))

    prms = [69,85,i,1,1,sbm_itr_num,1] # TODO intex 5 needs to be checked what is the best option here
    ints = " ".join([str(x) for x in prms])
    cmd = "python3 ../TensorialMMSBM.py " + train_file + " " + testfile + " " + ints + " " + outputfolder

    print("command: " + cmd)
    os.system(cmd)

    print("Dont with K = ", int(i))

# run the tensorial tool TensorialMMSBM.py with the network, for 10 iterations
# TODO check if cd is made using the partial network or the whole thing (we want the second ofc) seems like it is.

# now we have multiple cd for each node 
# TODO how to get a single membership from the all the iterations

# calculate AIC BIC for each K in the renge, this happens after all the params files are available.
# get k files
files = listdir('/Users/geutg/Documents/GitHub/MMmultilayer/output')

# get the likelihood
ml = np.zeros(shape=(1,10))
for file in files:
    #get likelihood from files
    with open(file) as f:
    first_line = f.readline()


