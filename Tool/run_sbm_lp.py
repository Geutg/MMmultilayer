# =============== run_sbm_lb.py ===================
# Date: 04.06.23 
# author: Geut Galai
# description: This script combines code from preciously written 
# tools to create a tool that recieves data for a multilayer network, 
# and runs an SBM analysis as well as a link prediction analysis
# ============================================

# imports --------
import sys
import os

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
    raise("Link removal method must either \"all\" or \"actual\".")


#target output for running tensorial:
train=sys.argv[1] # train
test=sys.argv[2] # test
p=int(sys.argv[3]) # nodes drugs69
T=int(sys.argv[4]) # layers drugs85
K=int(sys.argv[5]) # groups of nodes
L=K
S=int(sys.argv[6]) # groups of layers
R=int(sys.argv[7]) # different labels
sampling=int(sys.argv[8]) # different initializations
printp=int(sys.argv[9]) # 0/1 0noprint 1 print params



