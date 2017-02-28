# for Autonomous systems  networks 
import networkx as nx
import pickle
import numpy as np
import kcore_decomposition as kde
import kcorenew as kc
import jaccards as j
import make_seed_n as ms
import os
import matplotlib.pyplot as plt

topc = []
top5c = []
top5b = []
unodes = []
#sp = open("spread_result_as_predict.txt","w")
ids = 0
close_er = pickle.load(open("as_errors_close.p","rb"))
bet_er =  pickle.load(open("as_errors_bets.p","rb"))

sp  = open("predict1_spread_result_as.txt","w")
sp1 = open("predict1_bet_result_as.txt","w")


for v in range(34,65,1):
	gn  = 'as_edges/as_'+str(v)+".txt"
	gn1  = 'as_edges/as_'+str(v+1)+".txt"
	#gn = "n_as/as_"+str(v)+".txt"
	#gn1 = 'as_'+str(v)
	g = nx.read_edgelist(gn,nodetype=int)
	g1 = nx.read_edgelist(gn1,nodetype=int)
	#g2 = nx.convert_node_labels_to_integers(g, first_label=0, ordering='default', label_attribute=None)
	print v,g.number_of_nodes(),g.number_of_edges()
	#nx.write_edgelist(g,'as_'+str(v)+'.txt',data=False)
	#nx.write_edgelist(g2,gn2,data=False)
	c1 = pickle.load(open("as_"+str(v)+"close.p","rb"))
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
	ms.seed_file(c3,close_er[ids],"close")
        c1 = pickle.load(open("as_"+str(v)+"betw.p","rb"))
        c2 = c1.items()
        c3 = sorted(c2,key = lambda x:x[1],reverse=True)
	ms.seed_file(c3,bet_er[ids],"betw")
	size = g1.number_of_nodes()
	output = os.popen('java MultiSpreads '+str(size)+" "+gn1).read()
	out = os.popen('./new_centrality '+'seed_betw.txt '+gn1).read()
        op = output.split()
        print out
        print op
        sp.write(str(v)+'\t'+str(op[0])+"\t"+str(op[1])+'\n')
        sp1.write(str(v)+'\t'+str(out)+"\n")
	ids = ids+1


sp.close()
sp1.close()
