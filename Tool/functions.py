# =============== functions.py ===================
# Date: 05.12.23 
# author: Geut Galai
# description: This script holds functions used in the pipeline,  
# here organized by logic an usage
# ================================================

# Imports ---------------------------------------------
import random
import itertools
import numpy as np
import pandas as pd


# Run -------------------------------------------------
# I/O functions
def load_network_intralayer(file_path):
    # file format: first line has column names, is comma seperated (CSV), with these columns:
    # layer_from,node_from,layer_to,node_to,weight
    fh=open(file_path,'r')
    next(fh) # skip the first line with the column names
    igot=fh.readlines()
    
    trainn=[]
    for line in igot:
        about = line.strip().split(',')
        if (about[0] == about[2]): # make sure we only have intralayer edges
            trainn.append((int(about[0]),int(about[1]),int(about[3])))
    fh.close()

    net = pd.DataFrame(trainn, columns =['layer', 'from', 'to'])
    return net


# link removal
def link_removal_from_all(network, percent):
    ## take % of that edge pair randomly and set any edges appeared in that 20% to be 0
    all_edge_pair = list(itertools.product(node_in_layer,node_in_layer))
    all_edge_pair = [x for x in all_edge_pair if x[0]!=x[1]]
    remove_count = int(round(len(all_edge_pair)*(1-percent)))
    removed_edges = random.sample(all_edge_pair, remove_count)
    removed_edges = [(int(x[0]), int(x[1])) for x in removed_edges]


def link_removal_from_actual(network, percent): # TODO finish
    ## take % of that edge pair randomly and set any edges appeared in that 20% to be 0
    all_edge_pair = list(itertools.product(node_in_layer,node_in_layer))
    all_edge_pair = [x for x in all_edge_pair if x[0]!=x[1]]
    remove_count = int(round(len(all_edge_pair)*0.8))
    removed_edges = random.sample(all_edge_pair, remove_count)
    removed_edges = [(int(x[0]), int(x[1])) for x in removed_edges]


# validation functions
def XIC_table_result(arr, l, n):
    arr = [ -74732.3306278295,-71545.39906002226,-68971.3259163048,-67237.86495618176,
            -65561.31909272182,-63687.30706099175,-63145.9638735542,-62266.437700266666,
            -60799.18656109925,-60179.40374510149,-60117.32489620492,-58710.88873395683 ,
            -58408.32769170688,-57978.673102399975] # TEMP

    l = 12 # TEMP
    n = 1134 # TEMP

    for k in range(2,15):
        AIC = 2*(2*n*k+l*k**2) - 2*arr[k-2]
        print("AIC", AIC)
    
    for k in range(2,15):
        BIC = np.log(n)*(2*n*k+l*k**2) - 2*arr[k-2]
        print("BIC", BIC)

