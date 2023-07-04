# =============== run_sbm_lb.py ===================
# Date: 04.06.23 
# author: Geut Galai
# description: This script combines code from preciously written 
# tools to create a tool that recieves data for a multilayer network, 
# and runs an SBM analysis as well as a link prediction analysis
# ============================================

# imports --------
import sys

# Run --------

# Get input from command line


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



